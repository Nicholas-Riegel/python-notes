# FUNCTIONS

# a function is defined using the def keyword:

# def my_function():
#   print("Hello from a function")

# my_function()

# arguments
# def my_function(fname):
#   print(fname, "Smith")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus") 

# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the value that is sent to the function when it is called.

# This function expects 2 arguments, and gets 2 arguments:
# def my_function(fname, lname):
#   print(fname, lname)

# my_function("Emil", "Smith") 

# If the number of arguments is unknown, add a * before the parameter name:
# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus") 

# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") 

# Arbitrary Keyword Arguments, **kwargs
# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Smith") 

# Default Parameter Value

# If we call the function without argument, it uses the default value:
# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil") 

# Passing a List as an Argument
# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)

# Return Values
# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9)) 
