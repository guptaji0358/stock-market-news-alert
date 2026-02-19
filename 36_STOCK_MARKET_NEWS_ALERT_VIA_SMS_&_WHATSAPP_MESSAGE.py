"""
⚠️ WARNING ⚠️
Before running this program, replace all ENTER_YOUR_... values
with your actual API keys and credentials.

This version is safe for GitHub upload.
"""

#Project - Stock Market News Alert via SMS and WhatsApp 
#------------------------------------------------------

import requests
from twilio.rest import Client

# ------------------- API KEYS -------------------

STOCK_API_KEY = "ENTER_YOUR_ALPHA_VANTAGE_API_KEY"
NEWS_API_KEY = "ENTER_YOUR_NEWS_API_KEY"

ACCOUNT_SID = "ENTER_YOUR_TWILIO_ACCOUNT_SID"
AUTH_TOKEN = "ENTER_YOUR_TWILIO_AUTH_TOKEN"

Twilio_SMS_No = "ENTER_YOUR_TWILIO_PHONE_NUMBER"
User_Phone_Number = "ENTER_YOUR_VERIFIED_PHONE_NUMBER"

client = Client(ACCOUNT_SID, AUTH_TOKEN)

STOCK_ENDPOINT_URL = "https://www.alphavantage.co/query"
NEWS_ENDPOINT_URL = "https://newsapi.org/v2/everything"

# ------------------- STEP 1: USER INPUT -------------------

user_input = input("Enter stock name (example: Tesla, Gold, Apple): ")

# ------------------- STEP 2: SEARCH SYMBOL -------------------

search_params = {
    "function": "SYMBOL_SEARCH",
    "keywords": user_input,
    "apikey": STOCK_API_KEY
}

search_response = requests.get(STOCK_ENDPOINT_URL, params=search_params)
search_data = search_response.json()

if "bestMatches" not in search_data or not search_data["bestMatches"]:
    print("❌ Stock not found or API limit reached.")
    print(search_data)
    exit()

best_match = search_data["bestMatches"][0]

STOCK_NAME = best_match["1. symbol"]
COMPANY_NAME = best_match["2. name"]

print(f"✅ Found: {STOCK_NAME} - {COMPANY_NAME}")

# ------------------- STEP 3: GET STOCK DATA -------------------

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

stock_response = requests.get(STOCK_ENDPOINT_URL, params=stock_params)
stock_json = stock_response.json()

if "Time Series (Daily)" not in stock_json:
    print("⚠️ Could not fetch stock data.")
    print(stock_json)
    exit()

stock_data = stock_json["Time Series (Daily)"]
stock_list = list(stock_data.values())

yesterday_price = float(stock_list[0]["4. close"])
day_before_price = float(stock_list[1]["4. close"])

difference = yesterday_price - day_before_price

if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percentage_difference = round(abs(difference) / day_before_price * 100)

print(f"{STOCK_NAME} moved {percentage_difference}%")

# ------------------- STEP 4: CHECK 5% CONDITION -------------------

if percentage_difference > 5:

    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
        "language": "en"
    }

    news_response = requests.get(NEWS_ENDPOINT_URL, params=news_params)
    news_json = news_response.json()

    if "articles" not in news_json:
        print("⚠️ Could not fetch news.")
        print(news_json)
        exit()

    articles = news_json["articles"][:3]

    for article in articles:
        message_body = (
            f"{STOCK_NAME}: {up_down}{percentage_difference}%\n"
            f"Headline: {article.get('title')}\n"
            f"Brief: {article.get('description', 'No description available')}"
        )

        # SMS
        client.messages.create(
            body=message_body,
            from_=Twilio_SMS_No,
            to=User_Phone_Number
        )

        # WhatsApp (Twilio Sandbox)
        client.messages.create(
            body=message_body,
            from_="whatsapp:+14155238886",
            to="whatsapp:ENTER_YOUR_VERIFIED_WHATSAPP_NUMBER"
        )

        print("✅ Message Sent (SMS + WhatsApp)")

else:
    print("ℹ️ Movement less than 5%. No news sent.")
