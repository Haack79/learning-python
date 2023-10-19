# in file: hi.py

greetings = ["Hello", "Bonjour", "Hola"]
# can get info from user
name = input("What is your name? ")
for greeting in greetings:
    print(f"{greeting}, World!")

print(f"Hello, {name}!")


# dont use key words like list, int etc for naming variables
# use snake_case for naming variables and functions in python
# use camelCase for naming classes in python
# use PascalCase for naming modules in python
# use UPPER_CASE for naming constants in python
# use _ for unused variables
# use _ for private variables
# use __ for private variables that are not inherited
# use __init__ for constructors
# use __str__ for string representation of objects
# use __repr__ for debugging
# use __ for special methods
# use __ for special variables or methods that are used by python
# use __ for special variables or methods that are used by python and are not inherited
# helpful methods are help() and dir(), and type()  and id()
# use type() to check the type of a variable
# use id() to check the memory address of a variable
# use dir() to check the methods of a variable
# use help() to check the documentation of a variable
# dir(str) will show all the methods of str
# help(str.upper) will show the documentation of str.upper
# numbers are immutable in python so you cannot change them in place like in javascript or ruby
# use math module for math functions
# int 2 3 4 etc  float 2.0 3.33 etc complex 42j 3.14j etc bool True False , int("5") -> 5  True and False are 1 and 0 , bool(0) -> False you can add them together
# use type conversion functions to convert between types
# use str() to convert to string
# use int() to convert to integer
# use float() to convert to float
# use bool() to convert to boolean
# use complex() to convert to complex
# use list() to convert to list
# use tuple() to convert to tuple
# use set() to convert to set
# use dict() to convert to dict
# use ord() to convert to unicode
# use chr() to convert to character
# use bin() to convert to binary
# use hex() to convert to hexadecimal
# use oct() to convert to octal
# use eval() to evaluate a string
# use exec() to execute a string
# use abs() to get absolute value
# use round() to round a number
# use pow() to get power of a number
# use min() to get minimum value
# strings are immutable in python so you cannot change them in place like in javascript or ruby
# use len() to get length of a string or list or tuple or set or dict
# single quotes and double quotes are the same in python  , can do multi line strings with triple quotes """ """ or ''' '''
# f strings are the same as string interpolation in javascript or ruby , f" {variable} " , f" {variable.upper()} "
# use \ to escape characters in strings , use \n for new line , use \t for tab , use \b for backspace , use \r for carriage return , use \f for form feed , use \ooo for octal value , use \xhh for hexadecimal value , use \uxxxx for unicode value , use \Uxxxxxxxx for unicode value
# use r" " for raw strings
# LISTS
# use [] to create a list or list() , use list() to convert to list , use list("string") to convert to list , string => list of characters
# use list.append() to add to end of list , list.append("item")
# use list.insert() to add to a specific index of list , list.insert(0, "item") , list.insert(-1, "item") , list.insert(len(list), "item") , list.insert(len(list) + 1, "item") , list.insert(-len(list), "item") , list.insert(-len(list) - 1, "item")
# use list.remove() to remove an item from list , removes first occurence
# use list.pop() to remove an item from list , removes last item if no index is specified
# use list.clear() to clear a list , list.clear()
# use list.copy() to copy a list , list.copy()
# use list.count() to count the number of occurences of an item in a list , list.count("item") , list.count(1)
# use list.sort() to sort a list , list.sort() , list.sort(reverse=True)
# use list.reverse() to reverse a list , list.reverse()
# use list.index() to get the index of an item in a list , list.index("item")
# use list.extend() to add items from another list to a list , list.extend(["item1", "item2"]) , list.extend(list2)
# len(list) to get length of list
# trailing commas are allowed in python and encouraged , [1, 2, 3,] , (1, 2, 3,) , {1, 2, 3,} , {1: "one", 2: "two", 3: "three",} [::-1] to reverse a list
# list is mutable in python so you can change it in place like in javascript or ruby
# list.sort() or alist(sorted, reverse=True) to sort a list
# my_list.remove("l")
# my_list.insert(2, "l")
# del my_list[0]
# last_item = my_list.pop()
# last_item
# my_list[2]
# "!" in my_list
# my_list.sort(reverse=True)
# my_list
# sorted(my_list, reverse=False)
# my_list
# TUPLES
# use () to create a tuple or tuple() , use tuple() to convert to tuple , use tuple("string") to convert to tuple , string => tuple of characters
# tuples are immutable in python so you cannot change them in place like in javascript or ruby
# use len(tuple) to get length of tuple
# tuples are sorted -
# tuples data dont change good for storing information in a row on a spreadsheet , tuples are faster than lists
# if want to define a tuple with one item use (1,) , (1) is not a tuple, (1) is an integer , (1,) is a tuple has to have trailing comma
# tuple unpacking - coordinates = (1, 2, 3) , x, y, z = coordinates , x , y , z
# SETS
# use to create a set or set() , use set() to convert to set , use set("string") to convert to set , string => set of characters
# sets are unordered and unindexed and unsorted and unchangeable and unique , sets are mutable in python so you can change them in place like in javascript or ruby
# use len(set) to get length of set
# sets are faster than lists
# sets are good for storing unique information , sets are good for storing unique information in a row on a spreadsheet , sets are good for storing unique information in a row on a spreadsheet that you want to change
# use set.add() to add an item to a set , set.add("item") only store immutable items in a set
# can run a hash function on a set to get a unique id for the set , hash(set) , hash(set) => 123456789
# use set.remove() to remove an item from a set , set.remove("item") , set.remove("item") => KeyError: "item" , use set.discard() to remove an item from a set , set.discard("item") , set.discard("item") => no error
# use set.clear() to clear a set , set.clear()
# use set.copy() to copy a set , set.copy()
# set() to create an empty set if use {} it will create an empty dictionary
# shortcut to check if an item is in a set , "item" in set , "item" in set => True , "item" not in set => False
# shortcut to check for mutability hash(5) hash('hello') , sets dont have an order
# DICTIONARIES
# use {} to create a dictionary or dict() , use dict() to convert to dictionary , use dict("string") to convert to dictionary , string => dictionary of characters
# dictionaries are unordered and unindexed and unsorted and changeable and unique , dictionaries are mutable in python so you can change them in place like in javascript or ruby
# use len(dict) to get length of dictionary
# dictionaries are faster than lists
# keys in dictionaries have to be immutable , keys in dictionaries have to be unique , keys in dictionaries have to be unique and immutable
# use dict["key"] to get a value from a dictionary , dict["key"] => "value" , dict["key"] => KeyError: "key"
# tuples can be a dictioary key , lists cannot be a dictionary key , sets cannot be a dictionary key , dictionaries cannot be a dictionary key
# use dict.get("key") to get a value from a dictionary , dict.get("key") => "value" , dict.get("key") => None
# can perform acctions on teh deictonary values , dict["key"].upper() , dict["key"].upper() => "VALUE"
# mydict.keys() to get the keys of a dictionary , mydict.values() to get the values of a dictionary , mydict.items() to get the items of a dictionary
# pprint module to print dictionaries in a pretty way
# name files with snake_case , name classes with PascalCase , name modules with PascalCase , name constants with UPPER_CASE , name private variables with _variable , name private variables that are not inherited with __variable , name constructors with __init__ , name string representation of objects with __str__ , name debugging with __repr__ , name special methods with __variable , name special variables or methods that are used by python with __variable , name special variables or methods that are used by python and are not inherited with __variable
# FUNCTIONS
# use def to define a function , def my_function(): , def my_function(): pass , def my_function(): return None , def m
# functions use indentation to define the scope of the function , whatever is indented after teh def is part of the function (the function declaration)
# can add labels to function arguments , def my_function(name="Nina"): , def my_function(name="Nina"): return name , if no lables then the order of the arguments matters
# dont use mutable types as default arguments , dont use mutable types as default arguments , dont use mutable types as default arguments
# if you call a list and define it in the argument it will be the same list,
def do_stuff(my_list=None):
    if my_list is None:
        my_list = []
    my_list.append("stuff")
    return my_list


