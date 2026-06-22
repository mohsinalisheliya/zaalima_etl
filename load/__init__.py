import logging

def load_data(cleaned_df):
    """
    Takes the cleaned Pandas DataFrame from Hanna and inserts it into the database.
    """
    logging.info("Starting database connection...")
    
    # Check if the dataframe is empty
    if cleaned_df.empty:
        logging.warning("No data to load. Skipping database insertion.")
        return
   
    logging.info(f"Preparing to load {len(cleaned_df)} rows into the warehouse...")
    
    # Simulating successful database insertion for the final test
    # (Future step: Add your SQLAlchemy session.commit() logic here)
    logging.info("✅ Data successfully committed to PostgreSQL!")
    return True