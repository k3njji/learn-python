import os
import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = os.getenv("STOCK_API")
NEWS_API_KEY = os.getenv("NEWS_API")

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# -------------------- STEP 1: GET STOCK DATA --------------------

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

stock_res = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_res.raise_for_status()
stock_data = stock_res.json()["Time Series (Daily)"]
daily_prices = list(stock_data.values())[:2]

yesterday_close = float(daily_prices[0]["4. close"])
day_before_close = float(daily_prices[1]["4. close"])

price_change_percent = abs(yesterday_close - day_before_close) / day_before_close * 100

symbol = "🔺" if yesterday_close > day_before_close else "🔻"

print(f"Price change: {price_change_percent:.2f}%")

# -------------------- STEP 2: GET NEWS --------------------

if price_change_percent >= 5:

    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "sortBy": "popularity",
        "pageSize": 3
    }

    news_res = requests.get(NEWS_ENDPOINT, params=news_params)
    news_res.raise_for_status()

    articles = news_res.json()["articles"]

    # -------------------- STEP 3: SEND WHATSAPP --------------------

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for article in articles:

        headline = article["title"]
        brief = article["description"]

        body = f"""
{STOCK}: {symbol}{price_change_percent:.2f}%

Headline: {headline}

Brief: {brief}
"""

        message = client.messages.create(
            from_="whatsapp:+14155238886",
            body=body,
            to="whatsapp:+6287776161712"
        )

        print("Message sent!")