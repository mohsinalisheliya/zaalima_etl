import logging
from extract import fetch_payment_data
from transform.data_cleaner import clean_data, mask_pii
from load import load_data
from extract.s3_upload import upload_to_datalake
from extract.salesforce_api import fetch_salesforce_leads
from transform.salesforce_cleaner import clean_salesforce_data
from dags.slack_alert import send_slack_alert

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("pipeline_execution.log"),
        logging.StreamHandler()
    ]
)

def main():
    # We wrap the entire pipeline in a try/except block to catch crashes
    try:
        logging.info("Starting Secure Zaalima ETL Pipeline...")

        # --- STRIPE PIPELINE ---
        logging.info("Step 1: Extracting paginated data (Stripe)")
        raw_data = fetch_payment_data()
        upload_to_datalake(raw_data, "daily_extract.json")

        logging.info("Step 2: Transforming data with Polars (Stripe)")
        cleaned_df = clean_data(raw_data)
        
        # ✨ NEW: Masking sensitive transaction IDs for privacy
        logging.info("Step 2.5: Masking sensitive PII data (Stripe)")
        cleaned_df = mask_pii(cleaned_df, "id")

        logging.info("Step 3: Bulk Database Loading (Stripe)")
        load_data(cleaned_df)


        # --- SALESFORCE PIPELINE ---
        logging.info("Step 4: Extracting Salesforce Data")
        raw_crm = fetch_salesforce_leads()

        logging.info("Step 5: Transforming Salesforce Data")
        clean_crm = clean_salesforce_data(raw_crm)
        
        # ✨ NEW: Masking sensitive Lead IDs for privacy
        logging.info("Step 5.5: Masking sensitive PII data (Salesforce)")
        clean_crm = mask_pii(clean_crm, "lead_id")

        logging.info("Step 6: Loading Salesforce Data")
        logging.info(f"Ready to load {clean_crm.height} CRM records.")

        logging.info("Pipeline execution finished successfully! 🎉")
        
    except Exception as e:
        # ✨ NEW: If anything fails, send a Slack message!
        logging.critical(f"Pipeline crashed! Triggering Slack alert... Error: {e}")
        send_slack_alert(f"Critical Pipeline Failure: {str(e)}")

if __name__ == "__main__":
    main()