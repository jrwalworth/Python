# Week:          7
# Project No.    2
# File Name:     hw7project2.py
# Programmer:    Jason Walworth
# Date:          Math 8, 2020

# Problem Statement: Write a program that takes as input the gender of the child, the height of the mother
# in inches and the height of the father in inches. Output the estimated adult heigt of the child in inches.


# Overall Plan:
# 1. Print a welcome message to the user
# 2. Accept user input for gender of child
# 3. Accept user input for mother and father's height (in inches)
# 4. Evaluate which calculation to use based on child's gender
# 5. Calculate estimated adult height of the child (in inches)
# 6. Convert the estimated adult height to feet + inches


    
def main():
    print("This program will calculate the estimated adult height (in inches) for a child.")
    
    #Request user input for gender
    gender = (input("Please select the gender of the child (M/F):"))
    gender = gender.upper()
    print()
  
    

    #Evaluate if user input is M or F
    if gender == "M":
        #Request user input for mother and father heights
        motherH = eval(input("Please input the height of the mother (in inches):"))
        fatherH = eval(input("Please input the height of the father (in inches):"))
        print()
        #Calculate estimated adult male height of child in inches
        height = round(((motherH * (13/12)) + fatherH) / 2, 2)
        
        #Print estimated adult height of child to the screen
        print("The estimated adult height of the male child is:", height, "inches.")
        
        #Calculate the estimated adult height of the child in feet and inches
        feet = int(height // 12)
        inches = int(height % 12)
        
        #print the estimated adult height of the child in feet and inches.
        print("That's equal to a height of:", feet, "ft,", inches, "inches.")
        
    elif gender == "F":
        #Request user input for mother and father heights
        motherH = eval(input("Please input the height of the mother (in inches):"))
        fatherH = eval(input("Please input the height of the father (in inches):"))
        print()
        #Calculate estimated adult female height of child in inches
        height = round(((fatherH * (12/13)) + motherH) / 2, 2)
        
        #Print estimated adult height of child to the screen
        print("The estimated adult height of the female child is:", height, "inches.")
        
        #Calculate the estimated adught height of the child in feet and inches
        feet = int(height // 12)
        inches = int(height % 12)
        
        #print the estimated adult height of the child in feet and inches.
        print("That's equal to a height of:", feet, "ft,", inches, "inches.")
    
    else:
        print("This is not a valid gender.")
    

main()

