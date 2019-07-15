class GameUI:
    @staticmethod
    def play(game, ai, train_mode=False):
        player_turn = False
        if not train_mode:
            game.show()
        while len(game.actions()):
            move = input() if player_turn else ai.get_move(game)
            if player_turn:
                move = int(move) - 1
            game = game.move(int(move))
            if not train_mode:
                player_turn = not player_turn
                game.show()
