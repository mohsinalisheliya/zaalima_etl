import requests
import logging
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Read keys from .env file
STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")
STRIPE_BASE_URL = os.getenv("STRIPE_BASE_URL")

def fetch_payment_data():
    """Fetch real payment data from Stripe API"""
    try:
        response = requests.get(
            f"{STRIPE_BASE_URL}/charges",
            auth=(STRIPE_API_KEY, "")  # Stripe uses API key as username
        )
        response.raise_for_status()
        data = response.json()
        logger.info(f"✅ Data extracted successfully - {len(data['data'])} records found")
        return data['data']
    except Exception as e:
        logger.error(f"❌ Extraction failed: {e}")
        return []