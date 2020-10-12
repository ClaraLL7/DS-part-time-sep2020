"""
Example of a python module. Contains a variable called my_variable,
and a function called my_function.
"""

my_variable = 0
my_variable2 = (20,)
my_variable3 = "var"

def my_function1():
    """
    Example function
    """
    return my_variable


def my_function2(var1, var2):
    """
    Example 2 function. Returns a list that contains a concatenation of my_variable2 and my_variable3 and var1 and var2
    """
    return list(my_variable2) + [my_variable3] + [var1] + [var2]
