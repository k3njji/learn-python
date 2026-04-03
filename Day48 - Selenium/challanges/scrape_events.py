from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://www.python.org/'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

events_date = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".event-widget .menu li time"))
)

events_title = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".event-widget .menu li a"))
)

dict = {}

for i in range(len(events_date)):
    date = events_date[i].text
    title = events_title[i].text
    print(f"{date} - {title}")

    temp = {
        i: {
            "date": date,
            "title": title
        }
    }

    dict.update(temp)

print(dict)

input("Press Enter to exit...")