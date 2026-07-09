import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

#Positive Test cases

def test_login(driver):
    driver.get("https://www.guvi.in/")
    driver.find_element(By.XPATH, "//div[@class='⭐️3hk5qd-0 flex gap-5 z-50']//button[@id='login-btn'][1]").click()

    assert driver.current_url == "https://www.guvi.in/sign-in/?sourceUri=http%3A%2F%2Fwww.guvi.in%2F"

def test_email(driver):
    driver.get("https://www.guvi.in/sign-in/")
    username = driver.find_element(By.ID,"email")

    assert username.is_displayed(), "Username field is not visible"
    print("Username field is visible")
    assert username.is_enabled(), "Username field is not enabled"
    print("Username field is enabled")

def test_pass_word(driver):
    driver.get("https://www.guvi.in/sign-in/")
    password = driver.find_element(By.CSS_SELECTOR,"input[type='password']")

    assert password.is_displayed(), "Password field is not visible"
    print("Password field is visible")
    assert password.is_enabled(), "Password field is not enabled"
    print("Password field is enabled")

def test_submit_button(driver):
    driver.get("https://www.guvi.in/sign-in/")
    submit = driver.find_element(By.XPATH,"//a[@id='login-btn']")

    assert submit.is_enabled()
    submit.click()
    print("Submit field is working correctly")

    driver.quit()

# Negative Test Cases
def test_invalid_login(driver):
    driver.get("https://www.guvi.in/sign-in/")
    username = driver.find_element(By.ID,"email")
    username.send_keys("Test@gmail.com")
    password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    password.send_keys("qwerty")
    submit = driver.find_element(By.XPATH, "//a[@id='login-btn']")
    submit.click()

    assert driver.current_url == "https://www.guvi.in/sign-in/?sourceUri=http%3A%2F%2Fwww.guvi.in%2F"
    print("Invalid Credentials")

    driver.quit()


