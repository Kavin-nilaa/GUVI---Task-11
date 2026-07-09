from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless") 

driver = webdriver.Chrome(options=options)

driver.get("https://www.guvi.in/")
driver.maximize_window()

driver.find_element(By.XPATH, "//div[@class='⭐️3hk5qd-0 flex gap-5 z-50']//button[@id='login-btn'][1]").click()

driver.find_element(By.XPATH,"//input[@id='email']").send_keys("")

driver.find_element(By.XPATH,"//input[@type='password']").send_keys("")

driver.find_element(By.XPATH,"//a[@id='login-btn']").click()

driver.quit()
