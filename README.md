# stock-market-news-alert
DAY - 36 - Project - python X stock market news alert

# 📈 36_STOCK_MARKET_NEWS_ALERT

An automated Stock Market News Alert System built with Python.

This program:
- Accepts stock name from user (e.g., Tesla, Gold, Apple)
- Automatically finds the correct stock symbol
- Calculates daily percentage movement
- If movement is greater than 5%
- Fetches top 3 related news articles
- Sends SMS + WhatsApp alerts using Twilio

---

## 🚀 Features

- 🔍 Auto Stock Symbol Search
- 📊 Daily Stock Movement Calculation
- 📰 News Fetching (Top 3 Headlines)
- 📱 SMS Alerts (Twilio)
- 💬 WhatsApp Alerts (Twilio Sandbox)
- 🛡 Error Handling for API Limits

---

## 🛠 Technologies Used

- Python
- Alpha Vantage API
- NewsAPI
- Twilio SMS & WhatsApp API
- Requests library

---

# 🔑 How To Get Required API Keys

You need 3 services:

1. Alpha Vantage (Stock Data)
2. NewsAPI (News Articles)
3. Twilio (SMS & WhatsApp)

---

## 1️⃣ Alpha Vantage API Key (Stock Data)

1. Go to: https://www.alphavantage.co/
2. Click **Get Free API Key**
3. Create a free account
4. Copy your API key

Free Plan Limits:
- 5 requests per minute
- 25 requests per day

Add it inside your Python file:

```python
STOCK_API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"
2️⃣ NewsAPI Key (News Data)
Go to: https://newsapi.org/

Click Get API Key

Create a free account

Copy your API key

Free plan is enough for this project.

Add it inside your Python file:

NEWS_API_KEY = "YOUR_NEWS_API_KEY"
3️⃣ Twilio (SMS + WhatsApp)
Go to: https://www.twilio.com/

Create a free account

Verify your phone number

Go to Dashboard

Copy:

Account SID

Auth Token

Get your Twilio phone number

Add inside your Python file:

ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"
AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
Twilio_SMS_No = "YOUR_TWILIO_PHONE_NUMBER"
User_Phone_Number = "YOUR_VERIFIED_PHONE_NUMBER"
WhatsApp Setup (Twilio Sandbox)
In Twilio Console → Messaging → Try it out → Send a WhatsApp message

Join the sandbox using the given code

Use:

from_="whatsapp:+14155238886"
to="whatsapp:YOUR_VERIFIED_NUMBER"
▶️ How To Run The Project
Install dependencies:

pip install requests twilio
Add your API keys inside the script.

Run:

python 36_STOCK_MARKET_NEWS_ALERT.py
Enter stock name:

Tesla
Gold
Apple
📌 Example Output
Enter stock name: Tesla
✅ Found: TSLA - Tesla Inc
TSLA moved 7%
✅ Message Sent (SMS + WhatsApp)
⚠️ Important Notes
Alpha Vantage free API has strict limits.

If limit is exceeded, wait 1 minute or 24 hours.

Do NOT upload real API keys to GitHub.

Replace keys with placeholders before pushing.

👨‍💻 Author
Robin Gupta
100 Days of Code – Day 36

⭐ If You Like This Project
Give it a star ⭐ on GitHub!


---

# 🔥 This README Is

✔ Clean  
✔ Professional  
✔ Beginner friendly  
✔ Explains APIs clearly  
✔ Portfolio ready  

---

If you want, I can now:

- 🔥 Create LinkedIn post  
- 🔥 Create X (Twitter) post  
- 🔥 Improve project description  
- 🔥 Suggest GitHub repo name  

Your move, developer 😎

You said:
no tis not in good format in starting its look llike .ipynb file and whebn scroll down its look like txt

ChatGPT said:
Ahhh 😎 I know what happened.

Your README is probably not rendering properly because:

❌ Maybe you pasted it with wrong formatting

❌ Maybe you missed triple backticks

❌ Maybe headings are not spaced correctly

❌ Maybe no blank lines between sections

GitHub Markdown is sensitive to spacing.

Let me give you a properly formatted, clean GitHub-ready README that will render beautifully.

✅ CLEAN PROFESSIONAL README.md (Proper Markdown Format)
Copy this exactly:

# 📈 Stock Market News Alert System

An automated stock monitoring system built with Python.

This project:
- Accepts a stock name from the user (Tesla, Gold, Apple, etc.)
- Automatically finds the correct stock symbol
- Calculates daily percentage movement
- If movement is greater than 5%
- Fetches top 3 related news articles
- Sends SMS + WhatsApp alerts using Twilio


---

## 🚀 Features

- 🔍 Automatic Stock Symbol Search  
- 📊 Daily Percentage Movement Calculation  
- 📰 Top 3 News Headlines Fetching  
- 📱 SMS Notifications  
- 💬 WhatsApp Alerts  
- 🛡 API Error Handling  


---

## 🛠 Technologies Used

- Python  
- Alpha Vantage API  
- NewsAPI  
- Twilio API  
- Requests Library  


---

# 🔑 How to Get API Keys

You need 3 services:

1. Alpha Vantage (Stock Data)
2. NewsAPI (News Articles)
3. Twilio (SMS & WhatsApp)


---

## 1️⃣ Alpha Vantage API Key

1. Go to https://www.alphavantage.co  
2. Click **Get Free API Key**  
3. Create an account  
4. Copy your API key  

Free plan limits:
- 5 requests per minute  
- 25 requests per day  

Add inside your script:

STOCK_API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"



---

## 2️⃣ NewsAPI Key

1. Go to https://newsapi.org  
2. Click **Get API Key**  
3. Create an account  
4. Copy your API key  

Add inside your script:

NEWS_API_KEY = "YOUR_NEWS_API_KEY"



---

## 3️⃣ Twilio Setup (SMS + WhatsApp)

1. Go to https://www.twilio.com  
2. Create a free account  
3. Verify your phone number  
4. From Dashboard copy:
   - Account SID
   - Auth Token  
5. Get your Twilio phone number  

Add inside your script:

ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"
AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
Twilio_SMS_No = "YOUR_TWILIO_PHONE_NUMBER"
User_Phone_Number = "YOUR_VERIFIED_PHONE_NUMBER"



---

## WhatsApp Sandbox Setup

1. In Twilio Console → Messaging → Try WhatsApp  
2. Join the sandbox using the provided code  
3. Use:

from_="whatsapp:+14155238886"
to="whatsapp:YOUR_VERIFIED_NUMBER"



---

# ▶️ How To Run

### 1️⃣ Install dependencies

pip install requests twilio


### 2️⃣ Add your API keys inside the Python file

### 3️⃣ Run the program

python 36_STOCK_MARKET_NEWS_ALERT.py



---

# 📌 Example Output

Enter stock name: Tesla
Found: TSLA - Tesla Inc
TSLA moved 7%
Message Sent



---

# ⚠️ Important Notes

- Do NOT upload real API keys to GitHub.
- Replace them with placeholders before pushing.
- Alpha Vantage has strict free plan limits.


---

# 👨‍💻 Author

Robin Gupta  
100 Days of Code – Day 36

