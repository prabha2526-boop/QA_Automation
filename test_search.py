from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_wikipedia_search():
    driver = webdriver.Chrome()
    driver.get("https://www.wikipedia.org")

    search_box = driver.find_element(By.NAME, "search")
    search_box.send_keys("Selenium Testing")
    search_box.send_keys(Keys.RETURN)

    time.sleep(4)

    assert "Selenium Testing" in driver.title
    driver.quit()
    