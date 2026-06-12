import logging

# Set up the logging configuration so it prints timestamps and info
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    logging.info("Starting Zaalima ETL Pipeline...")

    # Note: We will uncomment these imports tomorrow once the team finishes pushing their code!
    # from extract import extract_data
    # from transform import clean_data
    # from load import load_data

    logging.info("Step 1: Extracting data (Pending Raghuvarshan's code)")
    # raw_data = extract_data()

    logging.info("Step 2: Transforming data (Pending Hanna's code)")
    # cleaned_data = clean_data(raw_data)

    logging.info("Step 3: Loading data to database (Pending Sidram's code)")
    # load_data(cleaned_data)

    logging.info("Pipeline execution finished successfully!")

if __name__ == "__main__":
    main()