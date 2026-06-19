from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open OrangeHRM
driver.get("https://opensource-demo.orangehrmlive.com/")

time.sleep(3)

# Login
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(3)

# Verify Dashboard
print("Page Title:", driver.title)

# Navigate to PIM
driver.find_element(By.XPATH, "//span[text()='PIM']").click()

time.sleep(3)

# Add Employee
driver.find_element(By.XPATH, "//a[text()='Add Employee']").click()

time.sleep(3)

driver.find_element(By.NAME, "firstName").send_keys("Saikat")
driver.find_element(By.NAME, "lastName").send_keys("Biswas")

# Save Employee
driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(5)

# Go to Employee List
driver.find_element(By.XPATH, "//a[text()='Employee List']").click()

time.sleep(3)

# Search Employee
search_box = driver.find_element(
    By.XPATH,
    "(//input[@placeholder='Type for hints...'])[1]"
)

search_box.send_keys("Saikat")

time.sleep(2)

driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(5)

# Verify Employee Exists
if "Saikat" in driver.page_source:
    print("Employee Found")
else:
    print("Employee Not Found")

# Take Screenshot
driver.save_screenshot("employee_search.png")
print("Screenshot Saved")

# Logout
driver.find_element(By.XPATH, "//p[@class='oxd-userdropdown-name']").click()

time.sleep(2)

driver.find_element(By.XPATH, "//a[text()='Logout']").click()

time.sleep(3)

# Close Browser
driver.quit()