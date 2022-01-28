# Week:          8
# Project No.    1
# File Name:     hw8project1.py
# Programmer:    Jason Walworth
# Date:          March 14, 2020
#
# Problem Statement: Programming exercise #1 on Page 262. Write a program that computes and ouputs
# the nth Fibonacci number, where n is a value entered by the user.
#
#

# Overall Plan:
# 1. Print welcome message
# 2. Request user input for value, n
# 3. Use n to determine the nth fibonacci number
# 4. Print output to the screen.
#
#
def fib(n):

    #start the fibonacci sequence
    n1 = 0
    n2 = 1
    #initialize a counter
    counter = 0

    if n <= 0:
        print("This sequence has to start somewhere, please enter a positive number.")
    elif n == 1:
        print("The", n, "st fibonacci number is:", n1)
    
    else:
        while counter < n:
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            counter = counter + 1
    print("The " + str(n) + "th fibonacci number is: " + str(n3))
        
                
    
print("This program will compute the nth Fibonacci number based on the user's input.")
print()
print("Hi user.")
       
n = eval(input("Please input a value for n: "))
fib(n)

