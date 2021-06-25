import json
from app import db
from models import SearchKeyword, CountKeyword, AlchemyEncoder
from sqlalchemy import func
from flask import jsonify
import datetime


db.create_all()

# add new row to SearchKeyword
# f = SearchKeyword(keyword="add", search_datetime=datetime.utcnow())
# db.session.add(f)

result = SearchKeyword.query.all()

# count no of keyword
ct = db.session.query(func.count(SearchKeyword.keyword)).distinct().scalar()
print("keyword list: ")
print(ct)

# select keyword from search_keyword
keywords = db.session.query(SearchKeyword.keyword).distinct().all()
print("keyword list: ")
print(keywords)

# count query result
cd = db.session.query(func.count(SearchKeyword.keyword), SearchKeyword.keyword)\
    .filter(SearchKeyword.search_datetime == datetime.datetime(2021, 6, 25))\
    .group_by(SearchKeyword.keyword).order_by(func.current_date()).all()
# type of query result
print("type of count result: ")
print(type(cd))
print("count word result (cd): ")
print(cd)
print("convert to JSON")
# sk = CountKeyword(count_date=datetime.utcnow(), count_output=cd.to_json())
# print(sk)
# print(json.dumps(sk, cls=AlchemyEncoder))


# jsonStr = dumps(cd)

# c = CountKeyword(count_output=cd.to_json(), count_date=func.current_date())
# print("result c:" + c)
# db.session.add(c)

# r = jsonify(list(cd))
# print(r[1])

# print(result)

# print(json.dumps(cd, cls=AlchemyEncoder))


db.session.commit()
