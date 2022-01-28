# Week:          3
# Project No.    3
# File Name:     hw3project3.py
# Programmer:    Jason Walworth
# Date:          Feb. 3, 2020
#
# Problem Statement: Write a program to determine the length of a ladder required
#   to reach a given height when leaned against a house. Height and angle of ladder as inputs.
#   Formula to use: Length = height / sin (angle)
#
# Overall Plan:
# 1. Print an initial welcoming message to the screen
# 2. Prompt the user for height of the house
# 3. Prompt the user for the angle of the ladder
# 4. Calculate the length of the ladder that is required to reach the top of the house
# 5. Print the whole number and the remainder results of the division performed


import math
from math import pi
from math import sin

def ladder():
    
    #print welcome message
    
    #prompt user for height of house
    house = eval(input("Please input the height of the house (in feet): \n"))
    
    #prompt user for angle of ladder
    angle = eval(input("At what angle is the ladder leaning up against the house? (in degrees): \n"))
    
    #calculate the radians, given the angle in degrees
    aRadian = (pi / 180) * angle
    #print(aRadian)
    #calculate the ladder length required to reach the roof of the house
    ladderLength = house / sin(aRadian) 
    
    #print results to the screen
    print("Your ladder will need to be", int(ladderLength), "ft in order to reach the roof of the house")
    
ladder()


