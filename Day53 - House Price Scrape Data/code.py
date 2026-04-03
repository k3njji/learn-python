from bs4 import BeautifulSoup
import requests
import re

from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ZILLA_URL = 'https://appbrewery.github.io/Zillow-Clone/'
FORM_URL = 'https://docs.google.com/forms/d/e/1FAIpQLScO7Q5t8Mq0q4q2XDnDNchN2jV8T4iloBx48EmJ10YT0oRV4g/viewform'


# ---------- CLEANING ----------
def clean_text(text):
    return " ".join(text.split())


def extract_price(text):
    match = re.search(r"\$([\d,]+)", text)
    return int(match.group(1).replace(",", "")) if match else None


# ---------- SCRAPING ----------
def get_stats():
    response = requests.get(ZILLA_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    prices_raw = soup.find_all('span', attrs={"data-test": "property-card-price"})
    addresses_raw = soup.find_all('address', attrs={"data-test": "property-card-addr"})
    links_raw = soup.find_all('a', attrs={"data-test": "property-card-link"})

    data = []

    for p, a, l in zip(prices_raw, addresses_raw, links_raw):
        data.append({
            "address": clean_text(a.get_text()),
            "price": extract_price(p.get_text()),
            "link": l['href'].strip()
        })

    return data


# ---------- FORM FILLING ----------
def filling_form(data):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    driver.get(FORM_URL)

    for item in data:
        # Wait for visible input fields (better selector)
        inputs = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "div[role='listitem'] input")
            )
        )

        values = [
            item["address"],
            str(item["price"]),
            item["link"]
        ]

        for i in range(3):
            field = inputs[i]
            wait.until(EC.element_to_be_clickable(field))
            field.click()
            field.clear()
            field.send_keys(values[i])

        submit_btn = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div[role='button'][aria-label='Submit']")
            )
        )
        submit_btn.click()

        another = wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Kirim jawaban lain")
            )
        )
        another.click()


# ---------- MAIN ----------
if __name__ == "__main__":
    data = get_stats()
    filling_form(data)