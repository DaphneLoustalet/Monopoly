import board
import card
import dice
from graphics import *

class Player:
    # class constructor
    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.positionx = 191
        self.positiony = 191

    # taking a turn
    def take_turn(Dice dice):
        # roll dice and roll
        movement = dice.roll()
        while (movement > 0) {
             # if on bottom (191, 191) and not on far left (9, 191) move left
            if (on_bottom(self) &! far_left(self)) {
                self.positionx-=9
                movement--
                }
            # if on top (9, 9) and not on far right (191, 9) move right
            else if (on_top(self) &! far_right(self)) {
                self.positionx+=9
                movement--
                }
            # if on far left and not at top move up
            else if (far_left(self) &! on_top(self)) {
                self.positiony+=9
                movement--
                }
            # if on far right and not at bottom move down
            else {
                self.positiony-=9
                movement--
                }
            }
        # print player on new space
        self.print()

    def print(self):
        point = Circle(Point(self.positionx, self.positiony), 10)
        point.setFill("red")
        point.draw(win)

    def on_bottom(self):
        return (self.positiony == 191)

    def on_top(self):
        return (self.positiony == 9)

    def far_left(self):
        return (self.positionx == 191)

    def far_right(self):
        return (self.positionx == 9)
    
