import logging
import requests

def fetch_salesforce_leads():
    logging.info("Extracting CRM data from Salesforce API...")

    # Simulating a Salesforce API response
    crm_data = [
        {"lead_id": "SF-001", "company": "TechCorp", "status": "Closed Won"},
        {"lead_id": "SF-002", "company": "GlobalNet", "status": "Negotiation"}
    ]

    logging.info(f"Pulled {len(crm_data)} Salesforce records.")
    return crm_data