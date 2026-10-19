from playwright.sync_api import sync_playwright

def test_search1_product():
    with sync_playwright() as p:
        # 1. Launch Chrome browser on your Mac
        browser = p.chromium.launch(headless=False, channel="chrome")
        page = browser.new_page()
        
        # 2. Navigate to Staging Store Login
        page.goto("https://www.saucedemo.com/")
        
        # 3. Perform Login Actions
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        
        # 4. Verify we reached Inventory Page
        print("Logged in successfully!")
        page.wait_for_timeout(2000)
        
        # 5. Close browser
        browser.close()

# Run our test function
test_search1_product()