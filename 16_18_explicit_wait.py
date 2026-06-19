from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

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
    # --- visibility_of_element_located ---
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    driver.find_element(By.TAG_NAME, "button").click()
    element = wait.until(EC.visibility_of_element_located((By.ID, "finish")))
    print("visibility_of_element_located →", element.text)

    # --- element_to_be_clickable ---
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    driver.find_element(By.TAG_NAME, "button").click()
    button = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
    print("element_to_be_clickable →", button.text)

    # --- presence_of_element_located ---
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    driver.find_element(By.TAG_NAME, "button").click()
    elem = wait.until(EC.presence_of_element_located((By.ID, "finish")))
    print("presence_of_element_located →", elem.text)

    # --- text_to_be_present_in_element ---
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    driver.find_element(By.TAG_NAME, "button").click()
    wait.until(EC.text_to_be_present_in_element((By.ID, "finish"), "Hello World!"))
    print("text_to_be_present_in_element → matched!")

    # --- invisibility_of_element_located ---
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    driver.find_element(By.TAG_NAME, "button").click()
    wait.until(EC.invisibility_of_element_located((By.ID, "loading")))
    print("invisibility_of_element_located → loading bar gone!")

    # --- title_contains ---
    driver.get("https://the-internet.herokuapp.com")
    wait.until(EC.title_contains("The Internet"))
    print("title_contains →", driver.title)

    # --- alert_is_present ---
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    alert = wait.until(EC.alert_is_present())
    print("alert_is_present →", alert.text)
    alert.accept()

    # --- TimeoutException handling ---
    try:
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.ID, "non_existent")))
    except TimeoutException:
        print("TimeoutException caught as expected!")

finally:
    driver.quit()
