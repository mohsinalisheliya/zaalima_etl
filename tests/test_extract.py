import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from extract import fetch_payment_data

def test_fetch_payment_data_pagination():
    data = fetch_payment_data()
    assert len(data) == 6
    assert data[0]["id"] == 10
    assert data[-1]["status"] == "success"