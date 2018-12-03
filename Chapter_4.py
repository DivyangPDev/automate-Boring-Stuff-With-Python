#Pracise Questions
# Q1) What is []?
# Empty List value

# 2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam?
#(Assume spam contains [2, 4, 6, 8, 10].)
#spam[3] = 'hello'

# For the following three questions, let’s say spam contains the list ['a','b', 'c', 'd'].
# Q3) What does spam[int('3' * 2) / 11] evaluate to?
# TypeError: list indices must be integers or slices, not float

# Q4) What does spam[-1] evaluate to?
# 'd'

# What does spam[:2] evaluate to?
# ['a','b']

# For the following three questions, let’s say bacon contains the list
# [3.14, 'cat', 11, 'cat', True].

# 6. What does bacon.index('cat') evaluate to?
# 1

# 7. What does bacon.append(99) make the list value in bacon look like?
# [3.14, 'cat', 11, 'cat', True, 99]

# 8. What does bacon.remove('cat') make the list value in bacon look like?
# [3.14, 11, 'cat', True, 99]

# 9. What are the operators for list concatenation and list replication?
# Operators for list concatenation is + and list replication is *

# 10. What is the difference between the append() and insert() list methods?
# The difference between append() inserts the item at the end of the list and insert() inserts item at the given index

# 11. What are two ways to remove values from a list?
# The two ways to remove values from a list are del and remove().
# For Example:
# spam = [3.14, 11, 'cat', True, 99]
# del spam[1] will remove the first item from the list value spam
# spam.remove('cat') will remove the first occurence of the cat from the list spam

# 12. Name a few ways that list values are similar to string values.
# List values are similar to string values as you can do indexing, slicing, using them with for loops, with len() and
# with the in and not in operator

# 13. What is the difference between lists and tuples?
# Lists are mutable objects while tuples are immutable objects. Tuples cannot be changed while List can be changed using indexes

# 14. How do you type the tuple value that has just the integer value 42 in it?
# spam = ((42,))

# 15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
# tuple(list) will get you the tuple form of a list value
# list(tuple) will get you the list form of a tuple values

# 16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
# references

# 17. What is the difference between copy.copy() and copy.deepcopy()?
# copy.copy() will make duplicate of a mutable value like list or dictionary but it doesnt copy inner lists
# deepcopy.copy() will make duplicate the of a mutable value like list or dictionary but it also copies inner lists

# Practise Projects

# spam = ['apples', 'bananas', 'tofu', 'cats']
#
# finalLstValue = ""
# def commaSpaces(lstvalue):
#     finalLstValue = ""
#     for item in range(len(lstvalue)):
#         finalLstValue += lstvalue[item] + ", "
#         if item == len(lstvalue)-1:
#             finalLstValue += "and " + lstvalue[item]
#
#     return finalLstValue
#
# print(commaSpaces(spam))

#Character Picture Grid

# grid = [['.', '.', '.', '.', '.', '.'],
# ['.', 'O', 'O', '.', '.', '.'],
# ['O', 'O', 'O', 'O', '.', '.'],
# ['O', 'O', 'O', 'O', 'O', '.'],
# ['.', 'O', 'O', 'O', 'O', 'O'],
# ['O', 'O', 'O', 'O', 'O', '.'],
# ['O', 'O', 'O', 'O', '.', '.'],
# ['.', 'O', 'O', '.', '.', '.'],
# ['.', '.', '.', '.', '.', '.']]
#
# for iIndex in range(len(grid[0])):
#     for oIndex in range(len(grid)):
#         print(grid[oIndex][iIndex], end=" ")
#     print('\n')
