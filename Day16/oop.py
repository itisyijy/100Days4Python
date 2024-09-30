# Day16 for 100Days4Python
# Day16 : Constructing Object

from turtle import Turtle, Screen
# https://docs.python.org/3/library/turtle.html

# class name -> PascalCase
# constructing object : object_name = module.Class()
mbappe = Turtle()
print(mbappe)
mbappe.shape("turtle")
mbappe.color("orange")
mbappe.forward(100)

# attributes of object : object.attribute
my_screen = Screen()
print(my_screen.canvheight)
print(my_screen.canvwidth)

# methods of object : object.method()
my_screen.exitonclick()


# Day16 : Attributes & Methods

from prettytable import PrettyTable
# https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki

# make new object
table = PrettyTable()
print(table)

# call object's methods
table.add_column("Pokémon", ["Pikachu", "Charmander", "Squirtle"])
table.add_column("Type", ["Electric", "Fire", "Water"])

# access object's attribute
table.align = "l"   # left aligned
print(table)






