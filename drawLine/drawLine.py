# Week:          4
# Project No.    3
# File Name:     hw4project3.py
# Programmer:    Jason Walworth
# Date:          Feb. 16, 2020
#
# Problem Statement: 1.	Programming Exercise #8, pg. 119.  
# Create a program that allows the user to draw a line segment and then display some
# graphical and textual information about the line segment.
# 
# Overall Plan:
# 1. Import graphics library
# 2. Create Gui for the following steps
# 3. Allow the user to make two mouse clicks for the line endpoints
# 4. Draw the midpoint of the segment in cyan
# 5. Draw the line
# 6. Print the length and the slope of the line
#
#
from graphics import *

def main():
    
    #Define GUI window
    win = GraphWin ('Week 4: Homework Project #3 - Line Segment', 700, 600)
    win.setBackground("White")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    Text(Point(5, 9.5), "Click me twice to draw a line!").draw(win)
    
    #Allow user to click two endpoints in the GUI window.
    p = win.getMouse()
    p.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
        
    #Draw a line between the two selected endpoints.
    drawLine = Line(p, p2).draw(win)
    
    #Display the length and slopce of the line.
    dx = p2.getX() - p.getX()
    dy = p2.getY() - p.getY()
    slope = dy / dx
    lineLength = ((dx**2) + (dy**2))**.5
    
    
    Text(Point(5, 5), "The line length is: " + str(lineLength)).draw(win)
    Text(Point(4.5, 4.5), "The slope of the line is: " + str(slope)).draw(win)
    #Close the program upon third click
    
    Text(Point(5, .25), "A third click will quit the program").draw(win)
    win.getMouse()
    win.close()
    
    
main()
