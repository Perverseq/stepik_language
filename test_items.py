import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button_add_to_basket(browser):
    browser.get(link)
    # time.sleep(10)
    assert browser.find_element_by_xpath('//form[@id="add_to_basket_form"]//button[@type="submit"]'), \
        'Кнопка не найдена'
