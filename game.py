import board
import player
import card
import dice

class Game:
    # class constructor
    def __init__(self):
        # create a board
        Board board()
        # create a player
        Player player1('player')
        Player AI('AI')
        self.player1 = Player player1('player')
        self.AI = Player
        self.cur_player = player1

    def play(self):
        # take turn
        self.cur_player.take_turn()
        # switch players
        if (self.cur_player.name() == 'player') {
            self.cur_player = AI }
        else {
            self.cur_player = player1
            }
    def end(self):
        return self.cur_player.money == 0
