from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

URL = 'https://en.wikipedia.org/wiki/Main_Page'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# wiki_count = WebDriverWait(driver, 10).until(
#     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#mp-welcomecount #articlecount ul li a"))
# )

# all_portals = WebDriverWait(driver, 10).until(
#     EC.presence_of_all_elements_located((By.LINK_TEXT, "Content portals"))
# )

# all_portals[0].click()

# print(wiki_count[0].text)

# wait until input is clickable
search = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "search"))
)

search.send_keys("Python (programming language)")
search.send_keys(Keys.ENTER)

input("Press Enter to exit...")