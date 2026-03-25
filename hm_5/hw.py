# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support import expected_conditions as EC


# URL = "https://www.globalsqa.com/demo-site/draganddrop/"

# # Открыть страницу Drag & Drop Demo.
# #  Перейти по ссылке: https://www.globalsqa.com/demo-site/draganddrop/.
# # Выполнить следующие шаги:
# # ● Захватить первую фотографию (верхний левый элемент).
# # ● Перетащить её в область корзины (Trash).
# # ● Проверить, что после перемещения:
# # ○ В корзине появилась одна фотография.
# # ○ В основной области осталось 3 фотографии.
# # Ожидаемый результат:
# # ● Фотография успешно перемещается в корзину.
# # ● Вне корзины остаются 3 фотографии.

# @pytest.fixture
# def driver():
#     d = webdriver.Chrome()
#     d.maximize_window()
#     yield d
#     d.quit()


# # from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# def accept_cookies(driver):
#     wait = WebDriverWait(driver, 10)

#     try:
#         btn = WebDriverWait(driver, 5).until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label*='Accept']"))
#         )
#         btn.click()
#         return True
#     except TimeoutException:
#         pass

#     frames = driver.find_elements(By.CSS_SELECTOR, "iframe")
#     for fr in frames:
#         src = (fr.get_attribute("src") or "").lower()
#         fid = (fr.get_attribute("id") or "").lower()
#         fcls = (fr.get_attribute("class") or "").lower()

#         if any(x in (src + " " + fid + " " + fcls) for x in ["consent", "cookie", "gdpr", "truste", "sp_message"]):
#             driver.switch_to.frame(fr)
#             try:
#                 btn = WebDriverWait(driver, 5).until(
#                     EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label*='Accept'], button[title*='Accept'], button[id*='accept'], button[class*='accept']"))
#                 )
#                 btn.click()
#                 driver.switch_to.default_content()
#                 return True
#             except TimeoutException:
#                 driver.switch_to.default_content()

#     return False


# def accept_cookie_if_present(driver) -> bool:
#     try:
#         btn = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, ".fc-cta-consent"))
#         )
#         btn.click()
#         WebDriverWait(driver, 10).until(EC.staleness_of(btn))
#         return True
#     except Exception:
#         return False


# def test_drag_and_drop(driver):
#     wait = WebDriverWait(driver, 10)
#     driver.get(URL)

#     accept_cookie_if_present(driver)

#     frame = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame")))
#     driver.switch_to.frame(frame)

#     source = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#gallery li")))[0]
#     trash = wait.until(EC.visibility_of_element_located((By.ID, "trash")))

#     ActionChains(driver).drag_and_drop(source, trash).perform()

#     wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#trash li")))

#     assert len(driver.find_elements(By.CSS_SELECTOR, "#trash li")) == 1
#     assert len(driver.find_elements(By.CSS_SELECTOR, "#gallery li")) == 3


# def accept_cookies_if_present(driver):
#     candidates = [
#         # "#onetrust-accept-btn-handler",
#         # "button#onetrust-accept-btn-handler",
#         "button[aria-label*='Accept']", #наш вариант тут, подходит на любом языке
#         # "button[aria-label*='accept']",
#         # "button[title*='Accept']",
#         # "button[title*='accept']",
#         # "button[class*='accept']",
#         # "button[id*='accept']",
#         # "a[class*='accept']",
#         # "a[id*='accept']",
#     ]
#     for css in candidates:
#         try:
#             btn = WebDriverWait(driver, 5).until(
#                 EC.element_to_be_clickable((By.CSS_SELECTOR, css))
#             )
#             btn.click()
#             return True
#         except Exception:
#             pass
#     return False


# def nuke_cookie_overlays(driver):
# driver.execute_script("""
#     const selectors = [
#       "[id*='cookie']", "[class*='cookie']",
#       "[id*='consent']", "[class*='consent']",
#       ".cookie-banner", ".cookie-notice", ".cookie-consent",
#       ".cc-window", ".cc-banner"
#     ];
#     selectors.forEach(sel => {
#       document.querySelectorAll(sel).forEach(el => el.remove());
#     });
#     document.body.style.overflow = "auto";
# """)


# def switch_to_dnd_frame(driver, wait):
#     wait.until(lambda d: len(d.find_elements(By.TAG_NAME, "iframe")) > 0)
#     frames = driver.find_elements(By.TAG_NAME, "iframe")

