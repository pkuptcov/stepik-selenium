from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = "http://selenium1py.pythonanywhere.com/ru/"
browser = webdriver.Chrome()
browser.maximize_window()

try:
    browser.get(link)

    select_language = Select(browser.find_element_by_xpath("//*[@name='language']"))
    select_language.select_by_value('en-gb')
    button = browser.find_element_by_xpath("//button[@type='submit'][@class='btn btn-default']")
    button.click()

    assert browser.current_url == 'http://selenium1py.pythonanywhere.com/en-gb/'

    language_en = browser.find_element_by_xpath("//option[@value='en-gb'][@selected='selected']")
    assert 'British English' in language_en.text

    button = browser.find_element_by_xpath("//button[@type='submit'][@class='btn btn-default']")
    assert 'Go' == button.text

    login_link = browser.find_element_by_xpath("//a[@id='login_link']")
    assert 'Login or register' in login_link.text

finally:
    browser.quit()
