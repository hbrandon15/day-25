
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

data = pandas.read_csv("weather_data.csv")
temp_list = (data["temp"]).to_list()

# avg_temp = round(sum(temp_list) / len(temp_list))
# print(avg_temp)

# Using pandas methods
print (round(data["temp"].mean()))
print (f'{data["temp"].max()} is the max temperature')

# Get data in columns
print(data["condition"])
print(data.condition)


