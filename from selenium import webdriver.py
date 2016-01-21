import time
from selenium import webdriver
print ('Hello, enter the email you want to send the message to')
userEmail = input('')
print ('What is your message?')
userText = input('')

browser = webdriver.Firefox()
browser.get('http://gmail.com')


emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('temuulen1234567@gmail.com')
emailElem.submit()

time.sleep(3)

passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys('Quality1234567')
passwordElem.submit()

time.sleep(7)

composeElem = browser.find_element_by_class_name('z0')
composeElem.click()

time.sleep(3)

toElem = browser.find_element_by_class_name('vO')
toElem.send_keys(userEmail)

time.sleep(3)

subjElem = browser.find_element_by_class_name('Am.Al.editable.LW-avf')
subjElem.send_keys(usertext)





