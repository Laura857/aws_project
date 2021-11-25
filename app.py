from datetime import datetime 
import json
import sys
import flask
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/iam/<relationshipType>/at/<relationshipDate>', methods=['POST'])
def showFram(relationshipType, relationshipDate):
    return relationship(relationshipType, relationshipDate)

def relationship(relationshipType : str, relationshipDate: str):
    now = datetime.now()
    daysNumber = (now - datetime.strptime(relationshipDate, '%Y-%m-%d')).days
    iconValueFrame1 = "i6946" if relationshipType == "single" else "i2259"
    iconValueFrame2 = "i7756" if relationshipType == "single" else "i18494"
    textFrame1 = str(daysNumber) + " days"
    textFrame2 = "23 matchs" if relationshipType == "single" else "35 times"
    
    value = {
        "frames": [
            {
                "index": 0,
                "text": textFrame1,
                "icon": iconValueFrame1
            },
            {
                "index": 1,
                "text": textFrame2,
                "icon": iconValueFrame2
            } 
        ]
    }
    response = json.dumps(value)
    print(response)
    return response