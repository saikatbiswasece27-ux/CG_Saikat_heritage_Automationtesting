from selenium import webdriver
def test_google_title():

# Launch Browser
    driver = webdriver.Chrome()
    driver.maximize_window()

# Open
    driver.get("https://www.google.com/")
    assert "Google" == driver.title
    driver.quit()

