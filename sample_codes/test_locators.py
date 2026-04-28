from playwright.sync_api import sync_playwright

def locator_examples():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        
        page =browser.new_page()
        
        page.goto("https://www.simplilearn.com/playwright-with-java-skillup")
        
        print("\n=== LOCATOR EXAMPLES ===\n")
        
        #Find by Text
        
        #text_element=page.get_by_text("span")
        #print(f"Found: {text_element.text_content()}")
        
        #Find by css selector
        
        '''heading=page.locator("body > div:nth-child(11) > div:nth-child(1) > header:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)")
        print(f"Heading text: {heading.text_content()}")
        
        heading.click()'''
        
        #find multiple elements
        
        paragraphs=page.locator("p")
        print(f"Number of paragraphs:{paragraphs.count()}")
        
        #check if the elemnet exists
        exists=page.locator("h1").count()>0
        print(f"Does h1 exists ? :{exists}")
        
        
        
if __name__=="__main__":
    locator_examples()