from selenium import webdriver

# Open Google Chrome browser
driver = webdriver.Chrome()

# Navigate to Google homepage
driver.get("https://www.google.com")

# Print page title in terminal
print("Page Title is:", driver.title)

# Close browser
driver.quit()