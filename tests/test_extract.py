import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from extract import fetch_payment_data

def test_fetch_payment_data_pagination():
    # Run the function (it loops through 3 simulated pages)
    data = fetch_payment_data()
    
    # Prove it works
    assert len(data) == 6  # 3 pages x 2 records each = 6 total
    assert data[0]["id"] == 10
    assert data[-1]["status"] == "success"