from selenium import webdriver
from selenium.webdriver.common.by import By
from time import time, sleep


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://orteil.dashnet.org/cookieclicker/")

# Maximize the window size so that it shows the hidden options
driver.maximize_window()

# Wait for the page to load
sleep(2)


change_language = driver.find_element(By.ID, value="changeLanguage")
change_language.click()

# Close the language prompt popup
exit_language = driver.find_element(By.ID, value="promptClose")
exit_language.click()

# Prepare list of product IDs (20 product items)
products_list = [f"product{i}" for i in range(20)]

cookie_button = driver.find_element(By.ID, value="bigCookie")

# Initialize the timer for checking upgrades
last_check_time = time()

while True:
    current_time = time()
    
    # Click the cookie continuously
    cookie_button.click()
    
    # Every 15 seconds, check for upgrades
    if (current_time - last_check_time) >= 15:
        cookie_button.click()  # Ensure enough cookies before purchase
        last_check_time = current_time
        
        # Check products from most expensive to least
        for product in reversed(products_list):
            try:
                best_product = driver.find_element(By.ID, value=product)
                
                # Get class attribute to check if the product is clickable
                element_class = best_product.get_attribute("class").split()[2]
            except:
                # If element not found or has no such class, continue clicking
                cookie_button.click()
            else:
                # If the product is enabled, purchase it
                if element_class == "enabled":
                    best_product.click()
                    break  # Buy only the most expensive available one