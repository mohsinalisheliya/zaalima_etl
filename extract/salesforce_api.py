import logging

def fetch_salesforce_leads():
    """
    Simulates extracting customer CRM data from the Salesforce API.
    """
    logging.info("Connecting to Salesforce API...")
    
    # Simulating a JSON response from Salesforce
    mock_crm_data = [
        {"lead_id": "SF-001", "company": "TechCorp", "status": "Closed Won"},
        {"lead_id": "SF-002", "company": "GlobalNet", "status": "Negotiation"}
    ]
    
    logging.info(f"Extraction complete. Pulled {len(mock_crm_data)} CRM records.")
    return mock_crm_data