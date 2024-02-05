from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pandas as pd
import re
import time
import datetime

options = ChromeOptions()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
options.add_argument('user-agent=' + user_agent)
options.add_argument("lang=ko_KR")

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

start_url = 'https:/www.yanolja.com/'
button_region_xpath = '//*[@id="__next"]/div[1]/main/section/section/section/section[1]/div/div/div/button'
driver.get(start_url)
time.sleep(0.5)
hotel_url = driver.find_element('xpath', '//*[@id="__next"]/div[1]/section[1]/section/section/section[1]/div[1]/a[1]').get_attribute('href')
driver.get(hotel_url)
time.sleep(0.5)
button_region = driver.find_element(By.XPATH, button_region_xpath)
driver.execute_script('arguments[0].click();', button_region)
time.sleep(0.5)
seoul_url = driver.find_element('xpath', '/html/body/div[3]/div/div/div/div/main/section/div/ul[2]/li/a').get_attribute('href')
driver.get(seoul_url)
time.sleep(0.5)
# button_busan_xpath = 'html/body/div[3]/div/div/div/div/main/section/div/ul[1]/li[2]'
# button_busan = driver.find_element(By.XPATH, button_busan_xpath)
# driver.execute_script('arguments[0].click();', button_busan)
# time.sleep(0.5)

button_popular_xpath = '//*[@id="__next"]/div[2]/section[1]/button'
button_popular = driver.find_element(By.XPATH, button_popular_xpath)
driver.execute_script('arguments[0].click();', button_popular)
time.sleep(0.5)
button_many_xpath = '/html/body/div[4]/div/div/section/div/ul/li[5]/button'
button_many = driver.find_element(By.XPATH, button_many_xpath)
driver.execute_script('arguments[0].click();', button_many)
time.sleep(1)
for i in range(3):
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(0.5)
list_review_url = []
hotel_name = []

for i in range(1, 11):
    base = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[2]/section[2]/div/div/div[{i}]/a/div').get_attribute("href")
    list_review_url.append(f"{base}/review")
    title = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[2]/section[2]/div/div/div[{i}]/a/div[1]/div[2]/div[2]').text
    hotel_name.append(title)
print(len(list_review_url))
print(len(hotel_name))
print(hotel_name[:5])
