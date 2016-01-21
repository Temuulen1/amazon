from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://gmail.com')

emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('temuulen1234567@gmail.com')
emailElem.submit()

time.sleep(2)

passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys('Quality1234567')
passwordElem.submit()
