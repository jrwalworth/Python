#button.py

#This is a reusable button class for gui

from graphics import *

class Button:
    
    '''A rectangular button to be displayed in GUI'''

    def __init__(self, win, center, width, height, label):
        '''Creates rectangular button. Sets active/inactive. Shows clicked or not clicked'''
        w, h = width/2.0, height/2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()
    
    def clicked(self, p):
        '''Returns true if button is active and point is inside rectangle'''
        return (self.active and
               self.xmin <= p.getX() <= self.xmax and
               self.ymin <= p.getY() <= self.ymax)
    
    def getLabel(self):
        return self.label.getText()
    
    def activate(self):
        "Sets this button to active"
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True
        
    def deactivate(self):
        "Sets this button to inactive"
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

class circButton:
    
    '''A circular button to be displayed in GUI'''

    def __init__(self, win, center, radius, label):
        '''Creates circular button. Sets active/inactive. Shows clicked or not clicked'''
        r = radius
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x+r, x-r
        self.ymax, self.ymin = y+r, y-r
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.circle = Circle(Point(x,y), radius )
        
        self.circle.setFill('lightgray')
        self.circle.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()
    
    def clicked(self, p):
        '''Returns true if button is active and point is inside circle'''
        return (self.active and
               self.xmin <= p.getX() <= self.xmax and
               self.ymin <= p.getY() <= self.ymax)
    
    def getLabel(self):
        return self.label.getText()
    
    def activate(self):
        "Sets this button to active"
        self.label.setFill('black')
        self.circle.setWidth(2)
        self.active = True
        
    def deactivate(self):
        "Sets this button to inactive"
        self.label.setFill('darkgrey')
        self.circle.setWidth(1)
        self.active = False
        
