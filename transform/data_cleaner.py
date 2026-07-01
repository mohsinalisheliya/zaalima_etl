import polars as pl
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def clean_data(raw_data, date_column=None):
    logging.info("Starting high-performance data cleaning with Polars...")
    
    if not raw_data:
        logging.warning("No data received for transformation.")
        return pl.DataFrame()
        
    try:
        # Load raw dictionaries into a Polars DataFrame
        df = pl.DataFrame(raw_data)
        
        # High-speed data scrubbing
        df = df.drop_nulls()
        df = df.unique()
        
        logging.info(f"Polars cleaning complete. Processed {df.height} rows.")
        return df
        
    except Exception as e:
        logging.error(f"Polars transformation failed: {e}")
        return pl.DataFrame()