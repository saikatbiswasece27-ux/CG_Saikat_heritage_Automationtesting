from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=opts)

driver = get_driver()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://demoqa.com/text-box")

    name = wait.until(EC.element_to_be_clickable((By.ID, "userName")))

    # ENTER key
    name.send_keys("John Doe")
    name.send_keys(Keys.ENTER)

    # TAB to move focus to next field
    name.clear()
    name.send_keys("Jane Smith")
    name.send_keys(Keys.TAB)
    email_field = wait.until(EC.element_to_be_clickable((By.ID, "userEmail")))
    email_field.send_keys("jane@example.com")

    # CTRL+A to select all, then overwrite
    name.click()
    name.send_keys(Keys.CONTROL, 'a')
    name.send_keys("Replaced Text")
    print("Name field value:", name.get_attribute("value"))

    # CTRL+C then CTRL+V to copy-paste
    addr = wait.until(EC.element_to_be_clickable((By.ID, "currentAddress")))
    addr.send_keys("123 Main Street")
    addr.send_keys(Keys.CONTROL, 'a')
    addr.send_keys(Keys.CONTROL, 'c')
    perm = driver.find_element(By.ID, "permanentAddress")
    perm.click()
    perm.send_keys(Keys.CONTROL, 'v')
    print("Permanent address value:", perm.get_attribute("value"))

    # BACKSPACE to delete last character
    email_field.click()
    email_field.send_keys(Keys.BACK_SPACE)
    print("Email after backspace:", email_field.get_attribute("value"))

finally:
    driver.quit()
