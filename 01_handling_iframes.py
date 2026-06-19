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
    driver.get("https://the-internet.herokuapp.com/iframe")

    # Wait for the iframe to be available, then switch into it
    iframe = wait.until(EC.presence_of_element_located((By.ID, "mce_0_ifr")))
    driver.switch_to.frame(iframe)

    # Clear existing text and type new content
    box = wait.until(EC.presence_of_element_located((By.ID, "tinymce")))
    box.clear()
    box.send_keys("Hello Selenium")
    print("Typed into iframe successfully")

    # Switch back to main page
    driver.switch_to.default_content()
    print("Switched back to main content")

finally:
    driver.quit()
