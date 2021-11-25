import flask
from flask import Flask, request, render_template
import relationship

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/iam/<relationshipType>/at/<relationshipDate>', methods=['POST'])
def showFram(relationshipType, relationshipDate):
    return relationship.relationship(relationshipType, relationshipDate)