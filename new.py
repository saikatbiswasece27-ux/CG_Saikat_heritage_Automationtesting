from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Open browser and navigate to login page
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practicetestautomation.com/practice-test-login/")
# Locate Username textbox using Name locator
time.sleep(5)
driver.find_element(By.NAME, "username").send_keys("student")
# Locate Password textbox using ID locator
time.sleep(5)
driver.find_element(By.ID, "password").send_keys("Password123")
time.sleep(5)
# Locate Login button using CSS Selector and click it
login_button = driver.find_element(By.CSS_SELECTOR, "#submit")
login_button.click()
time.sleep(5)

# Verify login is successful
if "logged-in-successfully" in driver.current_url:
    print("Login Successful")

    #  Print success message displayed on page
    success_message = driver.find_element(By.TAG_NAME, "strong")
    print("Success Message:", success_message.text)
    time.sleep(5)
    #  Use find_element() to locate Logout button
    logout_button = driver.find_element(By.LINK_TEXT, "Log out")
    print("Logout Button Found")
    time.sleep(5)

    #Take screenshot
    driver.save_screenshot("login_success.png")
    print("Screenshot saved successfully")
    time.sleep(5)
    driver.quit()
else:
    print("Login Failed")