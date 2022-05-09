# Personal details have been omitted. Environment variables can be used instead.
import requests
from twilio.rest import Client

# Constants
# Stocks constants
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_STOCKS = "API_KEY_STOCKS"
API_KEY_NEWS = "API_KEY_NEWS"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": API_KEY_STOCKS,
}
# News constants
NEWS_PARAMETERS = {
    "apiKey": API_KEY_NEWS,
    "q": COMPANY_NAME,
}
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = "account_sid"
auth_token = "auth_token"

# Twilio details
VIRTUAL_TWILIO_NUMBER = "VIRTUAL_TWILIO_NUMBER"
VERIFIED_NUMBER = "MY_NUM"

# yesterday's closing stock price
stocks_url = "https://www.alphavantage.co/query"
response_stocks = requests.get(stocks_url, params=STOCK_PARAMETERS)
data_stocks = response_stocks.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data_stocks.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

# the day before yesterday's closing stock price
day_before_yesterday_closing_price = data_list[1]["4. close"]
print(day_before_yesterday_closing_price)

# Find the positive difference between 1 and 2
closing_difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if closing_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

absolute_closing_difference = abs(closing_difference)
print(f"{absolute_closing_difference} - absolute closing difference")

# percentage difference in price between closing price yesterday and closing price the day before yesterday
percentage_difference = round((absolute_closing_difference / float(yesterday_closing_price)) * 100)
print(f"{percentage_difference} percentage_difference")

# STEP 2: using https://newsapi.org/
response_news = requests.get("https://newsapi.org/v2/everything", params=NEWS_PARAMETERS)
articles = response_news.json()["articles"]

# create a list that contains the first 3 articles
top_articles = articles[:3]

# STEP 3: using twilio.com to send a separate message with each article's title and description to your phone number

# a new list of the first 3 articles headline and description
top_news_titles = [item["title"] for item in top_articles]
top_news_descriptions = [item["description"] for item in top_articles]
top_news_pair = {top_news_titles[i]: top_news_descriptions[i] for i in range(len(top_news_titles))}

# Send each article as a separate message via Twilio
client = Client(account_sid, auth_token)
for title, description in top_news_pair.items():
    message = client.messages \
        .create(
            body=f"\n{STOCK_NAME}: {up_down}{percentage_difference:.02f}%\n"
                 f"Headline: {title}\n"
                 f"Brief: {description}",
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )