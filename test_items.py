from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button_add_to_basket(browser):
    browser.get(link)
    # time.sleep(10)
    assert WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, '//form[@id="add_to_basket_form"]'
                                                  '//button[@type="submit"]'))), 'Кнопка не найдена.'
