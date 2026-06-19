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
action = ActionChains(driver)
wait = WebDriverWait(driver, 10)

try:
    # --- Mouse Hover ---
    driver.get("https://the-internet.herokuapp.com/hovers")
    image = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "figure")))
    action.move_to_element(image).perform()
    # Verify hover caption appears
    caption = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "figcaption")))
    print("Hover caption:", caption.text)

    # --- Right Click (Context Click) ---
    driver.get("https://the-internet.herokuapp.com/context_menu")
    box = wait.until(EC.element_to_be_clickable((By.ID, "hot-spot")))
    action.context_click(box).perform()
    try:
        alert = wait.until(EC.alert_is_present())
        print("Alert text:", alert.text)
        alert.accept()
    except Exception:
        print("No alert appeared")

    # --- Double Click ---
    driver.get("https://demoqa.com/buttons")
    button = wait.until(EC.element_to_be_clickable((By.ID, "doubleClickBtn")))
    action.double_click(button).perform()
    msg = wait.until(EC.visibility_of_element_located((By.ID, "doubleClickMessage")))
    print("Double click:", msg.text)

finally:
    driver.quit()
