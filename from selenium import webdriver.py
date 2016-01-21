import time
from selenium import webdriver
print ('Hello, enter the email you want to send the message to')
userEmail = input('')
print ('What would you like your email subject to be?')
userSubject = input('')
print ('Type your message please')
userText = input('')

browser = webdriver.Firefox()
browser.get('http://gmail.com')


emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('temuulen1234567@gmail.com')
emailElem.submit()

time.sleep(2)

passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys('Quality1234567')
passwordElem.submit()

time.sleep(5)

composeElem = browser.find_element_by_class_name('z0')
composeElem.click()

time.sleep(3)

toElem = browser.find_element_by_class_name('vO')
toElem.send_keys(userEmail)

time.sleep(1)

toElem = browser.find_element_by_class_name('aoT')
toElem.send_keys(userSubject)


bodyElem = browser.find_element_by_class_name('Am')
bodyElem.send_keys(userText)

time.sleep(2)

sendElem = browser.find_element_by_xpath("//div[@class='J-J5-Ji']/div[@class='T-I J-J5-Ji aoO T-I-atl L3']")
sendElem.click()


