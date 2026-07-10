import requests
import os
import logging

# Slack Webhook Alert Module
# Sends real-time alerts to the Zaalima team Slack channel on pipeline failure

def send_slack_alert(message):
    """Send a Slack alert message when the ETL pipeline fails."""
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        logging.warning("No Slack webhook configured. Skipping alert.")
        return
    
    payload = {"text": f"🚨 *Zaalima ETL Alert:* {message}"}
    response = requests.post(webhook_url, json=payload)
    logging.info(f"Slack alert sent. Status code: {response.status_code}")