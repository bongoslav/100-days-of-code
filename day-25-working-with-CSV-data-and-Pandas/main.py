import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))  # pandas DataFrame object
# print(data["temp"])  # pandas series object (every column is a series obj)
#
# data_dict = data.to_dict()  # convert to a dictionary
# print(data_dict)
#
# average_temp = data["temp"].mean()  # the average value
# print(average_temp)
#
# max_temp = data["temp"].max()  # the max value
# print(max_temp)
#
# print(data.condition)  # = data["condition"]


# # Get Data in row
# print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# print(monday_temp*9/5 + 32)


# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65],
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


# # Project: Count the squirrels by their primary fur colors
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count],
# }
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")