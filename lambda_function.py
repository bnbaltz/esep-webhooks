import json
import os
import requests

def lambda_handler(input, context):
    
    # Exit of "issue" key is not found in input
    if 'issue' not in input:
        return json.dumps({"KeyError":"Key \'issue\' not found!"})
    
    url = os.getenv("SLACK_URL")
    content = { "text": input['issue']['url'] }
    
    response = requests.post(url=url, json=content)

    return response.text