STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "stock api key"
NEWS_API_KEY = "news api kkey"
TWILIO_SID = "twilio sid"
TWILIO_AUTH_TOKEN = "twilio token"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_param = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

respose = requests.get(STOCK_ENDPOINT, params=stock_param)
data = respose.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']
print(day_before_yesterday_closing_price)

diff = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(diff)

diff_percent = (diff/float(yesterday_closing_price))*100
print(diff_percent)

news_param = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}


if diff_percent > 3:
    respose1 = requests.get(NEWS_ENDPOINT, params=news_param)
    article = respose1.json()["articles"]

    three_article = article[:3]
    print(three_article)

    formatted_article = [f"Headline: {article['title']}. \nBreif: {article ['description']}" for article in three_article]
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_article:
        message = client.messages.create(
            body = article,
            from_ = "twilio number",
            to = "personal phone number"
        )




