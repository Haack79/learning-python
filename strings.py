# strings
# strings are used to represent text - strings are used to represent text in python - strings are used to represent text in python
# concatenate strings with + - concatenate strings with the + operator - concatenate strings with the + operator
# escape sequence " \' "
# formatted strings - formatted strings are strings that have placeholders for dynamic values - formatted strings are strings that have placeholders for dynamic values - formatted strings are strings that have placeholders for dynamic values
name = "brian"
age = 1000
print(f"hi {name}. you are {age} years old")
print("hi {}. you are {} years old".format(name, age))

# strings are immutable - strings are immutable - strings are immutable
# strinsg stored in memory and go 0123456789
# indexing - indexing is used to get a single character from a string
# start at 0 and go to the end of the string
# [start:stop:step] - slicing - slicing is used to get a substring from a string - slicing is used to get a substring from a string
selfish = "me me me"
print(selfish[0:5:1])  # me me
print(selfish[0:5:2])  # mm
print(selfish[::1])  # me me me
print(selfish[::-1])  # em em em - reverse string
print(selfish[0:7])  # me me m
print(selfish[::-1])  # em em em
# immutability means strings cannot be changed, cant change value in string but can reassign it
print('*' * 10) # *********
# can do methods in fstrings
print(f'{name} is {len(name)}')