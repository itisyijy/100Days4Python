# Day9 for 100Days4Python
# Dictionaries : {KEY : VALUE}

capital = {
    "Korea": "Seoul",
    "Japan": "Tokyo",
    "USA": "Washington D.C.",
    "France": "Paris",
    "Germany": "Berlin",
}
# Call Value By Key
print(capital["Japan"])
print("1-------------------------------")

# Add New Item On Dictionary
capital["China"] = "Beijing"
print(capital)
print("2-------------------------------")


# Edit Item In Dictionary
capital["Korea"] = "Busan"
print(capital["Korea"])
print("3-------------------------------")

# For Loop with Dictionary
for key in capital:
    print(key)
    print(capital[key])
print("4-------------------------------")

# Wipe All Items In Dictionary
capital = {}
print(capital)
print("5-------------------------------")

