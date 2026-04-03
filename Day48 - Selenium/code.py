from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# keeping the chroms open

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.tokopedia.com/philips-estore/baru-philips-airfryer-low-watt-500w-transparan-best-compact-size-3-2l-na210-00-air-fryer-multifungsi-digital-layar-sentuh-air-fryer-1730662955767465974?t_id=1773999056085&t_st=1&t_pp=homepage&t_efo=pure_goods_card&t_ef=homepage&t_sm=rec_homepage_outer_flow&t_spt=homepage')

# price = WebDriverWait(driver, 10).until(lambda d: d.find_element(By.CLASS_NAME, 'price'))
price = driver.find_element(By.CLASS_NAME, 'price')  # this is not recommended, because it can cause an error if the element is not found immediately
print(price.text)

driver.close()
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Deprecated - no longer needed
chrome_driver_path = "/Users/philippmuellauer/Development/chromedriver"

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chrome_options)

def test_eight_components():
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    title = driver.title
    assert title == "Web form"
    driver.implicitly_wait(0.5)
    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    text_box.send_keys("Selenium")
    submit_button.click()
    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"

    # Closes Chrome
    # driver.quit()
    driver.close()


test_eight_components()
