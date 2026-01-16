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

app_uuid = "nwcwk48o0kw0c0gg0ccg4k48"

print(f"Fetching deployments for {app_uuid}...")

# Try getting deployments filtered by app
resp = requests.get(f"{api_url}/deployments", headers=headers, params={"filter[application_uuid]": app_uuid, "sort": "-created_at"})

if resp.status_code != 200:
    print(f"Error: {resp.status_code} {resp.text}")
    sys.exit(1)

data = resp.json()
deployments = []

if isinstance(data, dict):
    deployments = data.get('deployments', [])
elif isinstance(data, list):
    deployments = data

print(f"Found {len(deployments)} deployments.")

if not deployments:
    print("No deployments found.")
    sys.exit(0)

# Get latest
latest = deployments[0]
dep_uuid = latest.get('uuid')
status = latest.get('status')
print(f"Latest Deployment: {dep_uuid} | Status: {status}")

# Get logs
print(f"Fetching logs for {dep_uuid}...")
resp = requests.get(f"{api_url}/deployments/{dep_uuid}/logs", headers=headers)

if resp.status_code == 200:
    print("--- LOGS ---")
    # Print last 30 lines
    lines = resp.text.split('\n')
    print('\n'.join(lines[-50:]))
else:
    print(f"Error getting logs: {resp.status_code}")
