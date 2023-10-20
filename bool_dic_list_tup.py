bool
# only 2 options 
bool([])  # false

bool(None)  # false

1 == 1  # true

1 != 1  # ->false

[] is None  # => false


# and or , not

a = True

b = True

# dont do -> a == True -it doesn’t work

# —

# dictionary has del and pop functionality

# mydic.pop(‘key’)

# del mydic[‘key’]

3 < 5 == True  # => false cause evaluation goes from right to left maybe ?

# sets do not repeat any elements

# sets have no order

my_tuple = (1,)

type(my_tuple)  # -> <class ‘tuple’>


# dictionary

# my_dict[‘key’] =  ‘a new value’


colors = ["red", "green", "blue", "orange", "yellow", "purple"]

for color in colors:
    print(f"inside the loop: {color}”")

print(f"outside of the loop: {color}”")


range(3)

range(0, 3)

for num in range(3, 7):
    print(num)

# can use enumerate on a list to get a tuple of key value pairs, index is key and value is element in array

enumerate(colors)

list(enumerate(colors))


# dictionary

# for key, value in hex_colors.items():

# 	print(key)

# 	print("-----------------"))

# 	print(value)


# while 3<5:

# 	print(val)

# 	val += 1


# #List Comprehensions

# [<value> for <vars> in <iter>]

# #with normal for loop

# names = [‘brian’, ‘ezra’, ‘susie’]

my_list = []

for name in names:
    my_list.append(len(name))

print(my_list)


# with comprehensions, added info goes in

[len(name) for name in names]

# so just one line instead of 4

# can also add conditional

[
    name for name in names if len(name) % 2 == 0
]  # -> this will print out even length names

# split, turn string into a list  like in js -

name_string = "ed, ted, bob, alex, ruf"

name_list = name_string.split(",")
# .join() is the opposite of split
# [num in nums if num % 2 == 0] #-> this will print out even numbers
[
    num * 2 for num in nums if num % 2 == 0
]  # -> this will print out even numbers and double them
# generator expressions
gen_expression = (x**2 for x in range(10) if x % 2 == 0)
# generator object
# once you iterate over it, it is gone , generator doesn't keep state
# it is a one time use thing
# slicing  -  [start:stop:step]
# start is inclusive, stop is exclusive
# step is how many to skip
# if you leave start blank it will start at 0
# if you leave stop blank it will go to the end
# if you leave step blank it will go by 1
# if you leave start and stop blank it will be a copy of the original list
# if you leave start and stop blank and do a negative step it will reverse the list
# [::-1] will reverse the list
# [::2] will skip every other element
# my_string[:7] will give you the first 7 characters of the string
# my_string[7:] will give you the last 7 characters of the string
# my_string[:] will give you a copy of the string
# FILES
# open() returns a file object
# open() takes two arguments, filename and mode
# mode is optional, default is 'r' for read mode
# mode can be 'r' for read, 'w' for write, 'a' for append, 'r+' for read and write
# file = open('my_file.txt', 'r') # opens file in read mode
# file.close() # closes file - NEED to close that file to release it
# with open('my_file.txt', 'r') as file: # opens file in read mode
# context manager - will close the file for you after you are done with it and take care of any cleanup
"""to comment out multiple lines in python
use triple quotes
>>> import json
>>> with open("cities.json") as cities_file:
...     cities_data = json.load(cities_file)
...     print(cities_data)
...
>>> # Let's pretty-print the results
>>> from pprint import pprint
>>> pprint(cities_data)
[{'name': 'New York', 'pop': 8550405},
 {'name': 'Los Angeles', 'pop': 3971883},
 {'name': 'Chicago', 'pop': 2720546},
 {'name': 'Houston', 'pop': 2296224},
 {'name': 'Philadelphia', 'pop': 1567442}]
>>> # Let's write the data to a JSON file
"""
# returns a list of dictionaries
# slice notation - [start:stop:step] - start is inclusive, stop is exclusive
# zip - zips two lists together into a list of tuples - zip(list1, list2) - returns a list of tuples - can also use zip(*list_of_tuples) to unzip a list of tuples into two lists
# instance methods - methods that are available on an instance of a class
# class methods - methods that are available on the class itself
# static methods - methods that are available on the class itself but don't have access to the class or instance
# class attributes - attributes that are available on the class itself
# class is a blueprint for creating instances of that class - class names are PascalCase
# instance attributes - attributes that are available on the instance of the class - instance names are snake_case
# __init__ - a method that is called when an instance of a class is created - it is the constructor for the class
# self - a reference to the instance of the class - it is the first argument to any instance method
# isinstanceof - a built-in function that takes an instance and a class and returns True if the instance is an instance of the class or a subclass of the class and False otherwise - isinstance(instance, Class)
# issubclass - a built-in function that takes two classes and returns True if the first class is a subclass of the second class and False otherwise - issubclass(ChildClass, ParentClass)
# inheritance - when a class inherits from another class - the child class gets all of the methods and attributes from the parent class
# super - a function that allows you to call a method from the parent class - super().__init__()
# dunder methods - methods that start and end with double underscores - __init__ is a dunder method
# encapsulation - the idea that data should not be directly accessed outside of a class - use getters and setters to access and change data
# getters and setters - methods that allow you to get and set data on an instance of a class
# __repr__ - a dunder method that returns a string representation of an instance of a class - used for debugging
# __str__ - a dunder method that returns a string representation of an instance of a class - used for displaying information to the user
# __add__ - a dunder method that allows you to add two instances of a class together - used for operator overloading
# __len__ - a dunder method that allows you to get the length of an instance of a class - used for operator overloading
# inheritance is when a class inherits from another class and gets all of the methods and attributes from the parent class
# super is a function that allows you to call a method from the parent class - super().__init__() - super() returns a proxy object that delegates method calls to a parent or sibling class
