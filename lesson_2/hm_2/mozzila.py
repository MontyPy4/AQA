import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    # Инициализация Firefox
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_payment_section(driver):
    # 1 Открываем сайт
    driver.get("https://itcareerhub.de/ru")
    sleep(3)

    # 2 Переходим в раздел "Способы оплаты"
    payment_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    payment_link.click()
    sleep(3)

    # 3 Делаем скриншот
    driver.save_screenshot("./payment_section.png")
    sleep(2)