from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import lxml.html as lh
import pandas as pd

driver = webdriver.Chrome()
driver.get('https://www.portnet.com/login')
window_main = driver.window_handles[0]
assert 'Portnet' in driver.title # ensure that Portnet is being loaded

# user_id = input('Please Input your Portnet User ')
# user_pass = input('Please input your Portnet Password ')

username = driver.find_element_by_name('userid')
username.clear
username.send_keys('Sslkeno1')

password = driver.find_element_by_name('password')
password.clear
password.send_keys('Welcome1')

driver.find_element_by_name('Login').click()

assert 'No results found.' not in driver.page_source
print('***You are in',driver.title,'***')

driver.implicitly_wait(5) # seconds

driver.switch_to_window(window_main)
driver.switch_to_frame('Main')
driver.find_element_by_partial_link_text('VEDA').click()

driver.implicitly_wait(5) # seconds
window_etb = driver.window_handles[1]
doc = lh.fromstring(window_etb.content)
vslName = driver.find_element_by_name('{actionForm.vslName}')
vslName.clear
vslName.send_keys('XING PING')
driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr/td/table[2]/tbody/tr[1]/td[4]/input').click()

# driver.quit()
