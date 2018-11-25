from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

app.run(port=5000, debug=True)

# Открыть в браузере http://127.0.0.1:5000
