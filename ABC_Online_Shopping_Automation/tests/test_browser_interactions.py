from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_double_click(setup):

    driver = setup
    wait = WebDriverWait(driver, 10)

    driver.get("https://demoqa.com/buttons")

    button = wait.until(
        EC.visibility_of_element_located((By.ID, "doubleClickBtn"))
    )

    print("Displayed :", button.is_displayed())
    print("Enabled :", button.is_enabled())

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", button)

    ActionChains(driver).move_to_element(button).double_click(button).perform()

    print("Double Click Performed")

    message = wait.until(
        EC.presence_of_element_located((By.ID, "doubleClickMessage"))
    )

    print("Message :", message.text)

    assert message.text == "You have done a double click"


def test_right_click(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    driver.get("https://demoqa.com/buttons")

    button = wait.until(
        EC.visibility_of_element_located((By.ID, "rightClickBtn"))
    )

    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", button)

    ActionChains(driver).move_to_element(button).context_click(button).perform()

    message = wait.until(
        EC.visibility_of_element_located((By.ID, "rightClickMessage"))
    )

    assert message.text == "You have done a right click"

    print("Right Click Passed")


def test_js_alert(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Click for JS Alert']")
        )
    ).click()

    alert = driver.switch_to.alert
    alert.accept()

    result = wait.until(
        EC.visibility_of_element_located((By.ID, "result"))
    ).text

    assert result == "You successfully clicked an alert"

    print("JS Alert Passed")


def test_js_confirm(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Click for JS Confirm']")
        )
    ).click()

    alert = driver.switch_to.alert
    alert.dismiss()

    result = wait.until(
        EC.visibility_of_element_located((By.ID, "result"))
    ).text

    assert result == "You clicked: Cancel"

    print("JS Confirm Passed")


def test_js_prompt(setup):
    driver = setup
    wait = WebDriverWait(driver, 10)

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Click for JS Prompt']")
        )
    ).click()

    alert = driver.switch_to.alert
    alert.send_keys("Saikat")
    alert.accept()

    result = wait.until(
        EC.visibility_of_element_located((By.ID, "result"))
    ).text

    assert result == "You entered: Saikat"

    print("JS Prompt Passed")