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
print("-------------------------------")

# Add New Item On Dictionary
capital["China"] = "Beijing"
print(capital)
print("-------------------------------")


# Edit Item In Dictionary
capital["Korea"] = "Busan"
print(capital["Korea"])
print("-------------------------------")

# For Loop with Dictionary
for key in capital:
    print(key)
    print(capital[key])
print("-------------------------------")

# Wipe All Items In Dictionary
capital = {}
print(capital)
print("-------------------------------")

# Nesting

