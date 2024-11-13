import os
import requests
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Log the input received
    logger.info(f"FunctionHandler received: {event}")

    payload = {
        "text": f"Issue Created: {event['issue']['html_url']}"
    }

    slack_url = os.getenv("SLACK_URL")
    response = requests.post(slack_url, json=payload, headers={"Content-Type": "application/json"})

    if response.ok:
        return response.text
    else:
        logger.error(f"Request to Slack failed: {response.status_code} - {response.text}")
        return f"Error: {response.status_code}"
