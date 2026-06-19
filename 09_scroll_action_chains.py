from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ScrollOrigin moved in Selenium 4.x — handle both import paths
try:
    from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
except ImportError:
    from selenium.webdriver.common.action_chains import ScrollOrigin

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
    # --- Scroll down 500px from current position ---
    driver.get("https://the-internet.herokuapp.com/infinite_scroll")
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    action.scroll_by_amount(0, 500).perform()
    print("Scrolled down 500px")

    # --- Scroll up 300px ---
    action.scroll_by_amount(0, -300).perform()
    print("Scrolled up 300px")

    # --- Scroll to a specific element ---
    driver.get("https://the-internet.herokuapp.com/large")
    element = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[@id='large-table']//tr[30]/td[1]")))
    action.scroll_to_element(element).perform()
    print("Scrolled to element:", element.text)

    # --- Scroll inside a scrollable div ---
    driver.get("https://the-internet.herokuapp.com/infinite_scroll")
    div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "jscroll-inner")))
    origin = ScrollOrigin.from_element(div)
    ActionChains(driver).scroll_from_origin(origin, 0, 400).perform()
    print("Scrolled inside div")

finally:
    driver.quit()
