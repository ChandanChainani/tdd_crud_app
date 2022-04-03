from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/words")
def words():
    words = []
    return jsonify(words)
