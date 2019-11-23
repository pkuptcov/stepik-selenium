from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

try:

    login_email = browser.find_element_by_xpath("//input[@id='id_login-username']")
    login_email.send_keys("test12345@gmail.com")
    login_password = browser.find_element_by_xpath("//input[@id='id_login-password']")
    login_password.send_keys("Qw1234567")
    login_submit = browser.find_element_by_xpath("//button[@name='login_submit']")
    login_submit.click()

    success_message = WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='alertinner wicon']")))
    assert 'Рады видеть вас снова' in success_message.text

    account_link = browser.find_elements_by_xpath("//a[@href='/ru/accounts/']")
    assert len(account_link) == 1

    logout_link = browser.find_elements_by_xpath("//a[@href='/ru/accounts/logout/']")
    assert len(logout_link) == 1

finally:
    browser.quit()
