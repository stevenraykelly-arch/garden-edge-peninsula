import os
import sys
import argparse
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Constants
SCOPES = [
    'https://www.googleapis.com/auth/webmasters',
    'https://www.googleapis.com/auth/siteverification'
]
SERVICE_ACCOUNT_FILE = 'execution/service_account.json'
SITE_URL = 'https://landscaperspakenham.com.au/'
SITEMAP_URL = 'https://landscaperspakenham.com.au/sitemap.xml'

def get_service(api_name, api_version):
    """Authenticates and returns the specified Google API service."""
    if not os.path.exists(SERVICE_ACCOUNT_FILE):
        print(f"❌ Error: Service account file not found at {SERVICE_ACCOUNT_FILE}")
        sys.exit(1)

    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build(api_name, api_version, credentials=creds)

def add_site(site_url):
    """Adds the site to Google Search Console."""
    print(f"Adding site: {site_url}...")
    service = get_service('searchconsole', 'v1')
    try:
        service.sites().add(siteUrl=site_url).execute()
        print(f"✅ Site added successfully.")
    except HttpError as e:
        print(f"⚠️ Error adding site: {e}")

def get_verification_token(site_url):
    """Retrieves the verification token using Site Verification API."""
    print(f"Retrieving verification token for {site_url}...")
    service = get_service('siteVerification', 'v1')
    try:
        request = {
            "verificationMethod": "META",
            "site": {
                "identifier": site_url,
                "type": "SITE"
            }
        }
        response = service.webResource().getToken(body=request).execute()
        token = response.get('token')
        print(f"✅ Token received: {token}")
        return token
    except HttpError as e:
        print(f"⚠️ Error getting token: {e}")
        return None

def submit_sitemap(site_url, sitemap_url):
    """Submits the sitemap to Google Search Console."""
    print(f"Submitting sitemap: {sitemap_url}...")
    service = get_service('searchconsole', 'v1')
    try:
        service.sitemaps().submit(siteUrl=site_url, feedpath=sitemap_url).execute()
        print(f"✅ Sitemap submitted successfully.")
    except HttpError as e:
        print(f"⚠️ Error submitting sitemap: {e}")

def main():
    parser = argparse.ArgumentParser(description='Automate Google Search Console Indexing')
    parser.add_argument('--action', choices=['all', 'add', 'verify', 'sitemap'], default='all', help='Action to perform')
    args = parser.parse_args()

    # Note: 'add' in GSC often requires verification first or simultaneously.
    # We'll try to get the token first.
    
    if args.action in ['all', 'verify']:
        token = get_verification_token(SITE_URL)
        if token:
            print("\n📋 ACTION REQUIRED: Add this meta tag to your src/layouts/Layout.astro file's <head> section:")
            print(f"   {token}")
            
    if args.action in ['all', 'add']:
        add_site(SITE_URL)

    if args.action in ['all', 'sitemap']:
        submit_sitemap(SITE_URL, SITEMAP_URL)

if __name__ == '__main__':
    main()
