# Day25 for 100Days4Python
# Day25 : Working with CSV File & Pandas for Data Analyzing

import pandas

data = pandas.read_csv("./weather_data.csv")

print("\n# DataFrame(2D) in pandas")
print("------------------------------")
data_dict = data.to_dict()
print(data)
print(data_dict)

print("\n# Series(1D) in pandas")
print("------------------------------")
temp = data["temp"].to_list()
print(temp)

print("\n# Get mean value in \"temp\" column")
print("------------------------------")
print(sum(temp) / len(temp))
print(data["temp"].mean())

print("\n#  Get max value in \"temp\" column")
print("------------------------------")
print(data["temp"].max())

print("\n# Get data in columns")
print("------------------------------")
print(data["condition"])    # like dictionary
print(data.condition)       # like object

print("\n# Get data in rows")
print("------------------------------")
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

print("\n# Convert Monday's temperature to Fahrenheit")
print("------------------------------")
monday = data[data.day == "Monday"]
print(monday.temp)
print(monday.temp * (9 / 5) + 32)

print("\n# Create a DataFrame from scratch")
print("------------------------------")
result = {
    "students": ["Pedro", "James", "Micky"],
    "scores": [76, 56, 65],
}
result_pandas = pandas.DataFrame(result)
print(result_pandas)
result_pandas.to_csv("./result.csv")    # make DataFrame .csv file
