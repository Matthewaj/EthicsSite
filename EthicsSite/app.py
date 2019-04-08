from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index_page():
    return render_template("index_template.html")


@app.route("/game")
def game_page():
    return render_template("game.html", title="Ethics Game")

if __name__ == '__main__':
    app.run()
