# Day25 for 100Days4Python
# Day25 : Working with CSV File & Pandas for Data Analyzing

import pandas

# make new dataframe about fur color count and convert it .csv file
data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray_count, red_count, black_count],
}

dataframe = pandas.DataFrame(data_dict)
dataframe.to_csv("./squirrel_count.csv")
