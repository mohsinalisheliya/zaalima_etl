import pandas as pd
from transform.data_cleaner import clean_data

def test_clean_data_removes_nulls():
    raw_data = [
        {"id": 1, "amount": 100},
        {"id": 2, "amount": None}
    ]

    df = clean_data(raw_data, date_column=None)

    assert len(df) == 1
    assert df.iloc[0]["id"] == 1