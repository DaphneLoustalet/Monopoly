import board
import player
import game
import dice

class startProperties:
    # class constructor
    def __init__(self):
        Property("Mediterranean Avenue", 60, 0, "brown", 0, 0, 0, 2, 10, 30, 90, 160, 250, 173, 191)
        Property("Baltic Avenue", 60, 1, "brown", 0, 0, 0, 4, 20, 60, 180, 320, 450, 137, 191)
        Property("Oriental Avenue", 100, 0, "light blue", 0, 0, 0, 6, 30, 90, 270, 400, 550, 83, 191)
        Property("Vermont Avenue", 100, 0, "light blue", 0, 0, 0, 6, 30, 90, 270, 400, 550, 47, 191)
        Property("Connecticut Avenue", 120, 1, "light blue", 0, 0, 0, 8, 40, 100, 300, 450, 600, 29, 191)
        Property("St. Charles Place", 140, 0, "magenta", 0, 0, 0, 10, 50, 150, 450, 625, 750, 9, 173)
        Property("States Avenue", 140, 0, "magenta", 0, 0, 0, 10, 50, 150, 450, 625, 750, 9, 137)
        Property("Virginia Avenue", 160, 1, "magenta", 0, 0, 0, 12, 60, 180, 500, 700, 900, 9, 119)
        Property("St. James Place", 180, 0, "orange", 0, 0, 0, 14, 70, 200, 550, 750, 950, 9, 83)
        Property("Tennessee Avenue", 180, 0, "orange", 0, 0, 0, 14, 70, 200, 550, 750, 950, 9, 47)
        Property("New York Avenue", 200, 1, "orange", 0, 0, 0, 16, 80, 220, 600, 800, 1000, 9, 28)
        Property("Kentucky Avenue", 220, 0, "red", 0, 0, 0, 18, 90, 250, 700, 875, 1050, 28, 9)
        Property("Indiana Avenue", 220, 0, "red", 0, 0, 0, 18, 90, 250, 700, 875, 1050, 65, 9)
        Property("Illinois Avenue", 240, 1, "red", 0, 0, 0, 20, 100, 300, 750, 925, 1100, 83, 9)
        Property("Atlantic Avenue", 260, 0, "yellow", 0, 0, 0, 22, 110, 330, 800, 975, 1150, 119, 9)
        Property("Ventnor Avenue", 260, 0, "yellow", 0, 0, 0, 22, 110, 330, 800, 975, 1150, 137, 9)
        Property("Marvin Gardens", 280, 1, "yellow", 0, 0, 0, 24, 120, 360, 850, 1025, 1200, 173, 9)
        Property("Pacific Avenue", 300, 0, "green", 0, 0, 0, 26, 130, 390, 900, 1100, 1275, 191, 28)
        Property("North Carolina Avenue", 300, 0, "green", 0, 0, 0, 26, 130, 390, 900, 1100, 1275, 191, 47)
        Property("Pennsylvania Avenue", 320, 1, "green", 0, 0, 0, 28, 150, 450, 1000, 1200, 1400, 191, 83)
        Property("Park Place", 350, 0, "blue", 0, 0, 0, 35, 175, 500, 1100, 1300, 1500, 191, 137)
        Property("Boardwalk", 400, 1, "blue", 0, 0, 0, 50, 200, 600, 1400, 1700, 2000, 191, 173)
        
    # determines if coordinates belong to a Property
    def isProperty(x, y):


class Property:
    # class constructor
    def __init__(self, name, cost, higher, color, hotels, houses, color_set, rent, rent1house, rent2house, rent3house, rent4house, renthotel, xcoord, ycoord):
        self.name = name
        self.cost = cost
        self.higher = higher
        self.color = color
        self.hotels = hotels
        self.houses = houses
        self.colorset = color_set
        self.rent = rent
        self.rent1house = rent1house
        self.rent2house = rent2house
        self.rent3house = rent3house
        self.rent4house = rent4house
        self.renthotel = renthotel
        self.xcoord = xcoord
        self.ycoord = ycoord

    def cost(self):
        if (self.hotels == 1) {
            return self.renthotel
        }
        else if (self.houses > 0) {
            if (self.houses == 1) {
                return self.rent1house
                }
            if (self.houses == 2) {
                return self.rent2house
                }
            if (self.houses == 3) {
                return self.rent3house
                }
            if (self.houses == 4) {
                return self.rent4house
                }
            }
        else if (self.colorset == 1){
                return self.rent*2
            }
        else {
            return self.rent
            }
        
        
