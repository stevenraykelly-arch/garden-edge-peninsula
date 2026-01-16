import os
import requests
import json
from dotenv import load_dotenv

load_dotenv("config.env")
api_url = os.getenv("COOLIFY_API_URL", "").replace('"', '').replace("'", "")
token = os.getenv("COOLIFY_TOKEN", "").replace('"', '').replace("'", "")
headers = {"Authorization": f"Bearer {token}"}

# Fetch recent deployments
url = f"{api_url}/deployments?limit=1&sort=-created_at"
print(f"Fetching latest: {url}")

uuid = None
try:
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        if isinstance(data, dict) and 'deployments' in data:
            if len(data['deployments']) > 0:
                d = data['deployments'][0]
                print(f"Latest Deployment Object: {d.keys()}")
                uuid = d.get('uuid') or d.get('id')
                status = d.get('status')
        elif isinstance(data, list):
             if len(data) > 0:
                 d = data[0]
                 print(f"List Item 0 Keys: {d.keys()}")
                 uuid = d.get('uuid')
                 if not uuid: uuid = d.get('deployment_uuid') # Try alternative
                 status = d.get('status')
                 print(f"Latest Deployment UUID: {uuid} | Status: {status}")
    else:
        print(f"Error listing: {resp.status_code}")
except Exception as e:
    print(f"Error: {e}")

if uuid:
    print(f"Fetching Logs for: {uuid}")
    url = f"{api_url}/deployments/{uuid}"
    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            data = resp.json()
            if 'logs' in data:
                logs = data['logs']
                if isinstance(logs, str):
                    try:
                        logs = json.loads(logs)
                    except:
                        pass
                
                if isinstance(logs, list):
                    with open("debug_log_dump.txt", "w", encoding="utf-8") as f:
                        for l in logs:
                            if 'output' in l:
                                f.write(l['output'] + "\n")
                    print("Logs written to debug_log_dump.txt")
                    
                    # Print last few lines
                    print("--- TAIL LOGS ---")
                    lines = []
                    for l in logs:
                         if 'output' in l:
                             lines.extend(l['output'].replace('\\n', '\n').split('\n'))
                    for line in lines[-20:]:
                        if line.strip(): print(line.strip())
                else:
                    print("Logs content (non-list):")
                    print(str(logs)[-500:])
        else:
            print(f"Error fetching detail: {resp.status_code}")
    except Exception as e:
        print(f"Error fetching logs: {e}")

if uuid:
    print("-" * 30)
    print(f"FINAL STATUS CHECK: {status}")
    print("-" * 30)
