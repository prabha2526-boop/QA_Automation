from playwright.sync_api import sync_playwright

def test_shopping_cart():
    with sync_playwright() as p:
        # 1. Launch Chrome browser
        browser = p.chromium.launch(headless=False, channel="chrome")
        page = browser.new_page()
        
        # 2. Navigate to store
        page.goto("https://www.saucedemo.com/")
        
        # 3. Login actions
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        
        # 4. NEW ACTION: Click the Shopping Cart icon using its CSS class selector
        page.click(".shopping_cart_link")
        
        print("Success: Logged in and clicked the shopping cart automatically!")
        page.wait_for_timeout(2000)
        
        # 5. Close browser
        browser.close()

# Run the test function
test_shopping_cart()
