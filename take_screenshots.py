import os
from selenium import webdriver

if not os.path.exists('shots'):
    os.makedirs('shots')

urls = []
with open('url_list.txt') as f:
    urls = f.readlines()

driver = webdriver.Chrome('./chromedriver')

count = 1
for url in urls:
    url = url.strip()

    driver.get(url)
    driver.save_screenshot('shots/screenshot{}.png'.format(count))
    count += 1
driver.close()