import logging
from extract import fetch_payment_data
from transform.data_cleaner import clean_data
from load import load_data

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("pipeline_execution.log"), 
        logging.StreamHandler()
    ]
)

def main():
    logging.info("Starting Zaalima ETL Pipeline...")

    logging.info("Step 1: Extracting data (Raghuvarshan's Engine)")
    raw_data = fetch_payment_data()

    logging.info("Step 2: Transforming data (Hanna's Engine)")
    
    cleaned_data = clean_data(raw_data, date_column=None)
    logging.info(f"Cleaned data ready. {len(cleaned_data)} rows.")

    logging.info("Step 3: Loading data (Sidram's Engine)")
    load_data(cleaned_data)

    logging.info("Pipeline execution finished successfully! ")

if __name__ == "__main__":
    main()