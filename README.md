<p align="center">
<a href="https://docs.python.org/3/">
<img src="https://img.icons8.com/?size=100&id=13441&format=png&color=000000" />
</a>
<br>
<a href="https://www.udemy.com/course/100-days-of-code/">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Udemy_logo.svg/320px-Udemy_logo.svg.png" />
</a>

</p>

# [100 Days of Code - Python Exercise](https://github.com/phillipai/100-days-of-code-python)

---

## [Auditorium for Coding Exercise](https://app.auditorium.ai/courses/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6)

---

## [Day 01](https://github.com/itisyijy/100Days4Python/tree/77af9a6683768b1b0a332f67decb469c1f7db45f/Day1)

- input() & print()

---

## [Day 02](https://github.com/itisyijy/100Days4Python/tree/77af9a6683768b1b0a332f67decb469c1f7db45f/Day2)

- Date types
- Type casting
- F-string
- Numerical operators

---

## [Day 03](https://github.com/itisyijy/100Days4Python/tree/77af9a6683768b1b0a332f67decb469c1f7db45f/Day3)

- Conditional statement
- Code blocks and scope
- Comparison operators
- Modulo operator, %
- Logical operator

---

## [Day 04](https://github.com/itisyijy/100Days4Python/tree/77af9a6683768b1b0a332f67decb469c1f7db45f/Day4)

- Module
- Randomization
- List
- Python docs

---

## [Day 05](https://github.com/itisyijy/100Days4Python/tree/ea67c6d4dae9087e953cbbe50e3270ff6cc284db/Day5)

- Loop statement
- random.function

---

## [Day 06](https://github.com/itisyijy/100Days4Python/tree/d8f443d26e642ad23d9ab2f8c966deb740da9200/Day6)

