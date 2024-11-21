from http.client import responses
from twilio.rest import Client

import requests
My_long=51.759048
My_lat=19.725078
api_key=""
account_sid = 'AC19ca0c76305cd936462d20789e1e650b'
auth_token = ""




parameter={
    "lat":My_lat,
    "lon":My_long,
    "appid":api_key,
    "cnt":4,

}
response=requests.get("https://api.openweathermap.org/data/2.5/forecast",params=parameter)
response.raise_for_status()
print(response.status_code)
data=response.json()
for i in range(0,1):
    if data["list"][i]["weather"][0]["id"]<800:
        print("Bring an umbrella")
    else:
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body="It is going to rain carry an umbrella",
            from_='+15633629805',
            to='VERIFIED NUMBER'
        )
        print(message.sid)
print(data)
