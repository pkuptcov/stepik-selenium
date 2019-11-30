import time


def test_check_button_add_to_cart(browser):
    add_to_cart_button = browser.find_elements_by_xpath("//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert len(add_to_cart_button) == 1
    time.sleep(30)
