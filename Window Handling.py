from selenium import webdriver
import time

# Open Chrome Browser
driver = webdriver.Chrome()

# Open website
driver.get("https://www.google.com")

# Maximize browser window
driver.maximize_window()
print("Browser Maximized")
time.sleep(2)

# Minimize browser window
driver.minimize_window()
print("Browser Minimized")
time.sleep(2)

# Set custom window size
driver.set_window_size(800, 600)
print("Window Size Set to 800x600")
time.sleep(2)

# Get current window size
size = driver.get_window_size()
print("Width:", size['width'])
print("Height:", size['height'])
time.sleep(2)

# Close browser
driver.quit()