import logging
from .database import engine

def load_data(df):
    """
    Takes a Polars DataFrame and performs a bulk insert into the database.
    """
    logging.info("Starting database connection...")
    
    if df.is_empty():
        logging.warning("No data to load. Skipping database bulk insert.")
        return

    logging.info(f"Preparing to bulk load {df.height} rows into the warehouse...")

    try:
        # Polars native ultra-fast database insertion
        df.write_database(
            table_name="payments",
            connection=engine,
            if_table_exists="append"
        )
        logging.info("✅ Bulk insert completed successfully!")
    except Exception as e:
        logging.error(f"Database insertion failed: {e}")