from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/predict")
def hello():
    x1 = request.args.get('x1')
    x2 = request.args.get('x2')
    return "Hello World! " + str(
        int(x1)**2 + int(x2)
    )

app.run()

# Открыть в браузере http://localhost:5000/predict?x1=5&x2=2
