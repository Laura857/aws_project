import flask
from flask import Flask, request
import relationship

app = Flask(__name__)

@app.route('/iam/<relationshipType>/at/<relationshipDate>', methods=['POST'])
def showFram(relationshipType, relationshipDate):
    return relationship.relationship(relationshipType, relationshipDate)