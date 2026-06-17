from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com")

print("Title:", driver.title)
print("URL:", driver.current_url)

driver.save_screenshot("page.png")

search_box = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "small-searchterms"))
)

search_box.send_keys("LAPTOP")

input("Press Enter...")
driver.quit()
