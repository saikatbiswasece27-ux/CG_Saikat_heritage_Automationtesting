from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")

    source = wait.until(EC.presence_of_element_located((By.ID, "column-a")))
    target = wait.until(EC.presence_of_element_located((By.ID, "column-b")))

    print("Before:", source.text, "|", target.text)

    # Native drag_and_drop can be unreliable on some sites;
    # using click_and_hold → move → release is more robust
    ActionChains(driver)\
        .click_and_hold(source)\
        .move_to_element(target)\
        .release(target)\
        .perform()

    # Re-locate after DOM update
    print("After:", driver.find_element(By.ID, "column-a").text,
                    "|", driver.find_element(By.ID, "column-b").text)

finally:
    driver.quit()
