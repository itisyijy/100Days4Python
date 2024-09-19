# Day10 for 100Days4Python
# Return

# Title Case
def format_name(f_name, l_name):
    """"
    Format parameters to return the title case version of them
    
    Parameters:
    f_name (str) : first name
    l_name (str) : last name
    
    Returns:
    str : title case version of full name = f_name + " " + l_name
    """ # docstring -> documentation of function
    if f_name == "" or l_name == "":
        return "error"
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"

firstname = "jeongyun"
lastname = "lee"
print(format_name(firstname, lastname))
print(format_name("", "biden"))