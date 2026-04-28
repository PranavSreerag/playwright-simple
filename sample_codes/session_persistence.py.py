# simple_mobile_session.py - Minimal mobile session persistence

from playwright.sync_api import sync_playwright
from pathlib import Path

# CONFIGURATION - CHANGE THESE!
YOUR_APP_URL = "https://app.questsandgames.com/login"  # CHANGE THIS!

# Mobile viewport size (width x height)
MOBILE_WIDTH = 375   # iPhone SE/12/13/14 width
MOBILE_HEIGHT = 667  # iPhone SE height
# For iPhone 14: width=390, height=844
# For Pixel 5: width=393, height=851

def save_mobile_session():
    """First time: Log in manually in mobile mode"""
    with sync_playwright() as p:
        # Set mobile viewport
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            viewport={"width": MOBILE_WIDTH, "height": MOBILE_HEIGHT},
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
            is_mobile=True,
            has_touch=True
        )
        page = context.new_page()
        
        print(f"📱 Opening {YOUR_APP_URL} in mobile mode ({MOBILE_WIDTH}x{MOBILE_HEIGHT})")
        page.goto(YOUR_APP_URL)
        
        print("\n🔐 LOG IN MANUALLY in the mobile browser window")
        print("   Then press Enter...")
        input()
        
        # Save session
        context.storage_state(path="mobile_session.json")
        print("✅ Mobile session saved!")
        
        browser.close()

def use_mobile_session():
    """Run automation in mobile mode using saved session"""
    with sync_playwright() as p:
        # Load saved session with mobile config
        context = p.chromium.launch_persistent_context(
            user_data_dir="./mobile_profile",
            headless=False,
            viewport={"width": MOBILE_WIDTH, "height": MOBILE_HEIGHT},
            is_mobile=True,
            has_touch=True,
            storage_state="mobile_session.json"
        )
        page = context.new_page()
        
        print(f"📱 Opening {YOUR_APP_URL} in mobile mode")
        page.goto(YOUR_APP_URL)
        
        print("✅ Already logged in and in mobile mode!")
        
        # Your automation here
        page.screenshot(path="mobile_result.png")
        print("📸 Screenshot saved")
        
        input("Press Enter to close...")
        context.close()

# Run the appropriate function
if __name__ == "__main__":
    if not Path("mobile_session.json").exists():
        print("First time setup - you'll need to log in manually")
        save_mobile_session()
    else:
        print("Using saved mobile session")
        use_mobile_session()