import random
from flask import Flask, current_app, request
from src.AI import AI
from src.Connect4 import Connect4

app = Flask(__name__, static_url_path='/static')
ai = AI(Connect4, "data/ai.json")

@app.route('/connect4')
def home():
    return current_app.send_static_file('index.html')

@app.route('/connect4/api')
def ai_move():
    state = request.data
    game = Connect4()
    return str(ai.get_move(game))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)