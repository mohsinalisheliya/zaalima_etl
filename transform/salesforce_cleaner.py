import polars as pl
import logging

def clean_salesforce_data(raw_data):
    logging.info("Cleaning Salesforce data with Polars...")
    if not raw_data:
        return pl.DataFrame()
        
    df = pl.DataFrame(raw_data)
    
    # Drop empty leads and standardize status strings to UPPERCASE
    df = df.drop_nulls()
    df = df.with_columns(pl.col("status").str.to_uppercase())
    return df