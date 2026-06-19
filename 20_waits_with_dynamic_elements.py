from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as FluentWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

def get_driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=opts)

driver = get_driver()
wait = WebDriverWait(driver, 15)

try:
    # --- Pattern 1: Click → wait for loading → read result ---
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    wait.until(EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()
    wait.until(EC.invisibility_of_element_located((By.ID, "loading")))
    finish = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
    print("Pattern 1 (click→wait→read):", finish.text)

    # --- Pattern 2: Enable input → type into it ---
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")
    driver.find_element(By.XPATH, "//form[@id='input-example']//button").click()
    input_field = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//form[@id='input-example']//input")))
    input_field.send_keys("Dynamic input works!")
    msg = wait.until(EC.visibility_of_element_located((By.ID, "message")))
    print("Pattern 2 (enable→type):", msg.text)

    # --- Pattern 3: Remove element → confirm gone → add it back ---
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")
    remove_btn = driver.find_element(By.XPATH, "//form[@id='checkbox-example']//button")
    remove_btn.click()
    wait.until(EC.invisibility_of_element_located((By.XPATH, "//input[@type='checkbox']")))
    msg = wait.until(EC.visibility_of_element_located((By.ID, "message")))
    print("Pattern 3 (removed):", msg.text)

    # Add it back by clicking the button again (now labelled "Add")
    driver.find_element(By.XPATH, "//form[@id='checkbox-example']//button").click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox']")))
    msg = wait.until(EC.visibility_of_element_located((By.ID, "message")))
    print("Pattern 3 (added back):", msg.text)

    # --- Pattern 4: Fluent wait for a slow-loading element ---
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.find_element(By.TAG_NAME, "button").click()

    fluent = FluentWait(
        driver,
        timeout=20,
        poll_frequency=2,
        ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]
    )
    result = fluent.until(lambda d: d.find_element(By.ID, "finish"))
    print("Pattern 4 (fluent wait):", result.text)

finally:
    driver.quit()
