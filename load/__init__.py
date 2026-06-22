import logging
from load.database import engine

def load_data(cleaned_df):
    """
    Loads cleaned dataframe into PostgreSQL.
    """

    logging.info("Starting database connection...")

    if cleaned_df.empty:
        logging.warning("No data to load.")
        return False

    try:
        cleaned_df.to_sql(
            name="users",
            con=engine,
            if_exists="append",
            index=False
        )

        logging.info(
            f"Loaded {len(cleaned_df)} rows into PostgreSQL."
        )

        return True

    except Exception as e:
        logging.error(f"Database load failed: {e}")
        return False