#     for fr in frames:
#         src = (fr.get_attribute("src") or "").lower()
#         if "drag" in src or "droppable" in src or "photo" in src or "jqueryui" in src:
#             driver.switch_to.frame(fr)
#             return

#     driver.switch_to.frame(frames[0])


# @pytest.fixture
# def browser():
#     d = webdriver.Chrome()
#     d.maximize_window()
#     yield d
#     d.quit()


# def test_drag_drop_trash(browser):
#     wait = WebDriverWait(browser, 10)
#     browser.get(URL)

#     if not accept_cookies_if_present(browser):
#         # 2) Если не нашли кнопку, убираем оверлеи “жёстко”
#         nuke_cookie_overlays(browser)

#     switch_to_dnd_frame(browser, wait)

#     gallery_items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#gallery li")))
#     assert len(gallery_items) == 4

#     first = gallery_items[0]
#     trash = wait.until(EC.visibility_of_element_located((By.ID, "trash")))

#     ActionChains(browser).click_and_hold(first).move_to_element(trash).release().perform()

#     wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#trash li")) == 1)
#     assert len(browser.find_elements(By.CSS_SELECTOR, "#trash li")) == 1
#     assert len(browser.find_elements(By.CSS_SELECTOR, "#gallery li")) == 3

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.globalsqa.com/demo-site/draganddrop/"


@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.maximize_window()

    d.get(URL)

    consent_cookie = {
        "name": "FCCDCF",
        "value": "%5Bnull%2Cnull%2Cnull%2C%5B%22CQgl8sAQgl8sAEsACBENCUFoAP_gAEPgABBoK1IB_C7EbCFCiDJ3IKMEMAhHABBAYsAwAAYBAwAADBIQIAQCgkEYBASAFCACCAAAKASBAAAgCAAAAUAAIAAFAABAAAwAIBAIIAAAgAAAAEAIAAAACIAAEQCAAAAEAEAAkAgAAAIASAAAAAAAAACBAAAAAAAAAAAAAAAABAEAAQAAQAAAAAAAiAAAAAAAABAIAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAABAAAAAAAQWEQD-F2I2EKFEGCuQUYIYBCuACAAxYBgAAwCBgAAGCQgQAgFJIIkCAEAIEAAEAAAQAgCAABQEBAAAIAAAAAqAACAABgAQCAQAIABAAAAgIAAAAAAEQAAIgEAAAAIAIABABAAAAQAkAAAAAAAAAECAAAAAAAAAAAAAAAAAAIAAEABgAAAAAABEAAAAAAAACAQIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAA.ILCIB_C7EbCFCiDJ3IKMEMAhXABBAYsAwAAYBAwAADBIQIAQCkkEaBASAFCACCAAAKASBAAAoCAgAAUAAIAAVAABAAAwAIBAIIEAAgAAAQEAIAAAACIAAEQCAAAAEAEAAkAgAAAIASAAAAAAAAACBAAAAAAAAAAAAAAAABAEAASAAwAAAAAAAiAAAAAAAABAIEAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAABAAAAAAAQAAAE%22%2C%222~61.89.122.161.184.196.230.314.442.445.494.550.576.827.1029.1033.1046.1047.1051.1097.1126.1166.1301.1342.1415.1725.1765.1942.1958.1987.2068.2072.2074.2107.2213.2219.2223.2224.2328.2331.2387.2416.2501.2567.2568.2575.2657.2686.2778.2869.2878.2908.2920.2963.3005.3023.3126.3234.3235.3253.3309.3731.6931.8931.13731.15731.33931~dv.%22%2C%2212B1A492-A3E1-4AB1-8265-0AC9C6F70FA1%22%5D%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%22b7049a38-ceb4-4b15-9a2b-b4be27488197%5C%22%2C%5B1772729210%2C963000000%5D%5D%22%5D%5D%5D",
        "domain": ".globalsqa.com",
        "path": "/",
        "secure": False,
    }

    d.add_cookie(consent_cookie)
    d.refresh()

    yield d
    d.quit()


def test_drag_and_drop(driver):
    wait = WebDriverWait(driver, 10)

    frame = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame")))
    driver.switch_to.frame(frame)

    source = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#gallery li")))[0]
    trash = wait.until(EC.visibility_of_element_located((By.ID, "trash")))

    ActionChains(driver).drag_and_drop(source, trash).perform()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#trash li")))

    assert len(driver.find_elements(By.CSS_SELECTOR, "#trash li")) == 1
    assert len(driver.find_elements(By.CSS_SELECTOR, "#gallery li")) == 3