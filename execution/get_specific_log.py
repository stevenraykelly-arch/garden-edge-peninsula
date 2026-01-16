import os
import requests
import sys
from dotenv import load_dotenv

load_dotenv("config.env")

api_url = os.getenv("COOLIFY_API_URL").rstrip('/')
token = os.getenv("COOLIFY_TOKEN")
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

dep_uuid = "d044ggsog848wsg0880gw4ws"

print(f"Fetching logs for specific deployment {dep_uuid}...")
resp = requests.get(f"{api_url}/deployments/{dep_uuid}", headers=headers)
print(f"Deployment Info Status: {resp.status_code}")
if resp.status_code == 200:
    print(f"Status: {resp.json().get('status')}")

resp = requests.get(f"{api_url}/deployments/{dep_uuid}/logs", headers=headers)

if resp.status_code == 200:
    print("--- LOGS ---")
    data = resp.json()
    # It might return a list of objects or a string, usually it's a list for logs
    # or sometimes just text depending on version.
    # Let's handle both.
    logs = data
    if isinstance(logs, list):
        # Join lines
        text = "\n".join([l.get('log', '') for l in logs])
        print(text[-3000:])
    elif isinstance(logs, str):
        print(logs[-3000:])
    else:
        print(logs)
    print("--- END ---")
else:
    print(f"Error getting logs: {resp.status_code} {resp.text}")
