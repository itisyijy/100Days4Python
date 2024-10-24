# Day26 for 100Days4Python
# Day26 : List Comprehension -> only available in python

numbers = [1, 2, 3]
new_numbers = []
for n in numbers:
    add_1 = n + 1
    new_numbers.append(add_1)
print(new_numbers)  # [2, 3, 4]

# List Comprehension : Create new list from previous list
# Pattern : new_list = [new_item for item in list]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)  # [2, 3, 4]

# Sequence : list, range, string, tuple
text = "Kulusevski"
text_list = [letter for letter in text]
print(text_list)    # ['K', 'u', 'l', 'u', 's', 'e', 'v', 's', 'k', 'i']

range_list = [i * 2 for i in range(1, 5)]
print(range_list)  # [2, 4, 6, 8]

# Conditional List Comprehension
# Pattern : new_list = [new item for item in list if condition]
names = ['Li', 'Mia', 'Zoe', 'Finn', 'Yara', 'Jonathan', 'Alexander', 'Elizabeth', 'Gabrielle', 'Christopher']
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]
print(short_names)  # ['Li', 'Mia', 'Zoe', 'Finn', 'Yara']
print(long_names)   # ['JONATHAN', 'ALEXANDER', 'ELIZABETH', 'GABRIELLE', 'CHRISTOPHER']
