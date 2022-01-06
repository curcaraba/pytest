import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_basket_button(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button, "Couldn't find button!"
