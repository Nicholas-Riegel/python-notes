# CONTROL STRUCTURES

# Nested if statements

# x = 41
# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.") 

# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

# a = 33
# b = 200
# if b > a:
#   pass 

# while

# Print i as long as i is less than 6:
# i = 1
# while i < 6:
#   print(i)
#   i += 1

# Exit the loop when i is 3:
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1 

# Continue to the next iteration if i is 3:
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# for

# Print each fruit in a fruit list:
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)

# Loop through the letters in the word "banana":
# for x in "banana":
#   print(x)

# Exit the loop when x is "banana":
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break

# Exit the loop when x is "banana", but this time the break comes before the print:
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)

# Do not print banana:
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)

# Using the range() function:
# for x in range(6):
#   print(x)

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
# for x in range(2, 6):
#   print(x)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
# Increment the sequence with 3 (default is 1):
# for x in range(2, 30, 3):
#   print(x)

# Print each adjective for every fruit:
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y) 