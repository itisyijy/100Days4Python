# Day09 for 100Days4Python
# Nesting

travel_log = {
    "Italia": {
        "num_of_visiting": 1,
        "visited_city": ["Roma", "Venezia", "Firenze"]},
    "France": {
        "num_of_visiting": 2,
        "visited_city": ["Paris"],
    },
    "United Kingdom": {
        "num_of_visiting": 1,
        "visited_city": ["London", "Newcastle", "Edinburgh"],
    },
}

# Access Nested Item
print(travel_log["Italia"]["visited_city"][0])
print("1-------------------------------")

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])
print("2-------------------------------")