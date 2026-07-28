from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.guvi.in/")

current_window = driver.current_url

#navigating from parent to child
live_classes = driver.find_element(By.XPATH,"//div[@id='solutions']/child::p[1]")
live_classes.click()

#navigating from parent to child
courses = driver.find_element(By.XPATH,"(//div[@id='solutions'])[2]/child::p")
courses.click()

#navigating from child to parent
practices = driver.find_element(By.XPATH,"//p[text()='Practice']/parent::div[1]")
practices.click()

#navigating from ancestor
resources = driver.find_element(By.XPATH,"//div[contains(@class,'⭐️f6lmuc-0')]/div[3]/div[4]/div[1]/p")
resources.click()

#navigating from grandparent
our_products = driver.find_element(By.XPATH,"//div[contains(@class,'xl:gap-2.5')]/div[5]/div[1]/p")
our_products.click()

#navigating through preceding-sibling
login = driver.find_element(By.XPATH,"//button[text()='Sign up']/preceding-sibling::button")
login.click()

driver.get(current_window)

#navigating through following-sibling
sign_up = driver.find_element(By.XPATH,"//button[text()='Login']/following-sibling::button")
sign_up.click()











