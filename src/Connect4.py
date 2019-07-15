import numpy as np
import copy
import json


class Connect4:
    def __init__(self, state=None):
        self._w, self._h = 7, 6

        self._state = json.loads(state) if state else {
            "board": [[0] * self._w] * self._h,
            "player": 1
        }

        self._state["board"] = np.array(self._state["board"])

    def state(self):
        return json.dumps({
            "board": self._state["board"].tolist(),
            "player": self._state["player"],
        })

    def player(self):
        return self._state["player"]

    def move(self, action):
        game = copy.deepcopy(self)
        for i in range(game._h):
            if game._state["board"][i, action] == 0:
                game._state["board"][i, action] = game._state["player"]
                break
        game._state["player"] = 1 if game._state["player"] == 2 else 2

        return game

    def actions(self):
        return [] if self.result() != 0 else [
            i for (i, piece) in enumerate(self._state["board"][-1]) if piece == 0
        ]

    def result(self):
        for player in [1, 2]:
            if any(all(piece == player for piece in line) for line in self._get_lines()):
                return player
        return 0

    def show(self):
        f = np.vectorize(lambda piece: {1: "x", 2: "o", 0: " "}[piece])
        print(f(np.flip(self._state["board"], 0)))

    def _get_lines(self):
        def get_diag(board):
            return [
                [board[x + k, y + k] for k in range(4)]
                for x in range(self._h - 3)
                for y in range(self._w - 3)
            ]

        rows = [row[i: i + 4] for i in range(self._w - 3) for row in self._state["board"]]
        cols = [col[i: i + 4] for i in range(self._h - 3) for col in np.rot90(self._state["board"])]
        f_diags = get_diag(self._state["board"])
        b_diags = get_diag(self._state["board"][:, ::-1])

        return rows + cols + f_diags + b_diags
