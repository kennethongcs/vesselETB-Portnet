from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.portnet.com/login')
assert 'Portnet' in driver.title #ensure that Portnet is being loaded

user_id = input('Please Input your Portnet User ')
user_pass = input('Please input your Portnet Password ')

username = driver.find_element_by_name('userid')
username.clear
username.send_keys(user_id)

password = driver.find_element_by_name('password')
password.clear
password.send_keys(user_pass)

driver.find_element_by_name('Login').click()
