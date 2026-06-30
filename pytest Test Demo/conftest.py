import pytest
from selenium import webdriver
@pytest.fixture
def driver():
 # ── SETUP (before test) ──
 print('\n[SETUP] Opening browser...')

 drv = webdriver.Chrome()
 drv.maximize_window()
 yield drv # <-- This is where the TEST runs
 # ── TEARDOWN (after test) ──
 print('[TEARDOWN] Closing browser...')
 drv.quit()
def test_google_title(driver):
 driver.get('https://www.google.com')
 assert 'Google' in driver.title