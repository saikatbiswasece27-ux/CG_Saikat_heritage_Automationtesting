from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://practicetestautomation.com/practice-test-login/")

# Create Explicit Wait object
wait = WebDriverWait(driver, 10)

# Wait for Username field
username = wait.until(
    EC.visibility_of_element_located((By.ID, "username"))
)

username.send_keys("student")

# Wait for Password field
password = wait.until(
    EC.visibility_of_element_located((By.ID, "password"))
)

password.send_keys("Password123")

# Wait for Login button to be clickable
login_button = wait.until(
    EC.element_to_be_clickable((By.ID, "submit"))
)

login_button.click()

print("Login Successful")

time.sleep(3)
driver.quit()