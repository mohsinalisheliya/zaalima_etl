import requests
import os
import logging

def send_slack_alert(message):
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not webhook_url:
        logging.warning("No Slack webhook configured. Skipping alert.")
        return
    
    payload = {"text": f"🚨 *Zaalima ETL Alert:* {message}"}
    requests.post(webhook_url, json=payload)