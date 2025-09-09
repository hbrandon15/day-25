# with open("weather_data.csv") as data:
#     weather = data.readlines()
#     print(weather)
#

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
temp_list = (data["temp"]).to_list()

# avg_temp = round(sum(temp_list) / len(temp_list))
# print(avg_temp)

print (round(data["temp"].mean()))

