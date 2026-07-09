import pytest

from extract.salesforce_api import fetch_salesforce_leads


class TestFetchSalesforceLeads:
    """Tests for fetch_salesforce_leads()"""

    def test_returns_list(self):
        """Function should return a list of records."""
        result = fetch_salesforce_leads()
        assert isinstance(result, list)

    def test_not_empty(self):
        """Simulated/fetched data should contain at least one record."""
        result = fetch_salesforce_leads()
        assert len(result) > 0

    def test_records_are_dicts(self):
        """Each record in the list should be a dictionary."""
        result = fetch_salesforce_leads()
        for record in result:
            assert isinstance(record, dict)

    def test_has_expected_keys(self):
        """Each record should contain the core lead fields the pipeline depends on."""
        result = fetch_salesforce_leads()
        expected_keys = {"lead_id", "company", "status"}
        for record in result:
            missing = expected_keys - set(record.keys())
            assert not missing, f"Record missing expected keys: {missing} -> {record}"

    def test_lead_id_not_empty(self):
        """Every record must have a non-empty lead_id, since it's used as a key downstream."""
        result = fetch_salesforce_leads()
        for record in result:
            assert record.get("lead_id"), f"Empty lead_id in record: {record}"

    def test_no_duplicate_lead_ids(self):
        """Lead IDs should be unique within a single fetch."""
        result = fetch_salesforce_leads()
        lead_ids = [record["lead_id"] for record in result]
        assert len(lead_ids) == len(set(lead_ids)), "Duplicate lead_id values found"

    def test_status_is_known_value(self):
        """Status field should be one of the expected CRM pipeline stages."""
        result = fetch_salesforce_leads()
        # Extend this set as new statuses show up in real Salesforce data
        known_statuses = {"Closed Won", "Closed Lost", "Negotiation", "Prospecting", "Qualified"}
        for record in result:
            assert record.get("status") in known_statuses, (
                f"Unexpected status '{record.get('status')}' in record: {record}"
            )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])