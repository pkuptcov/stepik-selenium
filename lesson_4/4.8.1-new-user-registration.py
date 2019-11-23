from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

try:

    login_email = browser.find_element_by_xpath("//input[@id='id_registration-email']")
    login_email.send_keys("test1234512312346@gmail.com")
    login_password = browser.find_element_by_xpath("//input[@id='id_registration-password1']")
    login_password.send_keys("Qw1234567")
    login_password_confirm = browser.find_element_by_xpath("//input[@id='id_registration-password2']")
    login_password_confirm.send_keys("Qw1234567")
    registration_submit = browser.find_element_by_xpath("//button[@name='registration_submit']")
    registration_submit.click()

    success_message = WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='alertinner wicon']")))
    assert 'Спасибо за регистрацию!' in success_message.text

    account_link = browser.find_elements_by_xpath("//a[@href='/ru/accounts/']")
    assert len(account_link) == 1

    logout_link = browser.find_elements_by_xpath("//a[@href='/ru/accounts/logout/']")
    assert len(logout_link) == 1

finally:
    browser.quit()
