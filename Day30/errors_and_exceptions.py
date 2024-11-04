# Day30 for 100Days4Python
# Day30 : Errors and Exceptions

# ------------ Error -----------
# FileNotFound
# KeyError
# IndexError
# TypeError
# ...

# ----- Exception Handling -----
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

