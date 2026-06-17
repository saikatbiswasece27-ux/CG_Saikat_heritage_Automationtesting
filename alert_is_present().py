from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH,
"//button[text()='Click for JS Alert']").click()

wait = WebDriverWait(driver, 10)

alert = wait.until(
    EC.alert_is_present()
)

print("Alert Text:", alert.text)

alert.accept()

time.sleep(2)
driver.quit()