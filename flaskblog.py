from flask import Flask

app = Flask(__name__)

@app.route("/aa")
@app.route("/bb")
def hello_world():
    return "<p>Hello, World!!</p>"

@app.route("/gay")
def gay():
    return "<p>gayaa</p>"


if __name__ == '__main__':
    app.run(debug=True)
