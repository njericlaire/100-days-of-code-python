import requests

STOCK = "IBM"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API="BLIRQS4WFYSLH0N9"
parameter={
"function":"TIME_SERIES_DAILY",
"symbol":STOCK,
"apikey":STOCK_API

}


## STEP 1: Use https://newsapi.org/docs/endpoints/everything

r = requests.get(STOCK_ENDPOINT,params=parameter)
data = r.json()["Time Series (Daily)"]
data_list=[value for key,value in data.items()]
diff=abs(float(data_list[1]['4. close'])-float(data_list[0]['4. close']))
perc=(diff/float(data_list[0]['4. close']))*100
up_down = None
if diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"



if perc>1:
    parameter2 = {
        'apiKey': 'eeef6001cf314d7ba80e1a91cf4bf57b',
        'q': COMPANY_NAME
    }

    response = requests.get(NEWS_ENDPOINT,params=parameter2)

    articles=response.json()["articles"]
    three_articles=articles[:3]
    print(three_articles)
    formatted_articles = [f"{STOCK}: {up_down}{perc}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for
        article in three_articles]
    print(formatted_articles)



"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

