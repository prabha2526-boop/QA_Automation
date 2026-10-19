from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_wikipedia_english_link():
    driver = webdriver.Chrome()
    driver.get("https://www.wikipedia.org")

    # 1. Click English link
    english_link = driver.find_element(By.ID, "js-link-box-en")
    english_link.click()

    # 2. Smart Wait: Pause ONLY until the page title contains 'Wikipedia' (max 10 seconds)
    WebDriverWait(driver, 10).until(EC.title_contains("Wikipedia"))

    # 3. Assert page title
    assert "Wikipedia, the free encyclopedia" in driver.title

    driver.quit()