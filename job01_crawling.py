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
all_url = driver.find_element('xpath', '/html/body/div[3]/div/div/div/div/main/section/div/ul[2]/li/a').get_attribute('href')
driver.get(all_url)
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
for i in range(13):
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(0.5)
list_review_url = []
hotel_name1 = []
hotel_name2 = []

for i in range(1, 11):
    base = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[2]/section[2]/div/div/div[{i}]/a').get_attribute("href")
    list_review_url.append(f"{base}/review")
    title1 = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[2]/section[2]/div/div/div[{i}]/a/div[1]/div[2]/div[2]').text
    hotel_name1.append(title1)
    title2 = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[2]/section[2]/div/div/div[{i}]/a/div/div[2]/div[1]').text
    hotel_name2.append(title2)
print(len(list_review_url))
print(len(hotel_name1))
print(hotel_name1)
print(hotel_name2)
print(list_review_url)

hap_hotel_name = []
for i in range(10):
    if('1'<= hotel_name1[i][0] <='9'):
        hap_hotel_name.append(hotel_name2[i])
    else:
        hap_hotel_name.append(hotel_name1[i])
print(hap_hotel_name)

review_url = []
for i in list_review_url:
    add = i.replace('www.yanolja.com/hotel','place-site.yanolja.com/places')
    review_url.append(add)
print(review_url)

for url in review_url:
    driver.get(url)
    time.sleep(1)
    reviews = []
    review = ''
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(0.5)
    driver.execute_script("window.scrollTo(1, document.documentElement.scrollHeight);")
    time.sleep(0.5)
    for i in range(20):
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(0.5)

    # driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    # time.sleep(0.5)
    # for j in range(1, 11):
    #     review_xpath = '//*[@id="__next"]/div/div/main/div/div[4]/div/div[{}]/div/div/div[2]/div'.format(j)
    #     review = review + ' ' + driver.find_element(By.XPATH, review_xpath).text
    # reviews.append(review)
    # print(len(reviews))
    # for idx, url in enumerate(review_url[0:10]):
    #     driver.get(url)
    #     time.sleep(0.5)
    #     review = ''
    #     driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    #     time.sleep(0.5)
    #     driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    #     time.sleep(0.5)
    #     for j in range(1, 11):
    #         review_xpath = '//*[@id="__next"]/div/div/main/div/div[4]/div/div[{}]/div/div/div[2]/div'.format(j)
    #         review = review + ' ' + driver.find_element(By.XPATH, review_xpath).text
    #     reviews.append(review)
    # print(len(reviews))


# review = ''
#     driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight);')
#     time.sleep(1)
#     driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight);')
#     time.sleep(1)
#     for i in range(1, 31):
#         try:
#             review_title_xpath = '//*[@id="contents"]/div[2]/div[2]/div[{}]/div/div[3]/a[1]/div'.format(i)
#             review_more_xpath = '//*[@id="contents"]/div[2]/div[2]/div[{}]/div/div[3]/div/button'.format(i)
#             try:
#                 print(i)
#                 review_more = driver.find_element(By.XPATH, review_more_xpath)
#                 driver.execute_script('arguments[0].click();', review_more)
#                 time.sleep(1)
#                 review_xpath = '//*[@id="contents"]/div[2]/div[1]/div/section[2]/div/div/div/p'
#                 review += ' ' + driver.find_element(By.XPATH, review_xpath).text
#                 driver.back()
#                 time.sleep(1)
#             except:
#                 review += ' ' + driver.find_element(By.XPATH, review_title_xpath).text
#         except:
#             print('no more')
#     # print(review)
#     reviews.append(review + '@@')

# for i in range(1, 5):
#     one_hotel_driver = webdriver.Chrome(service=service, options=options)
#     try:
#         one_hotel_url = driver.find_element('xpath', '//*[@id="__next"]/div[2]/section[2]/div/div/div[{}]/a'.format(i)).get_attribute('href')
#         one_hotel_driver.get(one_hotel_url)
#         time.sleep(0.5)
#         button_movie_tv_xpath = '//*[@id="__next"]/div/div/main/article/div[1]/div/div[1]/div[4]'
#         button_movie_tv = driver.find_element(By.XPATH, button_movie_tv_xpath)
#         driver.execute_script('arguments[0].click();', button_movie_tv)  # 자바스크립트로 되어있어서 변형해준다
#         time.sleep(1)
        # driver.find_element('xpath', '//*[@id="__next"]/div/div/main/article/div[1]/div/div[1]/div[5]/div[3]/div/div[3]/div').click()
        # time.sleep(0.5)

        # title = one_movie_driver.find_element('xpath', '//*[@id="content"]/div[2]/div/div[1]/div[1]/strong').text
        #
        # text = one_movie_driver.find_element('xpath', '//*[@id="content"]/div[2]/ul/li[1]/div[3]/p').text
        # text = re.compile('[^가-힇]').sub(' ', text)
        #
        # movie_titles.append(title)
        # movie_synopsis.append(text)

    #     one_hotel_driver.close()
    # except:
    #     print('find element', i)
    #     one_hotel_driver.close()


        # //*[@id="__next"]/div/div/main/article/div[1]/div/div[1]/div[4]
        # //*[@id="__next"]/div/div/main/article/div[1]/div/div[1]/div[4]

        # ↓ 더보기 클릭 ↓
#             driver.find_element('xpath', '//*[@id="content"]/div[2]/button').click()
#             time.sleep(0.5)
#             for i in range(j * 30 + 1, j * 30 + 31):
#                 one_movie_driver = webdriver.Chrome(service=service, options=options)
#
# //*[@id="__next"]/div[2]/section[2]/div/div/div[2]/a
# one_hotel_url = []
# for i in list_review_url:
#     if ('1'<= i <= '9'):
#         one_hotel_url.append(i)
# print(one_hotel_url)

# re_title = re.compile('[^가-힣|a-z|A-Z]')
#
# reviews = []
# for url in list_review_url:
#     driver.get(url)
#     time.sleep(1)
# seoul_url = driver.find_element('xpath', '/html/body/div[3]/div/div/div/div/main/section/div/ul[2]/li/a').get_attribute('href')
# driver.get(seoul_url)
# time.sleep(0.5)
# //*[@id="__next"]/div[2]/section[2]/div/div/div[1]/a
# //*[@id="__next"]/div[2]/section[2]/div/div/div[2]/a



# https://place-site.yanolja.com/places/3013410/review

# list_review_url = pd.DataFrame(list_review_url)
# list_review_url.replace({'www' : 'place-site', 'hotel' : 'places'}, inplace=True)