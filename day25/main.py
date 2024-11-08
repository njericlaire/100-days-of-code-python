# # with open("weather_data.csv") as weather:
# #     data=weather.readlines()
# #     print(data)
# # import csv
# # with open("weather_data.csv") as weather:
# #     data=csv.reader(weather)
# #     temp=[]
# #     for row in data:
# #         if row[1]!="temp":
# #             temp.append(int(row[1]))
# #     print(temp)
# from traceback import print_tb
#
import pandas
from pandas.core.interchange.dataframe_protocol import DataFrame

# from numpy.ma.extras import average
#
# data = pandas.read_csv("weather_data.csv")
# # data_dict=data.to_dict()
# # print(data_dict)
#
# temp_list=data["temp"].to_list()
# # print(temp_list)
# # aver=sum(temp_list)/len(temp_list)
# # print(aver)
# print(data["temp"].mean())
# print(data['temp'].max())
# #gettinf data for row
# print(data[data.day=="Monday"])
# print(data[data.temp==data["temp"].max()])
# monday=data[data.day=="Monday"]
# print(monday.condition)
# print(monday.temp*9/5 +32)
# #Create a dataframe from scratch
# data_dict={
#     "students":["Claire","James","Angela"],
#     "scores":[25,78,26]
# }
# data_st=pandas.DataFrame(data_dict)
# print(data_st)
# data_st.to_csv("new_data.csv")
data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color=data["Primary Fur Color"]
black=len(data[color=="Black"])
gray=len(data[color=="Gray"])
cinnamon=len(data[color=="Cinnamon"])

data_dict={
    "Fur Colour":["Gray","Cinnamon","Black"],
    "Count":[gray,cinnamon,black]
}
data_colour=pandas.DataFrame(data_dict)
data_colour.to_csv("DataColor.csv")