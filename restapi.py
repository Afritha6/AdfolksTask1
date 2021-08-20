from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic_name = db.Column(db.String(200))
    commment = db.Column(db.String(300))

# create db schema class
class TopicSchema(ma.Schema):
    class Meta:
        fields = ('id', 'topic_name', 'commment')


# instantiate schema objects for todolist and todolists
topic_schema = TopicSchema(many=False)
topic_schemas = TopicSchema(many=True)

@app.route("/topic", methods = ["POST"])
def add_topic():
    try:
        topic_name = request.json['topic_name']

        new_topic = Topic(topic_name=topic_name)
        
        db.session.add(new_topic)
        db.session.commit()

        return topic_schema.jsonify(new_topic)
    except Exception as e:
        return jsonify({"Error 409": "Invalid Request, please try again."})
        


if __name__ == "__main__":
    app.run(debug = True)