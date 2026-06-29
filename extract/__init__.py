import requests
import logging
import os
from dotenv import load_dotenv
from tenacity import retry, stop_after_attempt, wait_fixed

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")
STRIPE_BASE_URL = os.getenv("STRIPE_BASE_URL")

@retry(stop=stop_after_attempt(3), wait=wait_fixed(5))
def fetch_payment_data():
    """Fetch dummy payment data, retrying automatically if it fails"""
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts"
        )
        response.raise_for_status()
        logger.info("✅ Data extracted successfully")
        return response.json()
    except Exception as e:
        logger.error(f"❌ Extraction failed, retrying... ({e})")
        raise  # tenacity needs the error raised again to trigger a retry