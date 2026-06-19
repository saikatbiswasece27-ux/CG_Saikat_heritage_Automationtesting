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
    # --- Get page title and URL via JS ---
    driver.get("https://the-internet.herokuapp.com")
    print("Title (JS):", driver.execute_script("return document.title;"))
    print("URL (JS)  :", driver.execute_script("return document.URL;"))

    # --- Scroll to element using JS ---
    driver.get("https://the-internet.herokuapp.com/large")
    element = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[@id='large-table']//tr[30]/td[1]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    print("Scrolled to element:", element.text)

    # --- Highlight element with JS ---
    driver.get("https://the-internet.herokuapp.com")
    heading = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
    driver.execute_script("arguments[0].style.border='3px solid red'", heading)
    driver.execute_script("arguments[0].style.backgroundColor='yellow'", heading)
    print("Highlighted heading:", heading.text)

    # --- Click a hidden/obscured element via JS ---
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")
    checkbox = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//input[@type='checkbox']")))
    driver.execute_script("arguments[0].click();", checkbox)
    print("Checkbox checked:", checkbox.is_selected())

    # --- Set input value directly via JS (bypasses normal typing) ---
    driver.get("https://demoqa.com/text-box")
    name_input = wait.until(EC.presence_of_element_located((By.ID, "userName")))
    driver.execute_script("arguments[0].value = 'Set via JavaScript!';", name_input)
    print("Input value:", name_input.get_attribute("value"))

finally:
    driver.quit()
