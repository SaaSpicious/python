import datetime
import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_NEWS_DELTA = 1

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

def get_yesterdays_date():
    now = datetime.date.today() - datetime.timedelta(1)
    return now.strftime('%Y-%m-%d')

def get_stocks(date,stock_api_key):
    stock_api_key_params = {
        "apikey": stock_api_key,
        "function": 'TIME_SERIES_DAILY',
        "symbol": STOCK,
    }
    stock_api_request = requests.get(url=STOCK_ENDPOINT,params=stock_api_key_params)
    return stock_api_request.json()["Time Series (Daily)"][date]

def get_difference(stock_info):
    stock_open = float(stock_info["1. open"])
    stock_close = float(stock_info["4. close"])
    diff_percent = round((stock_close - stock_open) / stock_open * 100,4)
    return diff_percent

def get_news(date,news_api_key):
    news_api_key_params = {
        "apikey": news_api_key,
        "q": COMPANY_NAME,
        "from": date,
    }
    print (news_api_key_params)
    news_api_request = requests.get(url=NEWS_ENDPOINT, params=news_api_key_params)
    print(news_api_request.status_code)
    return news_api_request.json()["articles"]


def get_api_keys():
    api_keys = {}
    file = open("API_KEYS","r")
    lines = file.readlines()
    for line in lines:
        list = line.split("=")
        key = list[0].strip()
        value = list[1].strip()
        api_keys[key]=value
    return api_keys

api_keys=get_api_keys()
print(api_keys)

stock_difference = get_difference(get_stocks(get_yesterdays_date(),api_keys["STOCK_API_KEY"]))

print(f"The stock {COMPANY_NAME} changed by {stock_difference}% since yesterday!")
if abs(stock_difference) > STOCK_NEWS_DELTA:
    print("Here's some news that might be related to this:")
    for article in get_news(get_yesterdays_date(),api_keys["NEWS_API_KEY"]):
        print(f"According to {article["source"]["name"]}:")
        print(f"{article["title"]}\n")



