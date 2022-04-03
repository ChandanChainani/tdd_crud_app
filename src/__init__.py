import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from . import commands

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)


@app.route("/words", methods=["GET", "POST", "PUT", "DELETE"])
def words():
    status, resp = 200, {}
    if request.method == "GET":
        resp = [{"id": word.id, "word": word.name} for word in Word.query.all()]
    if request.method == "POST":
        data = request.get_json()
        word = Word(name=data['word'])
        db.session.add(word)
        db.session.commit()
        status, resp = 201, {"id": word.id, "message": "Word added successfully"}
    if request.method == "PUT":
        data = request.get_json()
        word = Word.query.filter_by(id=data['id']).first()
        word.name = data['word']
        db.session.commit()
        resp = {"id": word.id, "message": "Word updated successfully"}
    if request.method == "DELETE":
        data = request.get_json()
        _id = Word.query.filter(Word.name==data['word']).delete()
        resp = {"id": _id, "message": "Word deleted successfully"}
    return jsonify(resp), status

