#! /usr/bin/env python3

#Practice Questions
# 1. What are escape characters?
# Escape characters lets you use characters that otherwise impossible to put into a string. An escape character
# consists of a backslash (\n) followed by the character you want to add to the string

# 2. What do the \n and \t escape characters represent?
# \n escape character represents new newlines
# \t escape characters represents tab

# 3. How can you put a \ backslash character in a string?
# You can put a \backslash character in a string by making it a raw string.

# 4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it
#a problem that the single quote character in the word Howl's isn’t escaped?
# Because it is enclosed by double quotes

# 5. If you don’t want to put \n in your string, how can you write a string with newlines in it?
# By using triple quotes

# 6. What do the following expressions evaluate to?
# • 'Hello world!'[1]
# 'e'

# • 'Hello world!'[0:5]
# 'Hello'

# • 'Hello world!'[:5]
# 'Hello'

# • 'Hello world!'[3:]
# 'lo world!'

# 7. What do the following expressions evaluate to?
# • 'Hello'.upper()
# 'HELLO'

# • 'Hello'.upper().isupper()
# True

# • 'Hello'.upper().lower()
# 'hello'

# 8. What do the following expressions evaluate to?
# • 'Remember, remember, the fifth of November.'.split()
# ['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']

# • '-'.join('There can be only one.'.split())
# 'There-can-be-only-one'

# 9. What string methods can you use to right-justify, left-justify, and center a string?
# right-justify - rjust()
# left-justify - ljust()
# center a string - center()

# 10. How can you trim whitespace characters from the beginning or end of a string?
# beginning - lstrip()
# end - rstrip()

# Practise Project

tableDataList = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        del colWidths[i]
        colWidths.insert(i,len(max(tableData[i], key=len)))

    maxWidth = max(colWidths)
    tableLength = len(tableData[0])
    for i in range(tableLength):
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(maxWidth),end=" ")
        print("")

printTable(tableDataList)
