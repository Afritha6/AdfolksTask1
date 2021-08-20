from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)

class Topic(db.Model):
    topic_id = db.Column(db.Integer, primary_key=True)
    topic_name = db.Column(db.String(200))
    commment = db.Column(db.String(300))

# create db schema class
class TopicSchema(ma.Schema):
    class Meta:
        fields = ('topic_id', 'topic_name', 'commment')


# instantiate schema objects for todolist and todolists
topic_schema = TopicSchema(many=False)
topic_schemas = TopicSchema(many=True)


if __name__ == "__main__":
    app.run(debug = True)