from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import lxml.html as lh
import pandas as pd
import csv
from bs4 import BeautifulSoup

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
try:
    driver.find_element_by_xpath('//*[@id="Login"]/table/tbody/tr[9]/td/p/input').click()
except:
    print('No token needed')

assert 'No results found.' not in driver.page_source
print('*** You are in',driver.title,'***')

driver.implicitly_wait(5) # seconds

driver.switch_to_window(window_main)
driver.switch_to_frame('Main')
driver.find_element_by_partial_link_text('VEDA').click()

#driver.implicitly_wait(5) # seconds

# finding vessel ETB
vslName = driver.find_element_by_name('{actionForm.vslName}')
vslName.clear
vslName.send_keys('XING PING')
driver.find_element_by_xpath('/html/body/form/table[1]/tbody/tr/td/table[2]/tbody/tr[1]/td[4]/input').click()

driver.implicitly_wait(5) # seconds

# entered ETB URL
window_etb = driver.window_handles[0]

page = requests.get(driver.current_url)
# USING SOUP
soup = BeautifulSoup(page,'html.parser')
frames = soup.findAll('frame',{'name':'main'})
# my_table = soup.find('table',{'border':'0'})
links = my_table.findAll('tr',{'class'})
print (links)
# header = []
# data = []
# for link in links:
#     header.append(link.get('title'))
# for m in soup.findAll('tr'):
#     data.append(m)

# with open('Sample.csv', 'w') as csvfile:
#       writer = csv.DictWriter(csvfile, fieldnames=header)
#       writer.writeheader()
#       tempDateList = []
#       DateList = []
#       for i in data:
#         tempDateList.append(i["Date"])
#       for i in tempDateList:
#         DateList.append(datetime.datetime.strptime(i, "%d-%b-%Y").strftime("%Y-%m-%d"))
#       for i in data:
#         writer.writerow(i)

# USING LXML
# doc = lh.fromstring(page)
# tr_elements = doc.xpath('//tr')

#Create empty list

col=[]
i=0
# For each row, store each first element (header) and an empty list

for t in links[0]:
    i+=1
    name=t.text_content()
    print ('%d:"%s"'%(i,name))
    col.append((name,[]))

# driver.quit()
