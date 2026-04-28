from playwright.sync_api import sync_playwright

def sample_one():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False,slow_mo=500)
        page=browser.new_page()
        page.goto("https://discord.com/login?redirect_to=%2Foauth2%2Fauthorize%3Fclient_id%3D1456151388399734886%26redirect_uri%3Dhttps%253A%252F%252Fquega-staging.ashontech.in%252Fwebapp%252Fauth%252Fdiscord%252Fcallback%26response_type%3Dcode%26scope%3Didentify%2Bemail%26state%3DeyJ1c2VySWQiOiJiNDJhZTUwZC01OTY1LTQzN2MtOTllZC0wYTNjZTAxM2MzZjgifQ")
        
        
        
        
        
        
        
if __file__=="__main__":
    sample_one()