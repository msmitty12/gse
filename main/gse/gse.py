from flask import Flask
app = Flask(__name__)

@app.route("/gse")
def gse():
    return "Tim is poop."

if __name__ == '__main__':
    app.run()
