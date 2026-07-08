import logging
from extract import fetch_payment_data
from transform.data_cleaner import clean_data
from load import load_data
from extract.s3_upload import upload_to_datalake

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

    # Step 1: Paginated Extraction
    logging.info("Step 1: Extracting paginated data (Raghuvarshan's Engine)")
    raw_data = fetch_payment_data()

    logging.info("Step 1.5: Backing up raw data to S3 Data Lake")
    upload_to_datalake(raw_data, "daily_extract.json")

    # Step 2: High-Speed Polars Transformation
    logging.info("Step 2: Transforming data with Polars (Hanna's Engine)")
    cleaned_df = clean_data(raw_data)

    # Step 3: Bulk Database Loading
    logging.info("Step 3: Bulk Database Loading (Sidram's Engine)")
    load_data(cleaned_df)

    logging.info("Pipeline execution finished successfully! 🎉")

if __name__ == "__main__":
    main()