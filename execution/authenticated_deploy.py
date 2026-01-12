import os
import requests
import sys
from dotenv import load_dotenv

def main():
    load_dotenv("config.env")
    
    api_url = os.getenv("COOLIFY_API_URL")
    token = os.getenv("COOLIFY_TOKEN")
    
    if len(sys.argv) < 2:
        print("Usage: python authenticated_deploy.py <uuid>")
        return

    app_uuid = sys.argv[1]
    
    url = f"{api_url}/deploy?uuid={app_uuid}&force=true"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    print(f"Triggering authenticated deploy for {app_uuid}...")
    try:
        resp = requests.post(url, headers=headers)
        if resp.status_code == 200:
             print(f"Success: {resp.json()}")
        else:
             print(f"Failed: {resp.status_code} - {resp.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
