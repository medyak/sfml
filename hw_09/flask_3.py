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

