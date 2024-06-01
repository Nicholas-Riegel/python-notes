# FizzBuzz
# for i in range(15):
#   i += 1
#   if i % 3 == 0 and i % 5 == 0:
#     print('FizzBuzz')
#   elif i % 3 == 0:
#     print('Fizz')
#   elif i % 5 == 0:
#     print('Buzz')
#   else:
#     print(i) 

# populate a list up to 15 with only odd numbers
# listx = []
# for i in range(15):
#   i += 1
#   if i % 2 == 0:
#     continue
#   listx.append(i)
# listx.sort(reverse=True)
# print(listx)

# car = {
#   "company" : "Lamborghini",
#   "model" : "Diablo",
#   "color" : "red",
#   "capacity" : 2
# }

# for x,y in car.items():
#   print(x, ":", y)

# for x in car.keys():
#   print(x)

# print(car.values())

# f = open("notes.txt", "w")
# f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
# f.close()

# f = open("notes.txt")
# print(f.read())
# f.close()

# import os
# if os.path.exists("notes.txt"):
#   os.remove("notes.txt")
# else:
#   print("File does not exist.")

# add 4 'a's to li, and then remove them all 
# li = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# li.extend(['a', 'a', 'a', 'a'])
# print(li)
# for x in li:
#   if 'a' in li:
#     li.remove('a')
# print(li)

# add a sequence from 1 onwards after each letter in li
# li2 = []
# y = 1
# for x in li:
#   li2.append(x)
#   li2.append(y)
#   y +=1
# li = li2

# now removed all the numbers
# i = 0
# while i < len(li):
#   if type(li[i]) == int:
#     del li[i]
#   i += 1
# print(li)

# create a list from 0 to 15 of every 3rd number, starting with 3, 6, 9, etc.
# li = []
# i = 3
# while i < 16:
#   li.append(i)
#   i += 3
# print(li)
# # remove all the even numbers
# j = 0
# while j < len(li):
#   if li[j] % 2 == 0:
#     del li[j]
#   j += 1
# print(li)

# li = [7, "lady-bird", 10 , "mug-shot"]
# for x in range(len(li)):
#   if type(li[x]) ==  str and "-" in li[x]:
#     li[x] = li[x].replace('-', '_')
#   if type(li[x]) ==  str:
#     li[x] = 'HE-' + li[x] + '-QE'
# print(li)

# for x in range(len(li)):
#   print(x)

# person = {
#     'name': 'John Doe',
#     'sex': 'Male',
#     'age': 32,
#     'married': True
# }

# for key, value in person.items():
#   print("Key:", key +",", "Value:", value)

# array = [(1, 2), (3, 4), (5, 6)]
# for a, b in array:
#   if a < b:
#     print('the first is less than the second')

list0 = []
for j in range(10):
  j+=1
  list0.append(j)

def monotonic(alist):
  for i in range(len(alist)):
    if i+1 in range(len(alist)):
      if alist[i] < alist[i+1]:
        print("{} is less than {}".format(alist[i], alist[i+1]))
        continue
      else:
        print("{} is not less than {}.".format(alist[i], alist[i+1]))
        print('The list is not monotonic.')
        break
    print('The list is monotonic.')

monotonic(list0)