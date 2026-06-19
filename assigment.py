from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

# MODULE 1 - LOGIN VERIFICATION

driver.get("https://the-internet.herokuapp.com/login")
time.sleep(2)

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

print(driver.find_element(By.ID, "flash").text)

driver.save_screenshot("login.png")

# MODULE 2 - DROPDOWN HANDLING

driver.get("https://the-internet.herokuapp.com/dropdown")
time.sleep(2)

dropdown = Select(driver.find_element(By.ID, "dropdown"))

dropdown.select_by_index(1)
time.sleep(1)

dropdown.select_by_value("2")
time.sleep(1)

dropdown.select_by_visible_text("Option 1")
time.sleep(1)

# MODULE 3 - CHECKBOX VALIDATION

driver.get("https://the-internet.herokuapp.com/checkboxes")
time.sleep(2)

checkbox = driver.find_elements(By.TAG_NAME, "input")

if not checkbox[0].is_selected():
    checkbox[0].click()

print("Checkbox Selected:", checkbox[0].is_selected())

# MODULE 4 - JAVASCRIPT ALERTS

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(2)

driver.find_element(
    By.XPATH,
    "//button[text()='Click for JS Alert']"
).click()

alert = WebDriverWait(driver, 10).until(
    EC.alert_is_present()
)

print("Alert Text:", alert.text)

alert.accept()

# MODULE 5 - MULTIPLE WINDOWS

driver.get("https://the-internet.herokuapp.com/windows")
time.sleep(2)

parent = driver.current_window_handle

driver.find_element(By.LINK_TEXT, "Click Here").click()

time.sleep(2)

for window in driver.window_handles:
    if window != parent:
        driver.switch_to.window(window)
        print("New Window:", driver.title)
        driver.close()

driver.switch_to.window(parent)

# MODULE 6 - IFRAME HANDLING

driver.get("https://the-internet.herokuapp.com/iframe")
time.sleep(2)

driver.switch_to.frame("mce_0_ifr")

textbox = driver.find_element(By.ID, "tinymce")
textbox.clear()
textbox.send_keys("Hello Selenium")

driver.switch_to.default_content()

# MODULE 7 - NESTED FRAMES

driver.get("https://the-internet.herokuapp.com/nested_frames")
time.sleep(2)

driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-left")

print(driver.find_element(By.TAG_NAME, "body").text)

driver.switch_to.default_content()

# MODULE 8 - DYNAMIC CONTROLS

driver.get("https://the-internet.herokuapp.com/dynamic_controls")
time.sleep(2)

driver.find_element(
    By.XPATH,
    "//form[@id='input-example']//button"
).click()

textbox = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//form[@id='input-example']//input")
    )
)

textbox.send_keys("Selenium")

# MODULE 9 - WEB TABLE VALIDATION

driver.get("https://the-internet.herokuapp.com/tables")
time.sleep(2)

rows = driver.find_elements(
    By.XPATH,
    "//table[@id='table1']/tbody/tr"
)

for row in rows:
    print(row.text)

# MODULE 10 - DRAG AND DROP

driver.get("https://the-internet.herokuapp.com/drag_and_drop")
time.sleep(2)

source = driver.find_element(By.ID, "column-a")
target = driver.find_element(By.ID, "column-b")

ActionChains(driver).drag_and_drop(
    source,
    target
).perform()

# MODULE 11 - MOUSE ACTIONS

driver.get("https://the-internet.herokuapp.com/context_menu")
time.sleep(2)

box = driver.find_element(By.ID, "hot-spot")

ActionChains(driver).context_click(box).perform()

alert = WebDriverWait(driver, 10).until(
    EC.alert_is_present()
)

print("Right Click Alert:", alert.text)

alert.accept()

# MODULE 12 - JAVASCRIPT EXECUTOR

driver.get("https://the-internet.herokuapp.com")
time.sleep(2)

heading = driver.find_element(By.TAG_NAME, "h1")

driver.execute_script(
    "arguments[0].style.border='3px solid red'",
    heading
)

time.sleep(2)

driver.quit()

