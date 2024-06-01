# SYNTAX
# if 5 > 2:
#   print("Five is greater than two!")

# Comments
"""
This is a comment
written in
more than just one line
"""
'''
This is also a 
multiline 
comment
'''

# VARIABLES

# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)

# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)

# DATA TYPES

# Text Type: 	    str
# Numeric Types: 	int, float, complex
# Sequence Types:   list, tuple, range
# Mapping Type: 	dict
# Set Types: 	    set, frozenset
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview
# None Type: 	    NoneType

# CASTING

# x = int(1)        # x will be 1
# y = int(2.8)      # y will be 2
# z = int("3")      # z will be 3

# x = float(1)      # x will be 1.0
# y = float(2.8)    # y will be 2.8
# z = float("3")    # z will be 3.0
# w = float("4.2")  # w will be 4.2

# STRINGS

# strings are arrays
# a = "Hello, World!"
# print(a[0])

# for x in "banana":
#   print(x)

# Get the characters from position 0 to position 4 (not included):
# b = "Hello, World!"
# print(b[0:4])

# Get the characters from the start to position 4 (not included):
# b = "Hello, World!"
# print(b[:4])

# Get the characters from position 2, and all the way to the end:
# b = "Hello, World!"
# print(b[2:])

# Get the characters from "o" in "World!" (position -5) to, but not included: "d" in "World!" (position -2):
# b = "Hello, World!"
# print(b[-5:-2])

# Remove white space
# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!" 

# The replace() method replaces a string with another string:
# a = "Hello, World!"
# print(a.replace("H", "J"))
# print(a)

# The split() method splits the string into substrings if it finds instances of the separator:
# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!'] 

# concatenation
# age = 36
# txt = "My name is John, I am " + age
# print(txt)

# Use the format() method to insert things into strings:
# age = 36
# txt = "My name is John, and I am {} years old"
# print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))

# The escape character allows you to use double quotes when you normally would not be allowed:
# txt = "We are the so-called \"Vikings\" from the north."

# OPERATORS

# + 	Addition 	x + y 	
# - 	Subtraction 	x - y 	
# * 	Multiplication 	x * y 	
# / 	Division 	x / y 	
# % 	Modulus 	x % y 	
# ** 	Exponentiation 	x ** y 	
# // 	Floor division 	x // y

# Assignment operators 
# = 	x = 5 	x = 5 	
# += 	x += 3 	x = x + 3 	
# -= 	x -= 3 	x = x - 3 	
# *= 	x *= 3 	x = x * 3 	
# /= 	x /= 3 	x = x / 3 	
# %= 	x %= 3 	x = x % 3 	
# //= 	x //= 3 	x = x // 3 	
# **= 	x **= 3 	x = x ** 3

# Comparison operators are used to compare two values:

# == 	Equal 	x == y 	
# != 	Not equal 	x != y 	
# > 	Greater than 	x > y 	
# < 	Less than 	x < y 	
# >= 	Greater than or equal to 	x >= y 	
# <= 	Less than or equal to 	x <= y

# Logical operators are used to combine conditional statements:
# and  	Returns True if both statements are true 	x < 5 and  x < 10 	
# or 	  Returns True if one of the statements is true 	x < 5 or x < 4 	
# not 	Reverse the result, returns False if the result is true 	not(x < 5 and x < 10)

# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
# is  	  Returns True if both variables are the same object 	x is y 	
# is not 	Returns True if both variables are not the same object

# Membership operators are used to test if a sequence is presented in an object:
# in  	  Returns True if a sequence with the specified value is present in the object 	x in y 	
# not in 	Returns True if a sequence with the specified value is not present in the object 	x not in y

# Precedence
# 'and' takes precedence (is evaluated before) over 'or'
# the immediate neighbors of 'and' are evaluated before 'or'
# x = True or False and False
# x = False and False or True
# print(x) # True!

