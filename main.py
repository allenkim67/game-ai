from src import Connect4
from src import GameUI
from src.AI import AI
import sys


ai = AI(Connect4, './data/ai.json')


def train():
    for i in range(10):
        GameUI.play(Connect4(), ai, train_mode=True)
        print(i)
    ai.save()


def play():
    GameUI.play(Connect4(), ai)


if "--train" in sys.argv:
    train()
else:
    play()
