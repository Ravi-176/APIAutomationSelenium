from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
def test_google_search():
    driver = webdriver.Chrome("https://www.google.com")
    time.sleep(2)
    driver.quit()