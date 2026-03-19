import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "http://uitestingplayground.com/textinput"


@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.maximize_window()
    yield d
    d.quit()


def test_input(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 10)

    input_field = wait.until(
        EC.visibility_of_element_located((By.ID, "newButtonName"))
    )
    input_field.clear()
    input_field.send_keys("ITCH")

    button = wait.until(
        EC.element_to_be_clickable((By.ID, "updatingButton"))
    )
    button.click()

    wait.until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "ITCH")
    )

    assert button.text == "ITCH"