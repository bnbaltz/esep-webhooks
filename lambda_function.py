import json
import os
import requests

def lambda_handler(input, context):
    url = os.getenv("SLACK_URL")
    content = { "text": input['issue']['url'] }
    response = requests.post(url=url, json=content)
    return response.text
