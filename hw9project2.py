# Week:          9
# Project No.    2
# File Name:     hw9project2.py
# Programmer:    Jason Walworth
# Date:          April 4, 2020
#
# Problem Statement: Generate 6-digit random secure OTP using the secret class.
#
#

# Overall Plan:
# 1. Print welcome message
# 2. Define secure OTP as 6-digit 
# 3. Generate OTP at random
# 4. Display results to the screen


import random as r
import secrets

def randomOTP():
    #print welcome message
    print("This program will generate a OTP that is 6 digits long.")
    print()
    #set length of the OTP password
    otpLength = 6
    #initialize final random string
    finalOTP = ''
    #randomly generate digits from this sequence
    sequence = '0123456789'
    
    #randomly select each digit up to 6 digits.
    for n in range(otpLength):
        finalOTP = finalOTP + secrets.choice(sequence)
    
    #print random OTP to the screen
    print("The random string is: ", finalOTP)


randomOTP()

