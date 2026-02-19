# stock-market-news-alert
DAY - 36 - Project - python X stock market news alert

# 📈 Stock Market News Alert System

An automated stock monitoring system built using Python.

This project:

- Accepts stock name from user (Tesla, Gold, Apple, etc.)
- Automatically finds the correct stock symbol
- Calculates daily percentage movement
- If movement is greater than 5%
- Fetches top 3 related news articles
- Sends SMS + WhatsApp alerts using Twilio

---

## 🚀 Features

- 🔍 Automatic Stock Symbol Search  
- 📊 Daily Percentage Movement Calculation  
- 📰 Top 3 News Headlines  
- 📱 SMS Alerts  
- 💬 WhatsApp Alerts  
- 🛡 API Error Handling  

---

## 🛠 Technologies Used

- Python  
- Alpha Vantage API  
- NewsAPI  
- Twilio API  
- Requests library  

---

# 🔑 How to Get API Keys

You need 3 services:

1. Alpha Vantage (Stock Data)
2. NewsAPI (News Articles)
3. Twilio (SMS & WhatsApp)

---

## 1️⃣ Alpha Vantage API Key

1. Go to: https://www.alphavantage.co  
2. Click **Get Free API Key**  
3. Create an account  
4. Copy your API key  

Free Plan Limits:

- 5 requests per minute  
- 25 requests per day  

Add inside your Python file:

```python
STOCK_API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
```

---

## 2️⃣ NewsAPI Key

1. Go to: https://newsapi.org  
2. Click **Get API Key**  
3. Create a free account  
4. Copy your API key  

Add inside your Python file:

```python
NEWS_API_KEY = "YOUR_NEWS_API_KEY"
```

---

## 3️⃣ Twilio Setup (SMS + WhatsApp)

1. Go to: https://www.twilio.com  
2. Create a free account  
3. Verify your phone number  
4. From Dashboard copy:
   - Account SID  
   - Auth Token  
5. Get your Twilio phone number  

Add inside your Python file:

```python
ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"
AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
Twilio_SMS_No = "YOUR_TWILIO_PHONE_NUMBER"
User_Phone_Number = "YOUR_VERIFIED_PHONE_NUMBER"
```

---

## ▶️ How To Run The Project

### Step 1: Install dependencies

```bash
pip install requests twilio
```

### Step 2: Add your API keys inside the Python file

### Step 3: Run the script

```bash
python 36_STOCK_MARKET_NEWS_ALERT.py
```

---

## 📌 Example Output

```
Enter stock name: Tesla
Found: TSLA - Tesla Inc
TSLA moved 7%
Message Sent
```

---

## ⚠️ Important Notes

- Do NOT upload real API keys to GitHub.
- Replace them with placeholder values before pushing.
- Alpha Vantage has strict free API limits.

---

# 👨‍💻 Author

Robin Gupta  
100 Days of Code – Day 36
