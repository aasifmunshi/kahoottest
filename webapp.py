from flask import Flask, render_template, request, jsonify
from threading import Thread
from kahoot import flood_bots

app = Flask(__name__)


def run_kahoot_bot(game_pin, nickname, num_bots):
    flood_bots(game_pin, nickname, num_bots)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start', methods=['POST'])
def start():
    game_pin = request.form['gamePin']
    nickname = request.form['nickname']
    amount = int(request.form['amount'])

    # Start the bot in a separate thread
    bot_thread = Thread(target=run_kahoot_bot, args=(game_pin, nickname, amount))
    bot_thread.start()

    return jsonify({'status': 'Bots are joining!'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
