from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'http://secure-retreat-92358.herokuapp.com/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

wait = WebDriverWait(driver, 10)

first_name = wait.until(
    EC.presence_of_element_located((By.NAME, "fName"))
)

last_name = wait.until(
    EC.presence_of_element_located((By.NAME, "lName"))
)

email_name = wait.until(
    EC.presence_of_element_located((By.NAME, "email"))
)
submit = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
)

first_name.send_keys("kenzie")
last_name.send_keys("harsanto")
email_name.send_keys("kenzieharsanto123@gmail.com")

submit.click()

input("Press Enter to exit...")