# driver code for entire Monopoly Game comes from here
import game
import board
import player
import card
import dice

# initialize game in constructor
Game game()

# play game
while (!game.end()){
    game.play()
}

# end game
game.over()
