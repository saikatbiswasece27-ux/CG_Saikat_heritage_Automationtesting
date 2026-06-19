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
    driver.get("https://the-internet.herokuapp.com/tables")

    # Wait for the table to load
    wait.until(EC.presence_of_element_located((By.XPATH, "//table[@id='table1']")))

    # Print all rows
    rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr")
    print(f"Total rows: {len(rows)}")
    for row in rows:
        print(row.text)

    # Read a specific cell: row 1, column 1
    value = driver.find_element(By.XPATH, "//table[@id='table1']/tbody/tr[1]/td[1]").text
    print(f"\nCell [row1][col1]: {value}")

finally:
    driver.quit()
