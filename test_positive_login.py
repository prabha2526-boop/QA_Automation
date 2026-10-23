from playwright.sync_api import sync_playwright, expect

def test_successful_login():
    with sync_playwright() as p:
        # 1. Launch real system Chrome (visible mode)
        browser = p.chromium.launch(channel="chrome", headless=False)
        page = browser.new_page()
        
        # 2. Go to SauceDemo website
        page.goto("https://www.saucedemo.com/")
        
        # 3. Enter valid username and password
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        
        # 4. Click the login button
        page.click("#login-button")
        
        # 5. Verify that we successfully arrived at the inventory page
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        
        # 🕒 PAUSE FOR 5 SECONDS SO YOU CAN WATCH!
        page.wait_for_timeout(5000)
        
        # 6. Close the browser session
        browser.close()

test_successful_login()