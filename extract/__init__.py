import requests
import logging
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")
STRIPE_BASE_URL = os.getenv("STRIPE_BASE_URL")

def fetch_payment_data():
    """Fetch dummy payment data for now"""
    try:
        response = requests.get(
            "https://jsonplaceholder.typicode.com/posts"
        )
        response.raise_for_status()
        logger.info("✅ Data extracted successfully")
        return response.json()
    except Exception as e:
        logger.error(f"❌ Extraction failed: {e}")
        return []