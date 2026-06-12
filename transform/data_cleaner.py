import pandas as pd


def clean_data(raw_data, date_column="date"):
    

    # Convert JSON/dictionary to DataFrame
    df = pd.DataFrame(raw_data)

    # Drop rows with null values
    df = df.dropna()

    # Standardize date format
    if date_column in df.columns:
        df[date_column] = pd.to_datetime(
            df[date_column],
            errors="coerce"
        ).dt.strftime("%Y-%m-%d")

    # Remove duplicate records
    df = df.drop_duplicates()

    return df


#