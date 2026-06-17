from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Implicit Wait
driver.implicitly_wait(10)

driver.get("https://practicetestautomation.com/practice-test-login/")

# Enter Username
driver.find_element(By.ID, "username").send_keys("student")

# Enter Password
driver.find_element(By.ID, "password").send_keys("Password123")

# Click Login
driver.find_element(By.ID, "submit").click()

print("Login Successful")

time.sleep(3)
driver.quit()