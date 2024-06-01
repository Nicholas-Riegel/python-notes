# FILE HANDLING

# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# To open a file for reading it is enough to specify the name of the file:
# f = open("demofile.txt")
# The code above is the same as:
# f = open("demofile.txt", "rt")
# Because "r" for read, and "t" for text are the default values, you do not need to specify them.

# The open() function returns a file object, which has a read() method for reading the content of the file:
# f = open("demofile.txt")
# print(f.read()) 

# Return the 5 first characters of the file:
# f = open("demofile.txt")
# print(f.read(5)) 

# Read one line of the file:
# f = open("demofile.txt")
# print(f.readline()) 

# Read two lines of the file:
# f = open("demofile.txt")
# print(f.readline())
# print(f.readline()) 

# Loop through the file line by line:
# f = open("demofile.txt", "r")
# for x in f:
#   print(x) 

# It is a good practice to always close the file when you are done with it.
# f = open("demofile.txt")
# print(f.read())
# f.close() 

# Write to an Existing File

# To write to an existing file, you must add a parameter to the open() function:

# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content

# Open the file "demofile2.txt" and append content to the file:
# f = open("demofile2.txt", "w")
# f.write("Now the file has more content!")
# f.close()

#open and read the file after the appending:
# f = open("demofile2.txt")
# print(f.read()) 
# f.close()

# Create a file called "myfile.txt":
# f = open("myfile.txt", "x")

# Create a new file if it does not exist:
# f = open("myfile.txt", "w")

# Delete a File

# To delete a file, you must import the OS module, and run its os.remove() function:

# Remove the file "demofile.txt":
# import os
# os.remove("demofile2.txt")

# To avoid getting an error, you might want to check if the file exists before you try to delete it:

# Check if file exists, then delete it:
# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")

# To delete an entire folder, use the os.rmdir() method:
# import os
# os.rmdir("myfolder")

# THE OS MODULE
import os
# current_working_directory = os.getcwd() 
# files_in_dir = os.listdir('./')
# create a directory:
# os.makedirs('./data', exist_ok=True)
# url1 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans1.txt'
# url2 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans2.txt'
# url3 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans3.txt'

# from urllib.request import urlretrieve

# urlretrieve(url1, './data/loans1.txt')
# urlretrieve(url2, './data/loans2.txt')
# urlretrieve(url3, './data/loans3.txt')
# print(os.listdir('./data'))
# f = open('./data/loans1.txt')
# f_contents = f.read() 
# print(f_contents)
# f.close()

# Closing files automatically using with

# To close a file automatically after you've processed it, you can open it using the with statement.

# with open('./data/loans2.txt') as file2:
#   file2_contents = file2.read()
#   print(file2_contents)

# Reading a file line by line

# File objects provide a readlines method to read a file line-by-line.

# Processing data from files

# first make contents into a comma separated list:
# with open('./data/loans3.txt') as file3:
#     file3_lines = file3.readlines()

def parse_headers(header_line):
    return header_line.strip().split(',') 

# headers = parse_headers(file3_lines[0])

# Next, let's define a function parse_values that takes a line containing some data and returns a list of floating-point numbers.

# def parse_values(data_line):
#   values = []
#   for item in data_line.strip().split(','):
#       values.append(float(item))
#   return values

# line1 = parse_values(file3_lines[1])
# print(file3_lines[2])
# line2 = parse_values(file3_lines[2])
# this fails because the last item is a string '' (note the comma with nothing after it)

# so parse_values has to be updated
def parse_values(data_line):
  values = []
  for item in data_line.strip().split(','):
    if item == '':
      values.append(0.0)
    else:
      try:
        values.append(float(item))
      except ValueError:
        values.append(item)
  return values

# line1 = parse_values(file3_lines[1])
# line2 = parse_values(file3_lines[2])

# Next, let's define a function create_item_dict that takes a list of values and a list of headers as inputs and returns a dictionary with the values associated with their respective headers as keys.


# thing = list(zip('123', 'abcdefg'))
# print(thing)

def create_item_dict(headers, values):
  result = {}
  for header, value in zip(headers, values):
    result[header] = value
  return result

# dict1 = create_item_dict(headers, line1)
# dict2 = create_item_dict(headers, line2)

# We are now ready to put it all together and define the read_csv function.

def read_csv(path):
  result = []
  with open(path) as f:
    lines = f.readlines()
    headers = parse_headers(lines[0])
    for line in lines[1:]:
      values = parse_values(line)
      item_dict = create_item_dict(headers, values)
      result.append(item_dict)
  return result

result = read_csv('./data/loans3.txt') 