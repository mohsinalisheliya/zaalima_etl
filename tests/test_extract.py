import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from extract import fetch_payment_data

def test_fetch_payment_data_pagination():
    data = fetch_payment_data()

    # 6 records total (3 pages x 2 records)
    assert len(data) == 6

    # IDs should now be hashed strings, not plain integers
    assert isinstance(data[0]["id"], str)
    assert data[-1]["status"] == "success"