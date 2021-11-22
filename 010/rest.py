import requests
import json
access_token = ""


response = json.loads(requests.get('https://graph.microsoft.com/v1.0/users/',headers={"Authorization": "Bearer "+access_token}).text)

print(response)