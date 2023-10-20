li = []
# can have any number of elements and diff data types
# list slicing is a lot like string slicing
my_items = ['book', 'shoes', 'hat', 'cat', 'dog']
print(my_items[0::2])
# lists are mutalbe, can mutate them
# with list slicing you are creating an entirely new list. 
# copy a list list[:]
# if you assign a list to another list then any changes to the new list will change the list it points to.

#MATRIX array with arrays in it. 
matrix = [
    [],
    [],
    [],
]
# function len(), 
# methods .append - changes list in place, doesnt return anything just changes original list
my_items.append('hello')
# insert(indx, value), extend, 
# removing - .pop(indx?)-returns what it removes, remove(value) - does in place
# .clear(), .index(value) or index.(value, startlook at indx, stop at indx)
# list (value in list)  ('book' in my_items), count(value) counts how many time value occurs
# sort() sorts in place and method, function sorted makes a new array
# .reverse() 
# range(start, stop) can do list(range(1,100)) gets list with numbers 1 to 100
# .join('') works to make string  ' '.join([item, item, item])
# list unpacking a,b,c = [1,2,3]
# a,b,c, *other = [1,2,3,4,5,6,7,8,9]
