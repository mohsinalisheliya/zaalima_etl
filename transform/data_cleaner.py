import pandas as pd
import logging
import requests


def clean_data(raw_data, date_column=None):
    try:
        # Convert JSON data to DataFrame
        df = pd.DataFrame(raw_data)

        # Remove rows with null values
        df = df.dropna()

        # Standardize date format if a date column exists
        if date_column and date_column in df.columns:
            df[date_column] = pd.to_datetime(
                df[date_column],
                errors="coerce"
            ).dt.strftime("%Y-%m-%d")

        # Remove duplicate records
        df = df.drop_duplicates()

        return df

    except Exception as e:
        logging.error("Data schema mismatch!")
        logging.error(str(e))
        return pd.DataFrame()


if __name__ == "__main__":
    # Fetch sample data from API
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )

    sample_data = response.json()

    cleaned_df = clean_data(
        sample_data,
        date_column=None
    )
   
    print(cleaned_df.head())
    


