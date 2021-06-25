from flask import render_template, request, session, redirect, url_for, jsonify
from models import db, app, SearchKeyword, CountKeyword
from datetime import datetime
import json


@app.route("/", methods=["POST", "GET"])
def add_keyword():
    if request.method == "POST":
        # session.permanent = True
        keyword = request.form['keyword']
        print("Keyword : " + keyword)

        # Add data to DB
        keyword_search = SearchKeyword(keyword, search_datetime=datetime.utcnow())
        db.session.add(keyword_search)
        db.session.commit()

        return redirect(url_for("show_keyword", keyword=keyword))
    else:
        return render_template("index.html")


@app.route("/keyword/<keyword>", methods=["POST", "GET"])
def show_keyword(keyword):
    return f"<h1> Keyword : {keyword} </h1>"


if __name__ == '__main__':
    # db.create_all()
    app.run()
