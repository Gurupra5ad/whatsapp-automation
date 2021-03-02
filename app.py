from selenium import webdriver
import time

browser = webdriver.Chrome('/home/disciple/chromedriver')
browser.get('https://web.whatsapp.com/')

time.sleep(15)

user_name = 'Whatsapp bot'

user = browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
user.click()

message_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
message_box.send_keys('Hey, I am your whatsapp bot')

message_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
message_box.click()
