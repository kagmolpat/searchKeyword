from app import db
from models import SearchKeyword, CountKeyword, datetime
from sqlalchemy import func
from flask import jsonify

db.create_all()

# add new row to SearchKeyword
f = SearchKeyword(keyword="test", search_datetime=datetime.utcnow())
db.session.add(f)

result = SearchKeyword.query.all()

# count no of keyword
ct = db.session.query(func.count('*')).select_from(SearchKeyword).scalar()

key = db.session.query(SearchKeyword.keyword).distinct().all()

cd = db.session.query(func.count(SearchKeyword.keyword), SearchKeyword.keyword) \
    .group_by(SearchKeyword.keyword).order_by(func.current_date()).all()

# jsonStr = dumps(cd)

# c = CountKeyword(count_output=jsonify(cd), count_date=func.current_date())
# db.session.add(c)


# r = jsonify(list(cd))
# print(r[1])

print(result)
print(key)
print(cd)
print(ct)


db.session.commit()
