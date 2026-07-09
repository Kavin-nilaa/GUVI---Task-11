import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def setup_driver():
   driver = webdriver.Chrome()
   driver.maximize_window()
   driver.get("https://www.saucedemo.com/")
   return driver

def test_title(setup_driver): #test case for title of the webpage
   assert setup_driver.title == "Swag Labs"

def test_url(setup_driver): #negative test case for url of the homepage
   assert setup_driver.current_url =="https://www.saucedemo1.com/"

def test_current_url(setup_driver): # Positive test case to get the url after login
   # code to log in into the url
   setup_driver.find_element(By.ID, "user-name").send_keys("standard_user")

   setup_driver.find_element(By.ID, "password").send_keys("secret_sauce")

   setup_driver.find_element(By.ID, "login-button").click()

   assert setup_driver.current_url=="https://www.saucedemo.com/inventory.html"







