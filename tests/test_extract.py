import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from extract import fetch_payment_data
from extract import mask_id

def test_fetch_payment_data_pagination():
    """Test that pagination pulls 6 records across 3 pages."""
    data = fetch_payment_data()
    assert len(data) == 6, "Expected 6 records from 3 pages"

def test_pii_masking_applied():
    """Test that IDs are masked strings, not plain integers."""
    data = fetch_payment_data()
    for record in data:
        assert isinstance(record["id"], str), "ID should be a masked string"
        assert len(record["id"]) == 12, "Masked ID should be 12 characters"

def test_all_records_successful():
    """Test that all extracted records have success status."""
    data = fetch_payment_data()
    for record in data:
        assert record["status"] == "success", f"Expected success but got {record['status']}"

def test_amounts_are_positive():
    """Test that all payment amounts are positive numbers."""
    data = fetch_payment_data()
    for record in data:
        assert record["amount"] > 0, "Amount must be positive"

def test_mask_id_function():
    """Test that mask_id returns consistent 12-char hashes."""
    result = mask_id(12345)
    assert isinstance(result, str)
    assert len(result) == 12
    assert result == mask_id(12345)  # Same input = same hash always