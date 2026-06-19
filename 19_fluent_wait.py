from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

def get_driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=opts)

driver = get_driver()

try:
    # --- Fluent Wait with a lambda (custom condition) ---
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.find_element(By.TAG_NAME, "button").click()

    fluent_wait = WebDriverWait(
        driver,
        timeout=20,
        poll_frequency=2,                               # check every 2 seconds
        ignored_exceptions=[NoSuchElementException,
                            StaleElementReferenceException]
    )
    element = fluent_wait.until(lambda d: d.find_element(By.ID, "finish"))
    print("Fluent (lambda):", element.text)

    # --- Fluent Wait with expected_conditions ---
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    driver.find_element(By.TAG_NAME, "button").click()

    fluent_ec = WebDriverWait(
        driver,
        timeout=15,
        poll_frequency=1,
        ignored_exceptions=[NoSuchElementException]
    )
    finish = fluent_ec.until(EC.visibility_of_element_located((By.ID, "finish")))
    print("Fluent (EC):", finish.text)

finally:
    driver.quit()
