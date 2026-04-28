from playwright.sync_api import sync_playwright

def sample():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False,slow_mo=500)
        page=browser.new_page()
        page.goto("https://www.udemy.com/course/introduction-to-devops-habits-practices-and-pipelines/")
        
        
        
if __name__=="__main__":
    sample()        