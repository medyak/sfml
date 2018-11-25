
import pickle
lr = pickle.load(open('lr.pckl', 'rb'))
cv = pickle.load(open('cv.pckl', 'rb'))

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/predict")
def predict():
    text = request.args.get('text')
    if text is None:
        return "Чо?"

    return str(
        lr.predict_proba(
            cv.transform([text])
        )[0][1]
    )
app.run()


# http://localhost:5000/predict?text=Крупная+компания+производитель+и+дистрибьютор+охлажденной+мясной
