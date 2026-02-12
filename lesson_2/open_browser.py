from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest
# import os

# ЭТО скрипт, а не тест - тест это проверка - в скрипте нет ожидаемого результата

@pytest.fixture
def driver():
    # service = Service("/Users/romansurkov/Documents/chromedriver-mac-arm64/chromedriver")
    # options = Options()
    # driver = webdriver.Chrome(service=service, options=options)
    driver = webdriver.Chrome()  # Инициализация браузера
    driver.maximize_window()  # Максимизация окна
    # driver.set_window_size(640, 460)  # область видимости
    # driver = webdriver.Chrome(service=service)
    # driver = webdriver.Chrome(options=options)
    yield driver  # завершение
    driver.quit()

def test_about_page(driver):
    driver.get("https://itcareerhub.de/ru")  # открыть страницу
    sleep(3)                                 # задержка
    about_link = driver.find_element(By.LINK_TEXT, "О нас")  # нахождение элемента
    about_link.click() # клик
    sleep(3) # задержка

def test_berlin(driver):
    driver.get("https://itcareerhub.de/ru")
    driver.refresh()
    driver.get("https://www.berlin.de")
    driver.save_screenshot("./berlin_s.png")  # скрин страницы
    sleep(2)
    driver.refresh() # обновление страницы
    driver.back()    # вернуться на пред. страницу
    sleep(2)
    driver.forward()  # вперед страница
    driver.refresh()
    sleep(2)