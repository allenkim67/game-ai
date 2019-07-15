import os.path
import json


class GameTree:
    def __init__(self, Game, filepath):
        self.Game = Game
        self.filepath = filepath

        if os.path.isfile(filepath):
            with open(filepath) as f:
                self.tree = json.load(f)
        else:
            self.tree = {}

    def get(self, state):
        return self.tree.get(state) or self._add(state)

    def _add(self, state):
        game = self.Game(state)
        node = [{
            "n": 0,
            "q": 0,
            "action": action,
            "player": game.player()
        } for action in game.actions()]
        self.tree[state] = node
        return node

    def save(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.tree, f)
