#GUI Poker 

from pokerapp import PokerApp
from textpoker import TextInterface
from pokerapp import GraphicsInterface


inter = GraphicsInterface()
app = PokerApp(inter)
app.run()
print("Program complete. Window should appear.")