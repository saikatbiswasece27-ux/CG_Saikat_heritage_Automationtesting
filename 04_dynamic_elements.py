from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

def get_driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=opts)

driver = get_driver()
wait = WebDriverWait(driver, 10)
LOCATOR = (By.XPATH, "(//div[@class='large-10 columns'])[1]")

try:
    driver.get("https://the-internet.herokuapp.com/dynamic_content")

    # Read content before refresh
    element = wait.until(EC.presence_of_element_located(LOCATOR))
    print("Before refresh:", element.text[:80])

    # Refresh the page — element reference becomes stale
    driver.refresh()

    # Intentionally demonstrate StaleElementReferenceException
    try:
        print(element.text)  # This WILL raise StaleElementReferenceException
    except StaleElementReferenceException:
        print("StaleElementReferenceException caught! (expected after refresh)")

    # Re-locate the element after refresh
    element = wait.until(EC.presence_of_element_located(LOCATOR))
    print("After refresh:", element.text[:80])

finally:
    driver.quit()
