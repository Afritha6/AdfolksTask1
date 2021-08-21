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
topics_schemas = TopicSchema(many=True)

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
        
@app.route("/topic/<int:id>/comment", methods=["PUT"])
def update_comment(id):

    updtae_comment = Topic.query.get_or_404(int(id))

    try:
        commment = request.json['commment']

        updtae_comment.commment = commment
        db.session.commit()
    except Exception as e:
        return jsonify({"Error": "Invalid request, please try again."})
        
    return topic_schema.jsonify(updtae_comment) 
        

@app.route("/topic", methods = ["GET"])
def get_topic():
    get_topic = Topic.query.all()
    result_set = topics_schemas.dump(get_topic)
    return jsonify(result_set)

@app.route("/topic/<int:id>", methods=["GET"])
def get_specific_topic(id):
    specific_topic = Topic.query.get_or_404(int(id))
    return topic_schema.jsonify(specific_topic)


@app.route("/topic/<int:id>", methods=["PUT"])
def update_topic(id):

    updtae_topic = Topic.query.get_or_404(int(id))

    try:
        topic_name = request.json['topic_name']

        updtae_topic.topic_name = topic_name
        db.session.commit()
    except Exception as e:
        return jsonify({"Error": "Invalid request, please try again."})
        
    return topic_schema.jsonify(updtae_topic) 

if __name__ == "__main__":
    app.run(debug = True)