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
    driver.get("https://the-internet.herokuapp.com/nested_frames")

    # Switch into top frame, then each child frame
    driver.switch_to.frame("frame-top")

    driver.switch_to.frame("frame-left")
    print("LEFT:", driver.find_element(By.TAG_NAME, "body").text)

    driver.switch_to.parent_frame()
    driver.switch_to.frame("frame-middle")
    print("MIDDLE:", driver.find_element(By.TAG_NAME, "body").text)

    driver.switch_to.parent_frame()
    driver.switch_to.frame("frame-right")
    print("RIGHT:", driver.find_element(By.TAG_NAME, "body").text)

    # Go back to top-level to access bottom frame
    driver.switch_to.default_content()
    driver.switch_to.frame("frame-bottom")
    print("BOTTOM:", driver.find_element(By.TAG_NAME, "body").text)

    driver.switch_to.default_content()
    print("All nested frames read successfully")

finally:
    driver.quit()
