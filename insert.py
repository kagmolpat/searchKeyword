import json
from sqlalchemy.sql.functions import current_date
from app import db
from models import SearchKeyword, CountKeyword, datetime, AlchemyEncoder
from sqlalchemy import func
from flask import jsonify

db.create_all()

# add new row to SearchKeyword
f = SearchKeyword(keyword="delete", search_datetime=datetime.utcnow())
db.session.add(f)

result = SearchKeyword.query.all()

# count no of keyword
ct = db.session.query(func.count('*')).select_from(SearchKeyword).scalar()

key = db.session.query(SearchKeyword.keyword).distinct().all()

cd = db.session.query(func.count(SearchKeyword.keyword), SearchKeyword.keyword)\
    .group_by(SearchKeyword.keyword).order_by(func.current_date()).all()

# filter_by(SearchKeyword.search_datetime == datetime(2021, 6, 21))

# jsonStr = dumps(cd)

# c = CountKeyword(count_output=jsonify(cd), count_date=func.current_date())
# db.session.add(c

# r = jsonify(list(cd))
# print(r[1])

# print(result)

print(key)
# type of query result
print(type(cd))
# count query result
print(cd)

# print(json.dumps(cd, cls=AlchemyEncoder))

print(ct)

db.session.commit()
