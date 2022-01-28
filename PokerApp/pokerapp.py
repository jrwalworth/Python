#pokerapp.py - for pokerapp

from random import *
from graphics import *
from dieview import DieView
from button import Button

#poker interface

class Dice:
    def __init__(self):
        self.dice = [0] * 5
        self.rollAll()
        
    def roll(self, which):
        for pos in which:
            self.dice[pos] = randrange(1,7)
            
    def rollAll(self):
        self.roll(range(5))
    
    def values(self):
        return self.dice[:]
    
    def score(self):
        counts = [0] * 7
        for value in self.dice:
            counts[value] = counts[value] + 1
            
        #score
        if 5 in counts:
            return "Five of a Kind", 30
        elif 4 in counts:
            return "Four of a Kind", 15
        elif (3 in counts) and (2 in counts):
            return "Full House", 12
        elif 3 in counts:
            return "Three of a Kind", 8
        elif not (2 in counts) and (counts[1]==0 or counts[6] ==0):
            return "Straight", 20
        elif counts.count(2) == 2:
            return "Two Pair", 5
        else:
            return "Garbage", 0
            
            
class PokerApp:
    def __init__(self, interface):
        self.dice = Dice()
        self.money = 100
        self.interface = interface
    
    
    def run(self):
        while self.money >= 10 and self.interface.wantToPlay():
            self.playRound()
        self.interface.close()
        
    def playRound(self):
        self.money = self.money - 10
        self.interface.setMoney(self.money)
        self.doRolls()
        result, score = self.dice.score()
        self.interface.showResult(result, score)
        self.money = self.money + score
        self.interface.setMoney(self.money)
        
        
    def doRolls(self):
        self.dice.rollAll()
        roll = 1
        self.interface.setDice(self.dice.values())
        toRoll = self.interface.chooseDice()
        while roll < 3 and toRoll != []:
            self.dice.roll(toRoll)
            roll = roll + 1
            self.interface.setDice(self.dice.values())
            if roll < 3:
                toRoll = self.interface.chooseDice()
                

class GraphicsInterface:
    
    def __init__(self):
        self.win = GraphWin("Dice Poker", 600, 400)
        self.win.setBackground("green3")
        banner = Text(Point(300,30), "Python Poker Parlor")
        banner.setSize(24)
        banner.setFill('yellow2')
        banner.setStyle("bold")
        banner.draw(self.win)
        self.msg = Text(Point(300,380), "Welcome to the Dice Table")
        self.msg.setSize(18)
        self.msg.draw(self.win)
        self.createDice(Point(300,100), 75)
        self.buttons = []
        self.addDiceButtons(Point(300,170), 75, 30)
        b = Button(self.win, Point(300,230), 400, 40, "Roll Dice")
        self.buttons.append(b)
        b = Button(self.win, Point(300, 280), 150, 40, "Score")
        self.buttons.append(b)
        b = Button(self.win, Point(570,375), 40, 30, "Quit")
        self.buttons.append(b)
        self.money = Text(Point(300, 325), "$100")
        self.money.setSize(18)
        self.money.draw(self.win)
    
    def choose(self, choices):
        buttons = self.buttons
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()
        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()
    
    def setValue(self,value):
        for pip in self.pips:
            pip.setFill(self.background)
            
        for i in self.onTable[value]:
            self.pips[i].setFill(self.foreground)
            
        self.value = value
    
    def setColor(self, color):
        self.foreground = color
        self.setValue(self.value)
        
    def createDice(self, center, size):
        center.move(-3*size, 0)
        self.dice = []
        for i in range(5):
            view = DieView(self.win, center, size)
            self.dice.append(view)
            center.move(1.5*size, 0)   
            
    def addDiceButtons(self, center, width, height):
        center.move(-3*width, 0)
        for i in range (1, 6):
            label = "Die {0}".format(i)
            b = Button(self.win, center, width, height, label)
            self.buttons.append(b)
            center.move(1.5*width, 0)
            
    def setMoney(self, amt):
        self.money.setText("${0}".format(amt))
        
    def showResult(self, msg, score):
        if score > 0:
            text = "{0}! You win ${1}".format(msg, score)
        else:
            text = "You rolled {0}".format(msg)
        self.msg.setText(text)
    
    def setDice(self, values):
        for i in range(5):
            self.dice[i].setValue(values[i])
            
    def wantToPlay(self):
        ans = self.choose(["Roll Dice", "Quit"])
        self.msg.setText("")
        return ans == "Roll Dice"
    
    def chooseDice(self):
        #choices is a list of the indexes of the selected dice.
        choices = []
        while True:
            b=self.choose(["Die 1", "Die 2", "Die 3", "Die 4", "Die 5", "Roll Dice", "Score"])
            
            if b[0] == "D": #User clicked a die button
                i = eval(b[4])-1 #Translate label to die index
                if i in choices:
                    choices.remove(i)
                    self.dice[i].setColor("black")
                else:
                    choices.append(i)
                    self.dice[i].setColor("gray")
            else:
                for d in self.dice:
                    d.setColor("black")
                if b == "Score":
                    return []
                elif choices != []:
                    return choices
                
    def close(self):
        self.win.close()