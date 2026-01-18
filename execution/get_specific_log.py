import os
import requests
from dotenv import load_dotenv
load_dotenv('config.env')
api_url = os.getenv('COOLIFY_API_URL').rstrip('/')
token = os.getenv('COOLIFY_TOKEN')
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
dep_uuid = "jggoc804ckog0cwo0ocggs44"
print(f'Fetching logs for specific deployment {dep_uuid}...')
resp = requests.get(f'{api_url}/deployments/{dep_uuid}', headers=headers)
print(f'Deployment Info Status: {resp.status_code}')
if resp.status_code == 200: print(f'Status: {resp.json().get('status')}')
resp = requests.get(f'{api_url}/deployments/{dep_uuid}/logs', headers=headers)
if resp.status_code == 200: logs = resp.json(); text = '\n'.join([l.get('log', '') for l in logs]) if isinstance(logs, list) else str(logs); print(text[-3000:])
else: print(f'Error getting logs: {resp.status_code}')
