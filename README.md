![python](https://img.icons8.com/?size=100&id=13441&format=png&color=000000)

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

```
def is_answer()

...

¡MY CODE!
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
```
def resource_check(order):
    # ¡MY CODE!
    # if resources["water"] >= MENU[order]["ingredients"]["water"]:
    #     if resources["coffee"] >= MENU[order]["ingredients"]["coffee"]:
    #         if order != "espresso":
    #             if resources["milk"] >= MENU[order]["ingredients"]["milk"]:
    #                 return True
    #             print("Sorry there is not enough milk.")
    #             return False
    #         return True
    #     print("Sorry there is not enough coffee.")
    # else:
    #     print("Sorry there is not enough water.")
    # return False

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