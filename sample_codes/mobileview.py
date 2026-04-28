from playwright.sync_api import sync_playwright

def sample():
    with sync_playwright() as p:
        #iphone = p.devices["iPhone 13"]

        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://quega-staging.ashontech.in/wallet")
        #context2=browser.new_context()
        #page2=context2.new_page()
    
    
    
if __file__=="__main__":
    sample()