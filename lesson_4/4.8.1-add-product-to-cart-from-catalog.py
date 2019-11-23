from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

try:

    add_to_cart_first = browser.find_element_by_xpath("(//ol[@class='row']//button[@type='submit'])[1]")
    add_to_cart_first.click()

    alert_1 = WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.XPATH, "(//div[@class='alertinner '])[1]")))
    assert "The shellcoder's handbook" and "был добавлен в вашу корзину." in alert_1.text

    alert_2 = browser.find_element_by_xpath("(//div[@class='alertinner '])[2]")
    assert "Ваша корзина удовлетворяет условиям предложения" and "Deferred benefit offer" in alert_2.text

    alert_3 = browser.find_element_by_xpath("(//div[@class='alertinner ']/p)[1]")
    assert "Стоимость корзины теперь составляет" and "9,99 £" in alert_3.text

    view_cart_button = browser.find_element_by_xpath("//div[@class='alertinner ']/p/a[@href='/ru/basket/']")
    assert "Посмотреть корзину" == view_cart_button.text

    checkout_button = browser.find_element_by_xpath("//div[@class='alertinner ']/p/a[@href='/ru/checkout/']")
    assert "Оформить" == checkout_button.text

    price_in_cart = browser.find_element_by_xpath("//div[@class='basket-mini pull-right hidden-xs']")
    assert 'Всего в корзине:' and '9,99 £' in price_in_cart.text

finally:
    browser.quit()
