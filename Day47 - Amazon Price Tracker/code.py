import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")

# print(EMAIL, PASSWORD)

URL = 'https://appbrewery.github.io/instant_pot/'

def get_prices():
    print("Fetching price from Amazon...")
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    center_div = soup.find_all('div', id = 'apex_desktop')
    prices_element = center_div[0].select('span.aok-offscreen')

    # print(type(center_div))
    for price in prices_element:
        priyce = price.get_text()
    # print(prices_element.split())
    print(priyce)
    return float(priyce.replace('$', ''))

def send_email(price):
    import smtplib

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Price Alert!\n\nThe price has dropped to {price}!"
        )

def main():
    price = get_prices()
    print(price)
    if price < 100:
        print("Price is low! Sending email...")
        send_email(price)

# print(type(get_prices()), get_prices())

if __name__ == "__main__":
    main()