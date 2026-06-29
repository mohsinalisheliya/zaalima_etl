import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from unittest.mock import patch
from extract import fetch_payment_data

@patch('extract.requests.get')
def test_fetch_payment_data_success(mock_get):
    # 1. Fake a successful API response
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{"id": 999, "title": "dummy_payment"}]
    # 2. Run your function (it will hit the fake mock instead of the real internet)
    data = fetch_payment_data()
    # 3. Prove it works
    assert len(data) == 1
    assert data[0]["id"] == 999