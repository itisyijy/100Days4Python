# Day36 for 100Days4Python
# Project for Day36 : Stock News Monitoring

import datetime
import requests

STOCK = "TSLA"
ALPHA_VANTAGE_KEY = ""

COMPANY_NAME = "Tesla"
NEWS_KEY = ""

TWILIO_SID = ""
TWILIO_TOKEN = ""

ytd = datetime.date.today() - datetime.timedelta(2) # 1
dby = datetime.date.today() - datetime.timedelta(3) # 2

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_VANTAGE_KEY,
}
stock = requests.get(url="https://www.alphavantage.co/query?", params=stock_params)
stock_data = stock.json()
ytd_close = float(stock_data["Time Series (Daily)"][f"{ytd}"]["4. close"])
dby_close = float(stock_data["Time Series (Daily)"][f"{dby}"]["4. close"])
print(ytd_close, dby_close)

if ytd_close >= dby_close * 1.05 or ytd_close <= dby_close * 0.95:
    news_params = {
        "apiKey": NEWS_KEY,
        "q": COMPANY_NAME,
    }
    news = requests.get(url="https://newsapi.org/v2/everything?", params=news_params)
    news_data = news.json()
    news_top3 = news_data["articles"][:3]
    print(news_top3)
    


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