# functions have scope
# truthy and falsy values in python , 0 is falsy , 0.0 is falsy , "" is falsy , [] is falsy , () is falsy , {} is falsy , None is falsy , False is falsy , everything else is truthy
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list1 == list2  # True
list1 is list2  # False , is checks if they are the same object in memory
my_set = {}
type(my_set)
my_set = set()
type(my_set)
my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)
2 in my_set
my_set
my_set.add(3)
my_set
my_other_set = {1, 2, 3}
my_set.union(my_other_set)
my_set.intersection(my_other_set)
my_tuple = (1,)
my_tuple
my_tuple[1] = 2

my_dict = {"key": "value"}
my_dict[0]
my_dict["hello"] = "world"
my_dict["foo"] = "bar"
my_dict
my_dict["hello"]
my_dict.get("hello")
my_dict["baz"]
"baz" in my_dict
my_dict.get("baz", "default response")
my_dict.keys()
my_dict.values()
my_dict.items()
my_list = [1, 2, 3]
my_list[0] = "a"
my_list
my_dict = {"hello": "world"}
my_dict["foo"] = "bar"
my_dict
my_set = {1, 2, 3}
my_set[
    0
] = "a"  # This will throw a TypeError my_set.add('a') my_set my_tuple = (1, 2, 3) my_tuple[0] = 'a' # This will throw a TypeError
colors = ["Red", "Green", "Blue", "Orange"]
for color in colors:
    print(f"The color is: {color}")
# Main Method in Python - if __name__ == "__main__": - if you run the file directly it will run the code in the if statement - if you import the file it will not run the code in the if statement
# can use the pass keyword to do nothing
# can run other code and import other files in the if statement
# -m pip install -U pylint - install pylint
# from random import randint - import randint from random module
# Libraries and Modules in Python - import random - import random module - random.randint(1, 10) - random is the module and randint is the function
# Modules in Python - import random - import random module - random.randint(1, 10) - random is the module and randint is the function
# python has built in mondules like random and math and datetime and os and sys and json and csv and statistics and sqlite3 and tkinter and turtle and tkinter and tkint
# can create your own modules by creating a file with a .py extension and importing it into another file - import my_module - my_module.my_function()
# tests are usually in a tests folder and are named test_*.py - test_my_module.py - import my_module - my_module.my_function()
# unit tests are important
# to install package use pip
# pypi.org  - python package index
