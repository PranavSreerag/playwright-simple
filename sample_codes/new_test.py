from playwright.sync_api import sync_playwright

def num_one_test():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False,slow_mo=500)
        page=browser.new_page()
        page.goto("https://the-internet.herokuapp.com/login")
        usernm_field=page.get_by_label("username")
        passwd_field=page.get_by_label("password")
        
        #usernm_field.fill("Pranav")
        #passwd_field.fill("Pavikutty")
        passwd_field.type("pavikutty",delay=100)
        usernm_field.type("PranavSreerag",delay=100)
        
        
        
if __name__=="__main__":
    num_one_test()
        