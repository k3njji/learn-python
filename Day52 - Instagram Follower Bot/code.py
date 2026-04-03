from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
from selenium.common.exceptions import TimeoutException

load_dotenv()

IG_URL = 'https://www.instagram.com/'
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(IG_URL)

username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
)

password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "pass"))
)

username_input.send_keys(INSTAGRAM_USERNAME)
password_input.send_keys(INSTAGRAM_PASSWORD)

login_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[role="button"][aria-label="Log in"]'))
)

login_button.click()

def click_if_exists(xpath, timeout=5):
    try:
        el = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        el.click()
        return True
    except TimeoutException:
        return False
    
click_if_exists("//div[@role='button' and text()='Not now']")
click_if_exists("//button[normalize-space()='Not Now']")

account = input("Enter the account you want: ")

driver.get(IG_URL+account)

following_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/following/')]"))
)
following_btn.click()

import time

for _ in range(5):  # scroll 5 times
    follow_buttons = driver.find_elements(
        By.XPATH, "//button[.//div[normalize-space()='Follow']]"
    )

    for btn in follow_buttons:
        try:
            driver.execute_script("arguments[0].click();", btn)
            time.sleep(1)
        except:
            pass

    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(2)

input("Press Enter to exit...")