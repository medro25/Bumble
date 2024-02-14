from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://bumble.com/')

# Define WebDriverWait
wait = WebDriverWait(driver, 10) # 10 seconds wait time

# Update the CSS Selector
# This is a placeholder, you need to replace it with the correct selector
def kirjaudu():
    try:
        # Wait until the element is clickable
        link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Kirjaudu'))
        )
        # Click the link once it's clickable
        link.click()
    except TimeoutException:
        print("Timed out waiting for the 'Kirjaudu' button to appear")

    time.sleep(10)
def like():
    try:
        # Wait until the like button is clickable
        like_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#main > div > div.page__layout > main > div.page__content-inner > div > div > span > div.encounters-user__controls > div > div:nth-child(2) > div > div:nth-child(3) > div > div.encounters-action__icon > span'))
        )
        # Click the like button once it's clickable
        like_element.click()
    except TimeoutException:
        print("Timed out waiting for the 'like' button to appear")


def dislike():
    try:
        # Wait until the dislike button is clickable
        dislike_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#main > div > div.page__layout > main > div.page__content-inner > div > div > span > div.encounters-user__controls > div > div:nth-child(2) > div > div:nth-child(3) > div > div.encounters-action__icon > span'))
        )
        # Click the dislike button once it's clickable
        dislike_element.click()
    except TimeoutException:
        print("Timed out waiting for the 'dislike' button to appear")


def auto_swipe():
    
    from random import random
    left_count, right_count = 0, 0 
    while True:
        time.sleep(0.1)
        
        rand = random()
        if rand < 0.93:
            like()
            right_count += 1
            print('{}th right swipe'.format(right_count))
        else:
            dislike()
            left_count += 1
            print('{}th left swipe'.format(left_count))
kirjaudu()
time.sleep(2)
auto_swipe()