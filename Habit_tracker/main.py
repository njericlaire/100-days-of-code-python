import requests
from datetime import datetime

USER_NAME="clairemwangi"
USER_TOKEN="claire1234"


pixela_endpoint="https://pixe.la/v1/users"
user_params={
"token":USER_TOKEN,
"username":USER_NAME,
"agreeTermsOfService":"yes",
"notMinor":"yes"
}
# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
graph_endpoint=f"{pixela_endpoint}/{USER_NAME}/graphs"
graph_config={
    "id":"graph1",
    "name":"Walking Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"

}

headers={
    "X-USER-TOKEN":USER_TOKEN
}

pixel_endpoint=f"{pixela_endpoint}/{USER_NAME}/graphs/graph1"
today=datetime.now()
print(today.strftime("%Y%m%d"))
pixel_config={
    "date":today.strftime("%Y%m%d"),
    "quantity":"2.3"
}

response=requests.post(url=pixel_endpoint, json=pixel_config,headers=headers)
print(response.text)