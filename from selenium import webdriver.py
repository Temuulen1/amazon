from selenium import webdriver
print ('Enter Your Amazon Email PLS')
userEmail = input('')
print ('enter password')
userPassword = input('')


browser = webdriver.Firefox()
browser.get('http://amazon.com')

loginElem = browser.find_element_by_id('nav-link-yourAccount')
loginElem.click()

emailElem = browser.find_element_by_id('ap_email')
emailElem.send_keys(userEmail)

passwordElem = browser.find_element_by_id('ap_password')
passwordElem.send_keys(userPassword)
passwordElem.submit()
