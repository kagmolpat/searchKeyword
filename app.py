from flask import render_template, request, session, redirect, url_for
from models import db, SearchKeyword, app
from datetime import datetime


@app.route("/", methods=["POST", "GET"])
def get_keyword():
    if request.method == "POST":
        session.permanent = True
        keyword = request.form['keyword']
        print("Keyword : " + keyword)

        # Add data to DB
        keyword_search_db = SearchKeyword(keyword, search_datetime=datetime.utcnow())
        db.session.add(keyword_search_db)
        db.session.commit()

        return redirect(url_for("keyword", keyword=keyword))
    else:
        return render_template("index.html")


@app.route("/<keyword>", methods=["POST", "GET"])
def show_keyword(keyword):
    return f"<h1> Keyword : {keyword} </h1>"


if __name__ == '__main__':
    db.create_all()
    app.run()
