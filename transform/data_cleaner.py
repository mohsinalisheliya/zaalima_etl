import polars as pl
import logging
import hashlib

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
        df = pl.DataFrame(raw_data)
        df = df.drop_nulls()
        df = df.unique()
        
        logging.info(f"Polars cleaning complete. Processed {df.height} rows.")
        return df
        
    except Exception as e:
        logging.error(f"Polars transformation failed: {e}")
        return pl.DataFrame()

def mask_pii(df: pl.DataFrame, column_name: str) -> pl.DataFrame:
    """Hashes sensitive data like emails or user IDs for privacy."""
    logging.info(f"Masking PII in column: {column_name}")
    if column_name in df.columns:
        # Simple hash masking simulation for Polars
        return df.with_columns(pl.col(column_name).map_elements(lambda x: hashlib.sha256(str(x).encode()).hexdigest(), return_dtype=pl.String))
    return df