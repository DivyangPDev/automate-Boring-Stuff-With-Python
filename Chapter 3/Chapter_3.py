#! /usr/bin/env python3

# Q1) Why are functions advantageous to have in your programs?
#Functions are advantageous to have in your programs because they are the best way to compartmentalize and organise your code
#They can be advantageous when they is a lot of repeated code to be usedself.

#Q2) When does the code in a function execute: when the function is defined or when the function is called?
#When the function is called.

#Q3) What statement creates a function?
#def function

#Q4) What is a difference between a function and a function call?
# Function is a defination of a function
# Ex:
# def hello():
#     print("Hello!!! People")
# Function call is just the function's name followed by paranthesis, possibly with some arguments in between the paranthesis.
#Ex:
#hello()

# Q5) How many global scopes are there in Python Program? How many local scopes?
#There is one global scope and one local scope created whenever a function is calledself.

# Q6) What happens to variables in a local scope when the function call returns?
# When the function call returns, the local scope is destroyed and all the variables in it are forgotten

# Q7) What is a return value? Can a return value be part of an expression?
# A return value is a value that the function call evaluates to. Like any value, a return value can be used as a part of an expression.

# Q8) If a function does not have a return statement, what is the return value of a call to that function?
# The return value of a call to that function is None

# Q9) How can you force a variable in a function to refer to the global variable?
# A global statement will force a variable in a function to refer to the global variables

# Q10) What is the data type of None?
# The datatype of None is NoneType
#
# Q11) What does the import areallyourpetsnamederic statement do?
# It will import all the variables and functions from the areallyourpetsnamederic module.

# Q12) If you had a function named bacon() in a module named spam, how would you call it after importing spam?
# spam.bacon()

# Q13) How can you prevent a program from crashing when it gets an error?
# Place the line that might cause an error in a try clause

# Q14) What goes in the try clause? What goes in the except clause?
# The code that could potentially cause an error goes in the try clause.
# The code that executes if an error happens goes in the except clause.

def collatz(number):
	if number % 2 ==0:
		evenNum = number //2
		print(evenNum)
		return evenNum
	else:
		oddNum = 3*number+1
		print(oddNum)
		return oddNum


if __name__ == "__main__":
	num = int(input("Enter number: "))
	result = collatz(num)
	while result != 1:
		result = collatz(result)
