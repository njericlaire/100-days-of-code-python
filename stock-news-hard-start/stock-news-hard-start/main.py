import requests

STOCK = "IBM"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

#STOCK_API="BLIRQS4WFYSLH0N9"
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






## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator


if perc>1:
    parameter2 = {
        #'apiKey': 'eeef6001cf314d7ba80e1a91cf4bf57b',
        'q': 'Apple'
    }

    response = requests.get(NEWS_ENDPOINT,params=parameter2)

    print (response.json)

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



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

