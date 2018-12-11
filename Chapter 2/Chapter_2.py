#! /usr/bin/env python3

#Precedence of the Boolean operators
# NOT operations first, then AND operator and then OR operator

# Q1) What are the two values of the Boolean data type? How do you write them?
# The two values of Boolean datatype are - True and False.
# We write by using Capital T and F.

# Q2) What are the three Boolean operators?
# The three boolean operators are OR, NOT and AND.

# Q3) Write out the truth tables of each Boolean operator (that is, every
# possible combination of Boolean values for the operator and what they evaluate to).

# The AND Operator's Truth table
# Expression        | Evaluates to
  # True and True   | True
  # True and False  | False
  # False and True  | True
  # False and False | False

# The OR Operator's Truth table
# Expression        | Evaluates to
  # True or True    | True
  # True or False   | True
  # False or True   | True
  # False or False  | False

# The NOT Operator's Truth table
# Expression        | Evaluates to
  # Not True   | False
  # Not False  | True

# Q4) What do the following expressions evaluate to?
# (5 > 4) and (3==5)                  --- False
# not (5 > 4)                         --- True
# (5 > 4) or (3==5)                   --- True
# not ((5 > 4) or (3==5))             --- False
# (True and True) and (True == False) --- False
# (not False) or (not True)           --- True

# Q5) What are the six comparison operators?
# Six Comparison Operators are given below
# < , > , <=, >=, != , ==

# Q6) What is the difference between the equal to operator and the assignment
#operator?
# Difference between Equal to operator and assignment operator is
# == is used to compare two values be it strings or boolean values or integers or floats
# = is used to assign a particular value to a variable on the left hand side of the assignment variable

# Q7) Explain what a condition is and where you would use one.
# Expressions evaluating to True or False is called a condition. We can use it to write programs that make decisions on what code to execute and what code to skip

# Q8) Identify the three blocks in this code:
# Three Blocks in below code -
# spam = 0
# if spam == 10:
# 	print('eggs')
# 	if spam > 5:
# 		print('bacon')
# 	else:
# 		print('ham')
# 	print('spam')
# print('spam')

# are -

# if spam > 5:
# 	print('bacon')
# else:
# 	print('ham')


# if spam == 10:
# 	print('eggs')
# 	if spam > 5:
# 		print('bacon')
# 	else:
# 		print('ham')
# 	print('spam')

# and

# spam = 0
# if spam == 10:
# 	print('eggs')
# 	if spam > 5:
# 		print('bacon')
# 	else:
# 		print('ham')
# 	print('spam')
# print('spam')

#Q9) Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is
# stored in spam, and prints Greetings! if anything else is stored in spam.
# while True:
# 	spam = input("enter the number")
# 	if spam == '1':
# 		print("Hello")
# 	elif spam == '2':
# 		print("Howdy")
# 	else:
# 		print("Greetings")
# 		break

# Q10) What can you press if your program is stuck in an infinite loop?
# ctrl + C can be used to get out of infinite loop.

# Q11) What is the difference between break and continue?
# Break exits the loop mechanism while continue starts the iterating again from the start

# Q12) What is the difference between range(10), range(0, 10), and range(0, 10, 1)
#in a for loop?
#There is no difference between range(10) and range(0,10) and range(0,10,1)

# Q13) Write a short program that prints the numbers 1 to 10 using a for loop.
#Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
#Writing a program to print the numbers from 1 to 10 using for loop
# j=0
# for j in range(1, 11):
# 	print(j)

# Writing a program to print the numbers from 1 to 10 using while loop
# i=0
# while i < 11:
# 	print(i)
# 	i+=1

# Q14) If you had a function named bacon() inside a module named spam, how
#would you call it after importing spam?

#I would call it like this -  spam.bacon()
