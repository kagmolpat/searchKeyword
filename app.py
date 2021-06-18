from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)


@app.route("/", methods=["POST", "GET"])
def hello_world():
    return render_template("index.html")
    # return "Hello World"


if __name__ == '__main__':
    db.create_all()
    app.run()
