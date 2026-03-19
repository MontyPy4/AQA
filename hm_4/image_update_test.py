import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"


@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.maximize_window()
    yield d
    d.quit()


def test_image(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 10)

    third_image = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "img:nth-of-type(3)"))
    )

    assert third_image.get_attribute("alt") == "award"