#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
data=DataManager("")

sheet_data=data.get()
sheet_data=sheet_data['prices']
print(sheet_data)