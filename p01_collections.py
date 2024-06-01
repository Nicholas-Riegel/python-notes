# LISTS

# Print the number of items in the list:
# list = ["apple", "banana", "cherry"]
# print(len(list))

# Using the list() constructor to make a List:
# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

# COLLECTIONS (Arrays)

# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Dictionary is a collection which is ordered and changeable. No duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

# ACCESSING LISTS
# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])

# The search will start at index 2 (included) and end at index 5 (not included).
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# This example returns the items from the beginning to, but NOT including, "kiwi":
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])

# Check if "apple" is present in the list:
# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   answer = "Yes, {} is in the fruits list"
#   print(answer.format("'apple'")) 

# CHANGING LISTS

# Change the second item:
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# Change the second value by replacing it with two new values:
# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

############################

# remove from end:
# thislist = ["apple", "banana", "cherry"]
# x = thislist.pop()
# print(thislist)

# add to end:
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

# remove from beginning:
# thislist = ["apple", "banana", "cherry"]
# x = thislist.pop(0)
# print(thislist)

# add to beginning:
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(0, "orange")
# print(thislist)

#############################

# Remove "banana":
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)

# Remove the first occurance of "banana":
# thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
# thislist.remove("banana")
# print(thislist)

# Add the elements of tropical to thislist:
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# Add elements of a tuple to a list:
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)

# Delete the entire list:
# thislist = ["apple", "banana", "cherry"]
# del thislist 
# print(thislist)

# Clear the list content:
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)

# LOOPING

# Print all items in the list, one by one:
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x) 

# Print all items by referring to their index number:
# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i]) 

# Print all items, using a while loop to go through all the index numbers
# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#   print(thislist[i])
#   i += 1 

# A short hand for loop that will print all items in a list:
# thislist = ["apple", "banana", "cherry"]
# [print(x) for x in thislist] 

# SORTING

# Sort the list alphabetically:
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# Sort the list numerically:
# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

# To sort descending, use the keyword argument reverse = True:
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort(reverse = True)
# print(thislist)

# Sort the list descending:
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)
# print(thislist)

# Reverse the order of the list items:
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.reverse()
# print(thislist)

# COPYING LISTS

# Make a copy of a list with the copy() method:
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)

# Make a copy of a list with the list() method:
# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

# JOINING LISTS

# Join two list:
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)

# Append list2 into list1:
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# for x in list2:
#   list1.append(x)
# print(list1)

# Use the extend() method to add list2 at the end of list1:
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)

# LIST METHODS

# Method 	    Description
# append()	    Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()      Removes the item with the specified value
# reverse()	    Reverses the order of the list
# sort()	    Sorts the list

# DICTIONARIES

# Print the "brand" value of the dictionary:
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

# x = thisdict["brand"]
# print(x)

# Add a new item to the original dictionary:
# thisdict["color"] = "white"
# print(thisdict)

# Get a list of the keys:
# y = thisdict.keys() 
# print(y)

# Get a list of the values:
# x = thisdict.values() 

# Get a list of the key:value pairs
# x = thisdict.items() 
# print(x)

# Check if "model" is present in the dictionary:
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary") 

# Change the "year" to 2018:
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018

# Update the "year" of the car by using the update() method:
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020}) 

# Remove items

# The pop() method removes the item with the specified key name:
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict) 

# The del keyword removes the item with the specified key name:
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict) 

# The clear() method empties the dictionary:
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict) 

# Looping through dictionaries

# Print all key names in the dictionary, one by one:
# for x in thisdict:
#   print(x) 

# Print all values in the dictionary, one by one:
# for x in thisdict:
#   print(thisdict[x])

# You can use the keys() method to return the keys of a dictionary:
# for x in thisdict.keys():
#   print(x) 

# You can also use the values() method to return values of a dictionary:
# for x in thisdict.values():
#   print(x) 

# Loop through both keys and values, by using the items() method:
# for x, y in thisdict.items():
#   print(x, y) 

# Make a copy of a dictionary with the copy() method:
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)

# Nested dictionaries

# Create a dictionary that contain three dictionaries:
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# } 

# Print the name of child 2:
# print(myfamily["child2"]["name"]) 

# Dictionary Methods

# clear()	    Removes all the elements from the dictionary
# copy()	    Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	        Returns the value of the specified key
# items()	    Returns a list containing a tuple for each key value pair
# keys()	    Returns a list containing the dictionary's keys
# pop()	        Removes the element with the specified key
# popitem()	    Removes the last inserted key-value pair
# update()	    Updates the dictionary with the specified key-value pairs
# values()	    Returns a list of all the values in the dictionary

