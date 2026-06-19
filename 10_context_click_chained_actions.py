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
    # --- Context Click (right-click) ---
    driver.get("https://the-internet.herokuapp.com/context_menu")
    box = wait.until(EC.element_to_be_clickable((By.ID, "hot-spot")))
    ActionChains(driver).context_click(box).perform()
    try:
        alert = wait.until(EC.alert_is_present())
        print("Alert:", alert.text)
        alert.accept()
    except Exception:
        print("No alert appeared")

    # --- Chained: move to element + click ---
    driver.get("https://demoqa.com/buttons")
    click_btn = wait.until(EC.element_to_be_clickable((By.ID, "clickMeBtn")))
    ActionChains(driver).move_to_element(click_btn).click().perform()
    msg = wait.until(EC.visibility_of_element_located((By.ID, "dynamicClickMessage")))
    print("Single click:", msg.text)

    # --- Chained: move to element + double click ---
    driver.get("https://demoqa.com/buttons")
    dbl_btn = wait.until(EC.element_to_be_clickable((By.ID, "doubleClickBtn")))
    ActionChains(driver).move_to_element(dbl_btn).double_click(dbl_btn).perform()
    msg = wait.until(EC.visibility_of_element_located((By.ID, "doubleClickMessage")))
    print("Double click:", msg.text)

    # --- Chained: move to element + right click ---
    driver.get("https://demoqa.com/buttons")
    right_btn = wait.until(EC.element_to_be_clickable((By.ID, "rightClickBtn")))
    ActionChains(driver).move_to_element(right_btn).context_click(right_btn).perform()
    msg = wait.until(EC.visibility_of_element_located((By.ID, "rightClickMessage")))
    print("Right click:", msg.text)

finally:
    driver.quit()
