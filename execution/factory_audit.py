
import os
import re
import sys
from collections import Counter

# Configuration
PROJECT_ROOT = "c:/Users/srkel/Downloads/Website-builder-antigravity-at-scale"
SRC_DIR = os.path.join(PROJECT_ROOT, "src")
PAGES_DIR = os.path.join(SRC_DIR, "pages")
IMAGES_DIR = os.path.join(PROJECT_ROOT, "public/images")
DIRECTIVE_FILE = os.path.join(PROJECT_ROOT, "directives/manufacturing_pipeline.md")

REQUIRED_LOCATION = "Phillip Island" # This should ideally be dynamic, but hardcoded for this specific build verification.

def check_silos():
    print("\n[AUDIT] Checking Service Silos (Single-Page Ban Violation Check)...")
    service_dir = os.path.join(PAGES_DIR, "services")
    if not os.path.exists(service_dir):
        print("FAIL: 'services' directory missing. Site appears to be single-page only.")
        return False
    
    files = [f for f in os.listdir(service_dir) if f.endswith(".astro")]
    if len(files) < 3:
        print(f"FAIL: Only {len(files)} service silos found. Directives comply at least 3.")
        return False
    
    print(f"PASS: {len(files)} Service Silos detected ({', '.join(files)})")
    return True

def check_assets():
    print("\n[AUDIT] Checking Asset Uniqueness (Zero Repetition Mandate)...")
    expected_assets = ['hero.webp', 'decks.webp', 'handyman.webp', 'rental.webp', 'presale.webp']
    missing = []
    
    for asset in expected_assets:
        if not os.path.exists(os.path.join(IMAGES_DIR, asset)):
            missing.append(asset)
            
    if missing:
        print(f"FAIL: Missing required unique assets: {missing}")
        return False
        
    print("PASS: All critical unique assets verified present.")
    return True

def check_h1_compliance():
    print("\n[AUDIT] Checking H1 Tags for 'Service + Location' Standard...")
    files_to_check = []
    # Add index
    files_to_check.append(os.path.join(PAGES_DIR, "index.astro"))
    # Add services
    service_dir = os.path.join(PAGES_DIR, "services")
    if os.path.exists(service_dir):
        for f in os.listdir(service_dir):
             if f.endswith(".astro"):
                 files_to_check.append(os.path.join(service_dir, f))
    
    failures = []
    for fpath in files_to_check:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Simple regex to capture content inside <h1> tag.
            # Handles multiline H1s
            h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
            if h1_match:
                h1_text = h1_match.group(1)
                # Remove spans and tags
                clean_text = re.sub(r'<[^>]+>', '', h1_text).replace('\n', ' ').strip()
                clean_text = re.sub(r'\s+', ' ', clean_text)
                
                if REQUIRED_LOCATION.lower() not in clean_text.lower():
                    failures.append(f"{os.path.basename(fpath)}: H1 '{clean_text}' missing '{REQUIRED_LOCATION}'")
            else:
                failures.append(f"{os.path.basename(fpath)}: No H1 tag found.")

    if failures:
        for fail in failures:
            print(f"FAIL: {fail}")
        return False
        
    print(f"PASS: All {len(files_to_check)} pages have compliant H1 tags containing '{REQUIRED_LOCATION}'.")
    return True

def check_schema():
    print("\n[AUDIT] Checking SEO Schema Implementation...")
    files_to_check = [os.path.join(PAGES_DIR, "index.astro")]
    service_dir = os.path.join(PAGES_DIR, "services")
    if os.path.exists(service_dir):
        files_to_check.extend([os.path.join(service_dir, f) for f in os.listdir(service_dir) if f.endswith(".astro")])

    failures = []
    for fpath in files_to_check:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
            if "schema =" not in content and "JSON.stringify" not in content:
                failures.append(os.path.basename(fpath))
    
    if failures:
        print(f"FAIL: Schema missing in {failures}")
        return False
    
    print("PASS: Schema detected in all checked pages.")
    return True

def check_sitemap_config():
    print("\n[AUDIT] Checking Sitemap Configuration (Directive Phase 6)...")
    config_path = os.path.join(PROJECT_ROOT, "astro.config.mjs")
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Check if sitemap is imported and used, and NOT commented out
            if "import sitemap" in content and "sitemap()" in content:
                 # Rudimentary check for comments
                 if "// sitemap()" in content or "/*, sitemap() */" in content or "/* sitemap() */" in content:
                     print("FAIL: Sitemap integration is commented out.")
                     return False
                 print("PASS: Sitemap integration appears active.")
                 return True
            else:
                 print("FAIL: Sitemap integration missing from config.")
                 return False
    except Exception as e:
        print(f"FAIL: Could not read astro.config.mjs: {e}")
        return False

def check_trust_signals():
    print("\n[AUDIT] Checking Trust Signals (Directive Phase 5)...")
    index_path = os.path.join(PAGES_DIR, "index.astro")
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read().lower()
            if "insured" in content or "guarantee" in content or "licensed" in content:
                print("PASS: Trust signals ('insured', 'guarantee', etc.) found on Homepage.")
                return True
            else:
                print("FAIL: No Trust Signals found. Directive requires 'Licensed, Insured' etc.")
                return False
    except Exception as e:
        print(f"FAIL: Could not read index.astro: {e}")
        return False

def main():
    print("=== MANUFACTURING DIRECTIVE COMPLIANCE AUDIT (EXPANDED) ===")
    print(f"Target Project: {os.path.basename(PROJECT_ROOT)}")
    
    results = [
        check_silos(),
        check_assets(),
        check_h1_compliance(),
        check_schema(),
        check_sitemap_config(),
        check_trust_signals()
    ]
    
    print("\n================================================")
    if all(results):
        print("RESULT: SUCCESS - PROJECT IS COMPLIANT")
        sys.exit(0)
    else:
        print("RESULT: FAILURE - DIRECTIVE VIOLATIONS DETECTED")
        sys.exit(1)

if __name__ == "__main__":
    main()
