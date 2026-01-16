import os
import requests
import sys
from dotenv import load_dotenv
import time

load_dotenv("config.env")

api_url = os.getenv("COOLIFY_API_URL").rstrip('/')
token = os.getenv("COOLIFY_TOKEN")
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

app_uuid = "nwcwk48o0kw0c0gg0ccg4k48"
webhook_url = f"{api_url}/deploy?uuid={app_uuid}&force=true"

print(f"Triggering deployment for {app_uuid}...")
resp = requests.get(webhook_url, headers=headers)
print(f"Trigger response: {resp.status_code} {resp.text}")

print("Waiting 10 seconds for deployment to register...")
time.sleep(10)

# listing deployments again
resp = requests.get(f"{api_url}/deployments", headers=headers, params={"filter[application_uuid]": app_uuid, "sort": "-created_at"})
if resp.status_code == 200:
    data = resp.json()
    deployments = data.get('deployments', []) if isinstance(data, dict) else data
    print(f"Found {len(deployments)} deployments.")
    if deployments:
        print(f"Latest: {deployments[0].get('uuid')} status: {deployments[0].get('status')}")