- Define Function
- Code Blocks & Indentation
- While Loop
- [reeborg's world](https://reeborg.ca/index_en.html) for Practice While Loop

---

## [Day 07](https://github.com/itisyijy/100Days4Python/tree/4a3b3fed1a2178714860e965f9916343226e9035/Day7)

- hangman project
- in function
- list() function
- .append() function

---

## [Day 08](https://github.com/itisyijy/100Days4Python/tree/6cdd0724fda62e9230b456510539e8796a95d659/Day8)

- Function with multiple parameters
- difference between parameter and argument
- positional argument(default) & keyword argument
- caesar cipher

---

## [Day 09](https://github.com/itisyijy/100Days4Python/tree/6acf21357a08ed6d2c7345bb718e30650d457d15/Day9)

- Dictionary
- Nesting List & Dictionary
- Blind Auction
- max() function in dictionary

---

## [Day 10](https://github.com/itisyijy/100Days4Python/tree/6acf21357a08ed6d2c7345bb718e30650d457d15/Day9)

- return in defining function
- function name call in dictionary value

---

## [Day 11](https://github.com/itisyijy/100Days4Python/tree/805be17186470409092e39dd55e55af4ed181869/Day11)

- Capstone Design : Blackjack
- Difference : .extend() & .append()

---

## [Day 12](https://github.com/itisyijy/100Days4Python/tree/cd854aa53ad1e43de126da6b3d9e66cc1f389911/Day12)

- Scope (Global & Local)
- Constant
- Project : Number Guessing

---

## [Day 13](https://github.com/itisyijy/100Days4Python/tree/8c1fb58cdb1264008e2e4a80d9b9d823333274b8/Day13)

\*try & except

> ### Everyone gets bugs.
>
> ### Debugging Tips
>
> 1.  Describe The Problem.
> 2.  Reproduce The Bug
> 3.  Play Computer
> 4.  Fix The Error
> 5.  print() is your friend
> 6.  Use A Debugger
> 7.  Take A Rest
> 8.  Ask A Friend
> 9.  Run Often
> 10. Ask Stackoverflow

---

## [Day 14](https://github.com/itisyijy/100Days4Python/tree/27ef9db2735b5f7b32df12c86ce635a1e0868a66/Day14)

- Higher Lower Game
- random.choice()

```python
def is_answer():

    ...

    # ¡MY CODE!
    if a.get("follower_count") >= b.get("follower_count") and guess == 'a':
        return True
    elif a.get("follower_count") <= b.get("follower_count") and guess == 'b':
        return True
    else:
        return False

    # ¡SOLUTION!
    if a.get("follower_count") >= b.get("follower_count"):
        return guess == 'a'
    else:
        return guess == 'b'

    ...
```

---

## [Day 15](https://github.com/itisyijy/100Days4Python/tree/c3a2d479bf60c7192e476f6f976b81dfff548a0f/Day15)

- coffee machine project

```python
def resource_check(order):
    # ¡MY CODE!
    if resources["water"] >= MENU[order]["ingredients"]["water"]:
        if resources["coffee"] >= MENU[order]["ingredients"]["coffee"]:
            if order != "espresso":
                if resources["milk"] >= MENU[order]["ingredients"]["milk"]:
                    return True
                print("Sorry there is not enough milk.")
                return False
            return True
        print("Sorry there is not enough coffee.")
    else:
        print("Sorry there is not enough water.")
    return False

    # ¡SOLUTION!
    ingredients = MENU[order]["ingredients"]
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
```

---

## [Day 16](https://github.com/itisyijy/100Days4Python/tree/c77be7c917654187b328eecf412de66e268bf525/Day16)

### Procedural Programming

> - the earliest paradigm of programming
> - procedure leads another procedures
> - top to bottom

increasing complexity and number of relationships

### Object-Oriented Programming, OOP

> - blueprint of object = class, type
> - individual objects generated from the class = object

Object is a way of combining data and functionality altogether in the same thing

2 factors : attributes (what it has) & methods (what it does)

---

## [Day 17](https://github.com/itisyijy/100Days4Python/tree/758702e77fa5902c1fc1842d64758a7afb914d5d/Day17)

- PascalCase, camelCase, snake_case
- Constructor "\_\_init\_\_()"
- Initialize attributes
- Declare methods
- Meaning of 'self' keyword
- 'pass' keyword
- Making or modify object's attributes
- Call object's method

---

## [Day 18]()

### Importing Modules

```python
# import module_name
import turtle
tim = turtle.Turtle()

# from module_name import thing_in_module -> reducing redundancy
from turtle import Turtle
tom = Turtle()

# from module_name import * -> avoidable
from turtle import *
joe = Screen()
```

### Aliasing Modules

```python
# import module_name as alias_name
import turtle as t
kim = t.Turtle()
```

### Installing Modules

- python standard library: already installed
- others: installation needed. PyCharm will helps you.

### Tuple

```python
# tuple implementation
my_tuple = (1, 10, 3, 5, 7)
```

- 'tuple' is similar with 'list', but it has an immutable order.
- Items of tuple and tuple itself cannot be modified.

---

## [Day 19](https://github.com/itisyijy/100Days4Python/tree/0b61b17e10355de9de687c07a6677ad2659e920a/Day19)

### Function as Inputs(Arguments)

```python
def function_a(arg):
    return

# Arguments -> Function Name Without Parenthesis
def function_b(function_a):
    return
```

### Instaces

```python
from turtle import Turtle
timmy = Turtle()
tommy = Turtle()
```

- Turtle() -> class
- timmy, tommy, ... -> object
- timmy != tommy -> different instance
  - each instance can have own state

---

## [Day 20_21]()

### Class Inheritance

The idea that classes can inherit from other classes(attributes and methods).

```python
# Superclass
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
      print("inhale, exhale")

# Subclass
# Fish class inherits Animal class.
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("doing this underwater")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.swim()     # moving in water
nemo.breath()   # inhale, exhale doing this underwater
print(f"Number of eyes : {nemo.num_eyes}")  # 2
```

### Slicing

How to slice python list, tuple, and dictionary

```python
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(alphabet)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(alphabet[2:5])  # ['c', 'd', 'e']
print(alphabet[:5])  # ['a', 'b', 'c', 'd', 'e']
print(alphabet[2:])  # ['c', 'd', 'e', 'f', 'g']
print(alphabet[2:5:2])  # ['c', 'e']
print(alphabet[2::2])  # ['c', 'e', 'g']
print(alphabet[:5:2])  # ['a', 'c', 'e']
print(alphabet[::2])  # ['a', 'c', 'e', 'g']
print(alphabet[::-1])  # ['g', 'f', 'e', 'd', 'c', 'b', 'a']
```

---

## [Day 22](https://github.com/itisyijy/100Days4Python/tree/0c3afe9cca52840d069bf7dff3731d31c50ad3d5/Day22)

### The Pong Game

---

## [Day 23](https://github.com/itisyijy/100Days4Python/tree/b9cc8a34aa53f2f13ab241fcf01c445f4d6c202b/Day23)

### Turtle Crossing

```python
#[car_manager.py]

import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = STARTING_MOVE_DISTANCE
        # ¡MY CODE!
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.now_x = 300
        self.now_y = random.randrange(-240, 241)
        self.goto(self.now_x, self.now_y)
        # ¡SOLUTION!
        self.hideturtle()
        self.all_cars = []

    # ¡MY CODE!
    def move(self, level):
        if self.xcor() > -320 :
            self.goto(self.xcor() - (self.move_speed + MOVE_INCREMENT * level), self.now_y)


    # ¡SOLUTION!
    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randrange(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    # ¡SOLUTION!
    def move(self):
        for car in self.all_cars:
            car.backward(self.move_speed)

    # ¡SOLUTION!
    def level_up(self):
        self.move_speed += MOVE_INCREMENT
```

---

## [Day 24](https://github.com/itisyijy/100Days4Python/tree/83efb07b6a56140d07c07d357e4022b28ca07fc1/Day24)

### File Access

```python
file = open("file.txt", mode="")
file.read()     # mode="r", read
file.write()    # mode="w", write or mode="a", append
file.close()    # free resources

# no need for .close()
with open("file.txt", mode="") as file:
    file.read()
    file.write()
```

> [w]rite mode can make file with the contents when the file name doesn't exist.
> If the file exist, then overwrite the contents.

> In [r]ead mode, file contents are only readable. It cannot be modified.

> [a]ppend mode add the contents in EOF

### Paths

#### Absolute File Path

> /mnt/c/Users/itisyijy/Desktop/100Days4Python/Day24
>
> The first " / " is root.

Absolute file path always start off relative of the root

#### Relative File Path

> ./100Days4Python/Day24
>
> " . " is working directory.
>
> In this case, "/mnt/c/Users/itisyijy/Desktop" is current directory.
>
> " ./ " is optional

> ../README.md
>
> " .. " is parent directory.
>
> In this case, "/mnt/c/Users/itisyijy/Desktop100Days4Python/Day24" is current directory.

- Absolute file path always start off relative of the root
- Relative file path is relative with your current working directory.

---

## [Day 25](https://github.com/itisyijy/100Days4Python/tree/857d92d36f77d01d03979986831101ee42d1083c/Day25)

### Working with CSV File

CSV(Comma-Separated Values) : Representing tabular data that fits in table such as spreadsheet.

```python
# Using csv
import csv

with open("./weather_data.csv") as data_file:
    weather_data = csv.reader(data_file)
    temperatures = []
    for row in weather_data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

```

### Pandas for Data Analyzing

```python
import pandas

data = pandas.read_csv("./weather_data.csv")

# DataFrame(2D) in pandas
data_dict = data.to_dict()
print(data)
print(data_dict)

# Series(1D) in pandas
temp = data["temp"].to_list()
print(temp)

# Get mean value in "temp" column
print(sum(temp) / len(temp))
print(data["temp"].mean())

#  Get max value in "temp" column
print(data["temp"].max())

# Get data in columns
print(data["condition"])    # like dictionary
print(data.condition)       # like object

# Get data in rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# Convert Monday temperature to Fahrenheit
monday = data[data.day == "Monday"]
print(monday.temp)
print(monday.temp * (9 / 5) + 32)

# Create a DataFrame from scratch
result = {
    "students": ["Pedro", "James", "Micky"],
    "scores": [76, 56, 65],
}
result_pandas = pandas.DataFrame(result)
print(result_pandas)
result_pandas.to_csv("./result.csv")    # make DataFrame .csv file

```

---

## [Day 26](https://github.com/itisyijy/100Days4Python/tree/09cecff2cc7cea6a3031e9e3dc4565632d90a917/Day26)

### List Comprehension

` new_list = [new item for item in list if condition]`

```python
with open("./file1.txt", mode="r") as file1:
    one = [int(num) for num in file1.readlines()]
with open("./file2.txt", mode="r") as file2:
    two = [int(num) for num in file2.readlines()]

print(one, two)
result = [i for i in one if i in two]

print(result)
```

### Dictionary Comprehension

`new_dict = {new_key:new_value for item in list}`

```python
import random

names = ['Li', 'Mia', 'Zoe', 'Finn', 'Yara', 'Jonathan', 'Alexander', 'Elizabeth', 'Gabrielle', 'Christopher']
students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)

passed_students = {student: score for (student, score) in students_scores.items() if score > 60}
print(passed_students)
```

`new_dict = {new_key:new_value for (key,value) in dict.items() if condition}`

```python
import pandas

players = {
    "name": ["Son", "Maddison", "Solanke", "Kulusevski", "Romero"],
    "number": [7, 10, 19, 21, 17],
}

players_df = pandas.DataFrame(players)

for (index, row) in players_df.iterrows():
    print(row["name"], row["number"])
```

---

## [Day 27](https://github.com/itisyijy/100Days4Python/tree/d259d47e2c45ced1ea1caf27d0968191f8c4df2f/Day27)

### Advanced Python Arguments

```python
# Arguments with Default Values
def f1(a=1, b=2, c=3):
    print(a, b, c)

# Unlimited Positional Arguments, *args
def f2(n1, n2):
    return n1 + n2

def f3(*args):
    result = 0
    for n in args:  # args -> tuple type
        result += n
    return result

# Many Keyworded Arguments, **kwargs
def f4(n, **kwargs):
    n += kwargs["add"]  # kwargs -> dictionary type
    n *= kwargs["multiply"]
    return n

#
class Car:
    def __init__(self, **kwargs):
        self.brand = kwargs.get("brand")    # .get() -> return None when no value
        self.model = kwargs.get("model")    # kwargs[""] -> error can occur when no value
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")

```

### Tkinter Widgets

> Label, Entry, Button, Scale, Text,
> Spinbox, Checkbutton, Radiobutton, Listbox, ...

### Tkinter Layout Managers : no mix pack() with grid()

> pack()
>
> place(x=i, y=j)
>
> grid(column:i, row=j)

---

## [Day 28](https://github.com/itisyijy/100Days4Python/tree/8c054a1690ddb25e4d0c72c04be1e8686394417a/Day28)

### Pomodoro based on TKinter

```python
import tkinter

# Canvas widget : image, text ...
tkinter.Canvas().create_image(image=tkinter.PhotoImage())
tkinter.Canvas().create_text()

# like time.sleep(100) in Tkinter
def func():
  pass

id = tkinter.Tk().after(100, func)
tkinter.Tk().after_cancel(id)
```

## [Day 29](https://github.com/itisyijy/100Days4Python/tree/340b0efd10f2d26ef63b76ae5076afdb8769bfde/Day29)

### Password Manager

```python
import pyperclip

text = "Hello World!"
pyperclip.copy(text)
pyperclip.paste()

from tkinter import messagebox
messagebox.showinfo()
messagebox.askyesno()
...

from tkinter import *
label = Label()
label.grid(column=1, row=1, columnspan=2, sticky="NSWE")

entry = Entry()
entry_value = entry.get()
entry.delete(0, END)
```

---

## [Day 30](https://github.com/itisyijy/100Days4Python/tree/dbf190bda9c208c25249656eeea787b45cb997d7/Day30)

### Handling Errors and Exceptions

> Frequently Occur : if/else
>
> Rarely Occur : try/except

```python
a_dict = {"key": "value"}

try:    # Something that might cause an exception
    file = open("./a_file.txt")
    print(a_dict["lock"])

except FileNotFoundError:   # Do this if there was an exception
    file = open("./a_file.txt", mode="w")
    file.write("Something")

except KeyError as error_message:   # Multiple "except" is possible
    print(f"KeyError: {error_message}")

else:   # Do this if there were no exceptions
    content = file.readlines()
    print(content)
    file.close()

finally:    # Do this no matter what happens
    raise IndexError("Intentional Error Occurrence")    # Raise Own Exception

```

### JSON File

- Format : Nested Dictionary

```python
import json

new_data = "blah"
with open("data.txt", mode="r") as file:
    data = json.load(file)  # READ

data.update(new_data)   # UPDATE

with open("data.txt", mode="w") as file:
    json.dump(data, file)    # WRITE

```

---

## [Day 31](https://github.com/itisyijy/100Days4Python/tree/a935c1194d80c1c3c57d9d0a028e22e09bbd70bf/Day31)

### Flash Card Program

- Pandas
  - read_csv()
  - to_csv()
  - to_dict()
- Random
- Tkinter
  - after() / after_cancel()
  - Canvas
    - create_image()
    - create_text()
    - itemconfig()
  - Button

---

## [Day 32](https://github.com/itisyijy/100Days4Python/tree/952f99a1ec12bbe0e3a91ed8448de988afb3f6a2/Day32)

### What is SMTP(Simple Mail Transfer Protocol)?

> the rules that determine how an email is received by mail servers
> passed onto the next mail server and how email can be sent around

### smtplib

```python
import smtplib

from_email = "itisyijy@gmail.com"
from_password = input(f"{from_email}\nPASSWORD : ")

to_email = "graycona@yahoo.com"

# TLS, Transport Layer Security. Protocol Designed to Secure and Encrypt Communications over a Computer Network

# gmail_connection = smtplib.SMTP("smtp.gmail.com")
# gmail_connection.starttls()
# gmail_connection.login(user=from_email, password=from_password)
# gmail_connection.sendmail(from_addr=from_email, to_addrs=to_email,
#                           msg="Subject:Hello\n\nThis is the body of email.")
# gmail_connection.close()

with smtplib.SMTP("smtp.gmail.com") as gmail_connection:
    gmail_connection.starttls()
    gmail_connection.login(user=from_email, password=from_password)
    gmail_connection.sendmail(from_addr=from_email, to_addrs=to_email,
                              msg="Subject:Hello\n\nThis is the body of email.")    # \n\n ~ body
```

### datetime

```python
import datetime

# Current Time
now = datetime.datetime.now()
now_year = now.year
now_month = now.month
now_day = now.day
now_weekday = now.weekday() # 0 MON / 1 TUE / 2 WED / 3 THU / 4 FRI / 5 SAT / 6 SUN
print(now_year, now_month, now_day, now_weekday)

my_birthday = datetime.datetime(year=1948, month=8, day=15)
print(my_birthday)
```

---

## [Day 33](https://github.com/itisyijy/100Days4Python/tree/dbaac87d164ebc301c01774dc7ce25e404121fe4/Day33)

### Application Programming Interface, API

> Set of commands, functions, protocols, and objects
> that programmers can use to create software or interact with an external system.

### API Endpoint (URL) : Location that data is stored

### API Request

```python
import requests

# response code
parameters = {
  "key": "value",
              }
response = requests.get("api.something.com", params=parameters)

# make error
response.raise_for_status()

# json format data
data = response.json()

```

#### API Response Code

> - 1XX : Hold On
> - 2XX : Here You Go
> - 3XX : Go Away
> - 4XX : You Screwed Up
> - 5XX : I Screwed Up

---

## [Day 34](https://github.com/itisyijy/100Days4Python/tree/ce6bf22c5be6d711796ded79c097226c8bbc00e2/Day34)

### HTML Entity

```python
import html

html.unescape("This is an example with &lt;b&gt;bold&lt;/b&gt; text.")
```

### Type Hint

```python
# Assign Type of Variable #
name: str
height: float
name = "Jordan"
height = [172]      # Error message

# Assign Type of Return Value #
def is_adult(age: int) -> bool:
    if age >= 19:
        return True
    else:
      return "No"   # Error message


is_adult("twelve")  # Error message
```

### .grid() padding

```python
import tkinter

tkinter.Label().grid(column=1, row=2, padx=20, pady=10)
```

---

## [Day35](https://github.com/itisyijy/100Days4Python/tree/65a71d62fc72ca586409939b98397f47f5ae15e9/Day35)

### API Key for User Authentication

### Slicing

```python
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lsit_3_to_8 = list[3:9] # start ~ stop-1
```

### Environment Variables

> A variable for storing and sharing system information
>
> Environment Variable is set globally accessible.
> Various program or script are able to refer the same value.
>
> 1. Setting System Path
> 2. Setting Program
> 3. Saving User Info
> 4. Saving Credential Info

```shell
# How to declare Environment Variable in UNIX
export ENV_VAR=0123456789

# How to declare Environment Variable in Windows
set ENV_VAR=0123456789
```

```python
# How to use Environment Variable in Python
import os

os.environ.get("ENV_VAR")
```

---

## [Day 36](https://github.com/itisyijy/100Days4Python/tree/94721e19647b4f3163c219c3ad27ce3e5d73f4df/Day36)

> Nothing to Comment

---

## [Day 37](https://github.com/itisyijy/100Days4Python/tree/3af83ac7d3435a7f8fd1ee222786a2dd83b188da/Day37)

### HTTP Requests

> #### 1. GET = requests.get()
>
> Program request particular piece of data to external system.
> The system gives the data in the response.
>
> #### 2. POST = requests.post()
>
> Program gives external system some piece of data
>
> #### 3. PUT = requests.put()
>
> Update data in the external system
>
> #### 4. DELETE = requests.delete()
>
> Delete data in the external system

https://pixe.la/v1/users/auxigen/graphs/exercise.html

---

## [Day 38](https://github.com/itisyijy/100Days4Python/tree/8d39f1f7cda1486fcda1f9ead49e121bb22057bc/Day38)

[Check Google Sheet](https://docs.google.com/spreadsheets/d/1xcuo1peI80QWm1XfSjyaauPQSrMtSlaxljPrlI8Vec0/edit?usp=sharing)

```python
import os

# Set
os.environ["ENV_VAR"] = "KEY"

# Get
KEY = os.environ["ENV_VAR"] # Raise exception if key does not exist
KEY = os.environ.get("ENV_VAR") # return None if key does not exist
KEY = os.environ.get("ENV_VAR", "MESSAGE") # return MESSAGE if key does not exist
```

- time.strftime()

```python
from datetime import datetime

today = datetime.now()

# Formatting Date & Time
today.strftime("%X")
```

---

## [Day 39_40](https://github.com/itisyijy/100Days4Python/tree/15193671a402c3f8afeaeffa48ea43f501451642/Day39_40)

> Unavailable Assignment. I skipped this project.

```python
# .env file
# ENV_VAR=SOMETHING

import os
from dotenv import load_dotenv

load_dotenv()
os.environ.get("ENV_VAR")
```

```python
from datetime import datetime, timedelta

today = datetime.today()
three_days_after = today + timedelta(days=3)
```

---

## [Day 41](https://github.com/itisyijy/100Days4Python/tree/6ddddc097b90fb0e30344d52c1bf0dd7d4f867be/Day41)

### How Does the Internet Work?

Server <-> Client

> Request "www.google.com"
>
> - Browser sends the message to Internet Service Provider(ISP)
> - ISP sends the message to Domain Name System(DNS) Server
>   - DNS Server finds exact IP address of request
> - DNS Server sends IP address back to browser
> - Browser send direct request to the IP address through ISP
> - The server of the IP sends the website files

> Website Files
>
> - Hyper Text Markup Language(HTML) - Structure of website
> - CSS - Styling of website
> - JS - Behavior of website

> HTML Elements
>
> - <Start_Tag> Content <\End_Tag>
> - <Self-closing_Tag>
> - <HTML_elemnet HTML_Attribute="">

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Title of Webpage</title>
    <meta charset="incoding" />
  </head>
  <body>
    <h1>Heading 1</h1>
    <ol>
      <!-- ordered list -->
      <li>list item</li>
    </ol>
    <ul>
      <!-- unordered list -->
       <li>list item</li>
    </ul>
    <hr />
    <!-- horizontal rule -->
    <p>
        paragraph
        <em>emphasis, italic<em>
        <strong>importance, bold</strong>
        <a href="src.file">Link Text</a>
        <img src="image.file" alt="alternative text for image">
    </p>

  </body>
</html>
```

---

## [Day 42]()

### HTML Table

```html
<table>
  <thead>
    <tr>
      <td>Name</td>
      <td>Price</td>
      <td>Quantity</td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Laptop</td>
      <td>$1000</td>
      <td>2</td>
    </tr>
    <tr>
      <td>Smartphone</td>
      <td>$599</td>
      <td>3</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <td>Total</td>
      <td>$3797</td>
      <td>5</td>
    </tr>
  </tfoot>
</table>
```

### [HTML Form & Input](https://github.com/itisyijy/grey_cona.git)

please check "contact_details.html" in grey_cona

> get data from user and submit the data to server

```html
<form action="address_to_server" method="GET/POST">
  <label name="name">Name:</label>
  <input type="text/password/..." name="name" id="name" />

  <textarea
    name="message"
    cols="20"
    rows="10"
    placeholder="write down your message."
  ></textarea>

  <select name="country">
    <!-- dropdown list -->
    <option value="korea">korea</option>
    <option value="usa">usa</option>
  </select>
</form>
```

---

## [Day 43]()

### CSS

#### Priority of CSS Style

style more specific is powerful.

> inline css > internal css > external css
>
> inline style > id > class, attribute, pseudo-class > tag > \*

inline css

```html
<tag style="~~~~~"></tag>
```

internal css

```html
<head>
  <style>
    h1 {
      ~~~~~
    }
  </style>
</head>
```

external css

```html
<head>
  <link rel="stylesheet" href="file.css" />
</head>
```

```css
h1 {
  ~~~~~
}
```

### CSS Syntax

> selector { property: value; } <br>
> = who { what: how; }

```html
<tag class="a"></tag>
<tag class="b c"></tag>
<tag id="unique"></tag>
```

```css
/* Tag Selectors */
tag {
  color: red;
}

/* Class Selectors */
.a {
  color: white;
}

.b {
  color: black;
}

.c {
  color: black;
}

/* ID Selectors */
#unique {
  color: orange;
}
```

#### class vs. id

> class: certain category or group, single tag with multiple class is possible

> id: one and only, single, unique

#### "pseudo-class" - express different status

---

## [Day 44]()

### Block Elements

only element in the row<br>
can be resize

```
paragraphs <p>
headers <h1>-<h6>
divisions <div>
list <ol><ul> and list items <li>
forms <form>
...
```

### Inline Elements

can be side by side<br>
cannot resize

```
span <span>
images <img>
anchors <a>
...
```

### Inline-Block Element

can be side by side and resizable

```
block_element {
  display: inline-block;
}

inline_element {
  display: inline-block;
}
```

### None Element

```
element {
  display: none;
}
>>> as if it is deleted
```

```
cf.)
element {
  visibility: hidden;
}
>>> the element still occupies the space
```

### CSS Rendering Hierarchy

1. Contents is everything.
2. Order comes from code.
3. Children sit on parents.

### CSS Position

- static : default HTML flow
- relative : relative position based on static position. no impact on other elements. add margin.
  ```
  img {
    position: relative;
    top: 00;
    bottom: 00;
    left: 00;
    right: 00;
  }
  >>> similar with concept of margin. (e.g., margin-top)
  ```
- absolute : set margin relative to entire docs(HTML), but can be adjusted based on nearest parent(position: relative;). not occupy original space.
- fixed : fixed position by viewport

### Center
- text-align: center; >>> center everything with no width set
- margin: 0 auto 0 auto; >>> center things with width set


---

## [Day 45]()
### Web Scrapping
* BeautifulSoup: Drilling HTML files. Find html tags and its contents inside