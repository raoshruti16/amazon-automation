# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 20:22:08 2020

@author: shruti
"""


from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import logindata2

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver', chrome_options=options)
action = ActionChains(driver)
time.sleep(1)


driver.get('http://www.amazon.in')
time.sleep(3)
 
firstLevelMenu = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]')
action.move_to_element(firstLevelMenu).perform()
time.sleep(3)
 
secondLevelMenu = driver.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span')
secondLevelMenu.click()
time.sleep(3)

signinelement = driver.find_element_by_xpath('//*[@id="ap_email"]')
signinelement.send_keys(logindata2.USERNAME)
time.sleep(3)

cont = driver.find_element_by_xpath('//*[@id="continue"]')
cont.click()
time.sleep(3)

passwordelement = driver.find_element_by_xpath('//*[@id="ap_password"]')
passwordelement.send_keys(logindata2.PASSWORD)
time.sleep(3)

login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
login.click()
time.sleep(3)

search = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
search.send_keys('sunglasses')
search.send_keys(Keys.ENTER)
time.sleep(3)
sortby = driver.find_element_by_xpath('//*[@id="a-autoid-0-announce"]')
sortby.click()
time.sleep(3)
low = driver.find_element_by_xpath('//*[@id="s-result-sort-select_1"]')
low.click()
time.sleep(3)
elem1 = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[5]/div/span/div/div/div[2]/div/span/a/div/img')
elem1.click()
time.sleep(3)
driver.switch_to_window(driver.window_handles[1]) ##used to switche between tabs
wishlist = driver.find_element_by_xpath('//*[@id="add-to-wishlist-button-submit"]')
wishlist.click()
time.sleep(3)
Continue = driver.find_element_by_xpath('//*[@id="WLHUC_continue"]')
Continue.click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').clear()



search = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
search.send_keys('coffee mug')
search.send_keys(Keys.ENTER)
time.sleep(3)
sortby = driver.find_element_by_xpath('//*[@id="a-autoid-0-announce"]/span[1]')
sortby.click()
time.sleep(3)
low = driver.find_element_by_xpath('//*[@id="s-result-sort-select_1"]')
low.click()
time.sleep(3)
elem1 = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[4]/div/span/div/div/span/a/div/img')
elem1.click()
time.sleep(3)
driver.switch_to_window(driver.window_handles[2]) ##used to switche between tabs
wishlist = driver.find_element_by_xpath('//*[@id="add-to-wishlist-button-submit"]')
wishlist.click()
time.sleep(3)
Continue = driver.find_element_by_xpath('//*[@id="WLHUC_continue"]')
Continue.click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').clear()



search = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
search.send_keys('earring')
search.send_keys(Keys.ENTER)
time.sleep(3)
sortby = driver.find_element_by_xpath('//*[@id="a-autoid-0-announce"]/span[1]')
sortby.click()
time.sleep(3)
low = driver.find_element_by_xpath('//*[@id="s-result-sort-select_1"]')
low.click()
time.sleep(3)
elem1 = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[5]/div/span/div/div/div[2]/div/span/a/div/img')
elem1.click()
time.sleep(3)
driver.switch_to_window(driver.window_handles[3]) ##used to switche between tabs
wishlist = driver.find_element_by_xpath('//*[@id="add-to-wishlist-button-submit"]')
wishlist.click()
time.sleep(3)
Continue = driver.find_element_by_xpath('//*[@id="WLHUC_continue"]')
Continue.click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').clear()



search = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
search.send_keys('pen')
search.send_keys(Keys.ENTER)
time.sleep(3)
sortby = driver.find_element_by_xpath('//*[@id="a-autoid-0-announce"]/span[1]')
sortby.click()
time.sleep(3)
low = driver.find_element_by_xpath('//*[@id="s-result-sort-select_1"]')
low.click()
time.sleep(3)
elem1 = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[4]/div/span/div/div/span/a/div/img')
elem1.click()
time.sleep(3)
driver.switch_to_window(driver.window_handles[4]) ##used to switche between tabs
wishlist = driver.find_element_by_xpath('//*[@id="add-to-wishlist-button-submit"]')
wishlist.click()
time.sleep(3)
Continue = driver.find_element_by_xpath('//*[@id="WLHUC_continue"]')
Continue.click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').clear()



search = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
search.send_keys('ring')
search.send_keys(Keys.ENTER)
time.sleep(3)
sortby = driver.find_element_by_xpath('//*[@id="a-autoid-0-announce"]/span[1]')
sortby.click()
time.sleep(3)
low = driver.find_element_by_xpath('//*[@id="s-result-sort-select_1"]')
low.click()
time.sleep(3)
elem1 = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[4]/div/span/div/div/div[2]/div/span/a/div/img')
elem1.click()
time.sleep(3)
driver.switch_to_window(driver.window_handles[5]) ##used to switche between tabs
wishlist = driver.find_element_by_xpath('//*[@id="add-to-wishlist-button-submit"]')
wishlist.click()
time.sleep(3)
Continue = driver.find_element_by_xpath('//*[@id="WLHUC_continue"]')
Continue.click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').clear()
 


wishlist = driver.find_element_by_xpath('//*[@id="add-to-wishlist-button-submit"]')
wishlist.click() 
time.sleep(3) 

view = driver.find_element_by_xpath('//*[@id="WLHUC_viewlist"]/span/span')
view.click()
time.sleep(3)

'driver.switch_to_window(driver.window_handles[6])'
driver.execute_script("window.scrollTo(0,(document.body.scrollHeight)/2)")

cart = driver.find_element_by_xpath('//*[@id="pab-I34ZU2LENW7Y6N"]/span/a')
cart.click()
time.sleep(3)

proceed = driver.find_element_by_xpath('//*[@id="itemAction_I34ZU2LENW7Y6N"]/div[2]/span[1]/span/a')
proceed.click()
time.sleep(3)

deliver = driver.find_element_by_xpath('//*[@id="address-book-entry-0"]/div[2]/span/a')
deliver.click()
time.sleep(3)


Continue = driver.find_element_by_xpath('//*[@id="shippingOptionFormId"]/div[1]/div[2]/div/span[1]/span/input')
Continue.click()
time.sleep(3)
'''
search = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
search.send_keys(Keys.BACKSPACE)
search.send_keys('coffee mug')
search.send_keys(Keys.ENTER)
time.sleep(3)

sortby = driver.find_element_by_xpath('//*[@id="a-autoid-0-announce"]/span[1]')
sortby.click()
time.sleep(3)

low = driver.find_element_by_xpath('//*[@id="s-result-sort-select_1"]')
low.click()
time.sleep(3)

elem2 = driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[4]/div/span/div/div/span/a/div/img')
elem2.click()
time.sleep(3)

driver.switch_to_window(driver.window_handles[1])

wishlist = driver.find_element_by_xpath('//*[@id="add-to-wishlist-button-submit"]')
wishlist.click()
time.sleep(3)

Continue = driver.find_element_by_xpath('//*[@id="shippingOptionFormId"]/div[1]/div[2]/div/span[1]/span/input')
Continue.click()
time.sleep(3)


proceed = driver.find_element_by_xpath('//*[@id="itemAction_I34ZU2LENW7Y6N"]/div[3]/span[1]/span/a')
proceed.click()
time.sleep(3)

'''
