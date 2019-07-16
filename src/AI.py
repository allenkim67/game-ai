import random
import math
from src.GameTree import GameTree


class AI:
    def __init__(self, Game, filepath):
        self.Game = Game
        self.tree = GameTree(Game, filepath)

    def save(self):
        self.tree.save()

    def get_move(self, game):
        for _ in range(len(game.actions()) * 25):
            self.train(game)
        return max(self.tree.get(game.state()), key=lambda c: c["n"])["action"]

    def train(self, game):
        next_game, history = self.next_node(game)
        reward = self.roll_out(next_game)
        self.back_prop(history, reward)

    def next_node(self, game, history=None):
        node = self.tree.get(game.state())
        history = history or []

        if len(node) == 0:
            return game, history

        unvisited = next((c for c in node if c["n"] == 0), None)
        if unvisited:
            return game.move(unvisited["action"]), history + [unvisited]

        best_uct = self.best_uct(node)
        return self.next_node(game.move(best_uct["action"]), history + [best_uct])

    def best_uct(self, parent):
        total_n = sum(c["n"] for c in parent)

        def uct(c):
            return c["q"] / c["n"] + 1.5 * (math.log(total_n) / c["n"])

        return max(parent, key=uct)

    def roll_out(self, game):
        while len(game.actions()):
            game = game.move(random.choice(game.actions()))
        return game.result()

    def back_prop(self, nodes, result, n=1):
        for node in nodes:
            node["q"] += self.reward(result, node["player"])
            node["n"] += n

    def reward(self, result, player):
        if result == 0:
            return 0
        else:
            return 1 if result == player else -1
