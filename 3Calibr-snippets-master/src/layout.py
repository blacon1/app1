from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "aojh"

if __name__ == "__main__":
    app.run(port=1000)