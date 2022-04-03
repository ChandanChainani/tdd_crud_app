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


@app.route("/words", methods=["GET", "POST", "PUT", "DELETE"], defaults={"word_id": None})
@app.route("/words/<int:word_id>", methods=["GET"])
def words(word_id):
    status, resp = 200, {}
    if request.method == "GET":
        if word_id:
            word = Word.query.filter_by(id=word_id).first()
            resp = {
                "id": word.id,
                "name": word.name
            }
        else:
            resp = [{"id": word.id, "word": word.name} for word in Word.query.all()]
    elif request.method == "POST":
        data = request.get_json()
        if data.get("word") != None:
            word = Word(name=data['word'])
            db.session.add(word)
            db.session.commit()
            status, resp = 201, {"id": word.id, "message": "Word added successfully"}
        else:
            status, resp = 400, {"message": "missing parameter"}
    elif request.method == "PUT":
        data = request.get_json()
        if data.get("id") != None and  data.get("word") != None:
            word = Word.query.filter_by(id=data['id']).first()
            word.name = data['word']
            db.session.commit()
            resp = {"id": word.id, "message": "Word updated successfully"}
        else:
            status, resp = 400, {"message": "missing parameter"}
    elif request.method == "DELETE":
        data = request.get_json()
        if data.get("word") != None:
            _id = Word.query.filter(Word.name==data['word']).delete()
            resp = {"id": _id, "message": "Word deleted successfully"}
        else:
            status, resp = 400, {"message": "missing parameter"}
    return jsonify(resp), status

