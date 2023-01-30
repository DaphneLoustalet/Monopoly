from random import random
import player
import board
import game
import card

class Dice:
    def __init__(self):
        self.roll1 = 0
        self.roll2 = 0
        
    def roll(self):
        self.roll1 = (random.random()*10)%7
        self.roll2 = (random.random()*10)%7
        return self.roll1 + self.roll2
        
