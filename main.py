from flask import Flask

app = Flask(__name__)

@app.route("/")
def ping():
    return "ok", 200

app.run(host="0.0.0.0", port=8080)