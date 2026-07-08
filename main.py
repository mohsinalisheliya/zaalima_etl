import logging
from extract import fetch_payment_data
from transform.data_cleaner import clean_data
from load import load_data
from extract.s3_upload import upload_to_datalake
from extract.salesforce_api import fetch_salesforce_leads
from transform.salesforce_cleaner import clean_salesforce_data

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("pipeline_execution.log"),
        logging.StreamHandler()
    ]
)

def main():
    logging.info("Starting Polars-optimized Zaalima ETL Pipeline...")

    # Step 1: Paginated Extraction (Stripe)
    logging.info("Step 1: Extracting paginated data (Raghuvarshan's Engine)")
    raw_data = fetch_payment_data()

    logging.info("Step 1.5: Backing up raw data to S3 Data Lake")
    upload_to_datalake(raw_data, "daily_extract.json")

    # Step 2: High-Speed Polars Transformation (Stripe)
    logging.info("Step 2: Transforming data with Polars (Hanna's Engine)")
    cleaned_df = clean_data(raw_data)

    # Step 3: Bulk Database Loading (Stripe)
    logging.info("Step 3: Bulk Database Loading (Sidram's Engine)")
    load_data(cleaned_df)

    # Step 4: Extracting Salesforce Data
    logging.info("Step 4: Extracting Salesforce Data")
    raw_crm = fetch_salesforce_leads()

    # Step 5: Transforming Salesforce Data
    logging.info("Step 5: Transforming Salesforce Data")
    clean_crm = clean_salesforce_data(raw_crm)

    # Step 6: Loading Salesforce Data
    logging.info("Step 6: Loading Salesforce Data")
    # In production, pass this to Sidram's loader
    logging.info(f"Ready to load {clean_crm.height} CRM records.")

    logging.info("Pipeline execution finished successfully! 🎉")

if __name__ == "__main__":
    main()