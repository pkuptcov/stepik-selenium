from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = "http://selenium1py.pythonanywhere.com/ru/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

try:

    login_link = browser.find_element_by_xpath("//a[@id='login_link']")
    login_link.click()

    auth_form = browser.find_elements_by_xpath("//form[@id='login_form']")
    assert len(auth_form) == 1

    reg_form = browser.find_elements_by_xpath("//form[@id='register_form']")
    assert len(reg_form) == 1

finally:
    browser.quit()
