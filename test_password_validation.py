from playwright.sync_api import sync_playwright, expect

def test_invalid_password_shows_error():
    with sync_playwright() as p:
        # Launch real system Chrome instead of downloading the bundled build
        browser = p.chromium.launch(channel="chrome", headless=False)
        page = browser.new_page()
        
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "1234567")
        page.click("#login-button")
        
        expect(page.locator("[data-test='error']")).to_be_visible()
        browser.close()