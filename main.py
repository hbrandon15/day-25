
# # # Read the data from a file
# # # Method 1
# with open("weather_data.csv") as data:
#     weather = data.readlines()
#     print(weather)
#
# # Method 2
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# # Method 3
import pandas

# data = pandas.read_csv("weather_data.csv")
# temp_list = (data["temp"]).to_list()
#
# # avg_temp = round(sum(temp_list) / len(temp_list))
# # print(avg_temp)
#
# # Using pandas methods
# print (round(data["temp"].mean()))
# print (f'{data["temp"].max()} is the max temperature')
#
# # Get data in columns
# print(data["condition"])
# print(data.condition)


# # Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
#
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data2 = pandas.DataFrame(data_dict)
# data2.to_csv("new_data.csv")
# print(data2)


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# print(len(data[data['Primary Fur Color'] == 'Gray']))
# print(len(data[data['Primary Fur Color'] == 'Cinnamon']))
# print(len(data[data['Primary Fur Color'] == 'Black']))

squirrel_count = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(data[data['Primary Fur Color'] == 'Gray']),
              len(data[data['Primary Fur Color'] == 'Cinnamon']),
              len(data[data['Primary Fur Color'] == 'Black'])]
    }

data2 = pandas.DataFrame(squirrel_count)
print(data2)

