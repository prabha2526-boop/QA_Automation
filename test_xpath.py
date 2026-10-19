from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_wikipedia_xpath():
    driver = webdriver.Chrome()
    driver.get("https://www.wikipedia.org")

    # Locate the search input using explicit XPath instead of By.NAME
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='searchInput']"))
    )
    search_input.send_keys("Software Testing")

    # Locate the search button using text-contains XPath and click
    search_button = driver.find_element(By.XPATH, "//button[contains(@class, 'pure-button')]")
    search_button.click()

    # Wait for page title to update
    WebDriverWait(driver, 10).until(EC.title_contains("Software testing"))

    assert "Software testing" in driver.title
    driver.quit()
    