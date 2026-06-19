from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    # contains() — match button whose text contains 'Remove'
    btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(), 'Remove')]")))
    print("contains() →", btn.text)

    # starts-with() — match input whose type starts with 'check'
    checkbox = driver.find_element(By.XPATH, "//input[starts-with(@type, 'check')]")
    print("starts-with() →", checkbox.get_attribute("type"))

    # Relative XPath — button inside a specific form
    form_btn = driver.find_element(By.XPATH, "//form[@id='checkbox-example']//button")
    print("Relative XPath →", form_btn.text)

    # Click the Remove button and wait for the confirmation message
    btn.click()
    msg = wait.until(EC.visibility_of_element_located((By.ID, "message")))
    print("Message:", msg.text)

finally:
    driver.quit()
