import requests
from pprint import pprint
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self,endpoint):
        self.endpoint=endpoint
    def get(self):
        self.response=requests.get(url=self.endpoint)
        return self.response.json()


