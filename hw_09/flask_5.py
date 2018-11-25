from flask import Flask
from flask import request, jsonify
import base64

import pickle
lr = pickle.load(open('lr.pckl', 'rb'))
cv = pickle.load(open('cv.pckl', 'rb'))

app = Flask(__name__)

@app.route("/predict",  methods=['POST'])
def hello():
    text = request.form.get('text')
    resp = {
        'predict_proba': lr.predict_proba(cv.transform([text]))[0][1],
        'text': text
    }
    return jsonify(resp)

app.run(host='0.0.0.0', port=12454)

# протестировать, запустив requests_for_flask_5.py
