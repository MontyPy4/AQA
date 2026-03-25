import json
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

STATE_FILE = "consent_state.json"
BASE = "https://www.globalsqa.com/"
URL = "https://www.globalsqa.com/demo-site/draganddrop/"

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.maximize_window()
    yield d
    d.quit()

def restore_consent_state(driver):
    driver.get(BASE)

    with open(STATE_FILE, "r", encoding="utf-8") as f:
        state = json.load(f)

    for c in state.get("cookies", []):
        payload = {"name": c["name"], "value": c["value"], "path": c.get("path", "/")}
        if "expiry" in c:
            payload["expiry"] = c["expiry"]
        try:
            driver.add_cookie(payload)
        except Exception:
            pass

    driver.execute_script("localStorage.clear(); sessionStorage.clear();")
    for k, v in state.get("localStorage", {}).items():
        driver.execute_script("localStorage.setItem(arguments[0], arguments[1]);", k, v)
    for k, v in state.get("sessionStorage", {}).items():
        driver.execute_script("sessionStorage.setItem(arguments[0], arguments[1]);", k, v)

    driver.get(URL)

def drag_drop_js(driver, src, tgt):
    driver.execute_script("""
        const src = arguments[0];
        const tgt = arguments[1];

        const s = src.getBoundingClientRect();
        const t = tgt.getBoundingClientRect();

        const startX = s.left + s.width / 2;
        const startY = s.top + s.height / 2;
        const endX = t.left + t.width / 2;
        const endY = t.top + t.height / 2;

        function fire(el, type, x, y) {
            el.dispatchEvent(new MouseEvent(type, {
                bubbles: true,
                cancelable: true,
                view: window,
                clientX: x,
                clientY: y
            }));
        }

        fire(src, "mousedown", startX, startY);
        fire(document, "mousemove", startX + 5, startY + 5);
        fire(document, "mousemove", endX, endY);
        fire(tgt, "mouseup", endX, endY);
    """, src, tgt)

def test_drag_and_drop(driver):
    restore_consent_state(driver)

    wait = WebDriverWait(driver, 20)

    frame = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame")))
    driver.switch_to.frame(frame)

    source = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#gallery li")))[0]
    trash = wait.until(EC.visibility_of_element_located((By.ID, "trash")))

    drag_drop_js(driver, source, trash)

    wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, "#trash li")) == 1)

    assert len(driver.find_elements(By.CSS_SELECTOR, "#trash li")) == 1
    assert len(driver.find_elements(By.CSS_SELECTOR, "#gallery li")) == 3