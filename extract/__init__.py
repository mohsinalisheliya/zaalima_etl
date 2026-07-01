import logging
import requests
from tenacity import retry, stop_after_attempt, wait_fixed

@retry(stop=stop_after_attempt(3), wait=wait_fixed(5))
def fetch_payment_data():
    logging.info("Extracting data from API using pagination...")
    all_data = []
    
    # Simulating cursor-based pagination loop
    for page in range(1, 4):
        logging.info(f"Fetching data page {page}...")
        # Simulated API response block
        page_data = [
            {"id": page * 10, "amount": 100 * page, "status": "success"},
            {"id": page * 11, "amount": 150 * page, "status": "success"}
        ]
        all_data.extend(page_data)
        
    logging.info(f"Extraction complete. Pulled {len(all_data)} total records.")
    return all_data