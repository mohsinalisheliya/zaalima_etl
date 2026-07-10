import logging
import hashlib
from tenacity import retry, stop_after_attempt, wait_fixed

def mask_id(value):
    """Masks sensitive IDs using SHA-256 hashing for privacy compliance."""
    return hashlib.sha256(str(value).encode()).hexdigest()[:12]

@retry(stop=stop_after_attempt(3), wait=wait_fixed(5))
def fetch_payment_data():
    logging.info("Extracting data from API using pagination...")
    all_data = []

    # Simulated API headers check
    rate_limit_remaining = 15
    if rate_limit_remaining < 20:
        logging.critical(f"API Rate Limit Warning! Only {rate_limit_remaining} calls left.")

    # Simulating cursor-based pagination loop
    for page in range(1, 4):
        logging.info(f"Fetching data page {page}...")
        page_data = [
            {"id": mask_id(page * 10), "amount": 100 * page, "status": "success"},
            {"id": mask_id(page * 11), "amount": 150 * page, "status": "success"}
        ]
        all_data.extend(page_data)

    logging.info(f"Extraction complete. Pulled {len(all_data)} total records.")
    return all_data