# import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
from time import sleep
# from dotenv import load_dotenv

load_dotenv()

PROMISED_DOWN = 100
PROMISED_UP = 10
CHROME_DRIVER_PATH = 'C:/Development/chromedriver.exe'
TWITTER_ACCOUNT = os.getenv('TWITTER_ACCOUNT')
TWITTER_PASSWORD = os.getenv('TWITTER_PASSWORD')
TWITTER_URI = 'https://x.com/login'
SPEEDTEST_URI = 'https://www.speedtest.net/'


# --- Chrome Setup (persistent session) ---
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = "C:\\selenium_profiles\\twitter_profile"
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(SPEEDTEST_URI)
wait = WebDriverWait(driver, 30)

button = driver.find_element(By.CLASS_NAME, 'js-start-test')

button.click()

sleep(60)

down_speed = WebDriverWait(driver, 60).until(
    lambda d: d.find_element(By.CLASS_NAME, "download-speed").text != "--"
)

down_speed = float(driver.find_element(By.CLASS_NAME, "download-speed").text)

up_speed = WebDriverWait(driver, 60).until(
    lambda d: d.find_element(By.CLASS_NAME, "upload-speed").text != "--"
)

up_speed = float(driver.find_element(By.CLASS_NAME, "upload-speed").text)

print(up_speed)
print(down_speed)

if down_speed < PROMISED_DOWN or up_speed < PROMISED_UP:
    driver.get(TWITTER_URI)

    wait = WebDriverWait(driver, 20)

    username_input = wait.until(
        EC.presence_of_element_located((By.NAME, "text"))
    )
    username_input.send_keys(TWITTER_ACCOUNT)

    next_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']/ancestor::button"))
    )
    next_button.click()

    password_input = wait.until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_input.send_keys(TWITTER_PASSWORD)

    login_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="LoginForm_Login_Button"]'))
    )
    login_button.click()

    tweet_box = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="tweetTextarea_0"]'))
    )

    tweet = f"My internet is {down_speed}↓/{up_speed}↑. This is unacceptable."

    tweet_box.click()
    tweet_box.send_keys(tweet)

    # wait until button is actually clickable (enabled)
    post_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="tweetButtonInline"]'))
    )

    post_button.click()

input("Press Enter to exit...")