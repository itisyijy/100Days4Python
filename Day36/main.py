# Day36 for 100Days4Python
# Project for Day36 : Stock News Monitoring

from datetime import *
import requests
from twilio.rest import Client

STOCK = "TSLA"
ALPHA_VANTAGE_KEY = "KEY"

COMPANY_NAME = "Tesla"
NEWS_KEY = "KEY"

TWILIO_SID = "KEY"
TWILIO_TOKEN = "KEY"

ytd = date.today() - timedelta(1)
dby = date.today() - timedelta(2)

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
    news_top3 = []
    for article in news_data["articles"]:
        if article["author"]:
            news_top3.append(article)
            if len(news_top3) > 3:
                break
    articles = [f"Headline: {article['title']}\nBrief: {article['description']}" for article in news_top3]
    
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    if ytd_close > dby_close:
        fluctuation_rate = f"📈{abs((ytd_close - dby_close) / dby_close * 100):.2f}%"
    else:
        fluctuation_rate = f"📉{abs((ytd_close - dby_close) / dby_close * 100):.2f}%"
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        to='whatsapp:+NUM',
        body=f"{STOCK}: {fluctuation_rate}\n{articles[0]}\n\n{articles[1]}\n\n{articles[2]}"
    )
    print(message.body)