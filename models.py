from app import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime


class SearchKeyword(db.Model):
    search_log_id = db.Column('search_log_id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    keyword = db.Column('keyword', db.String(255))
    search_datetime = db.Column('search_datetime', db.DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, keyword, search_datetime):
        self.keyword = keyword
        self.search_datetime = search_datetime


class CountKeyword(db.Model):
    count_id = db.Column('count_id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    count_date = db.Column('count_date', db.Date, nullable=False, default=datetime.utcnow())
    count_output = db.Column('count_output', db.String)

    def __init__(self, count_date, count_output):
        self.count_date = count_date
        self.count_output = count_output


# class CountSearchKeyword(db.Model):
#     count_keyword_id = db.Column('count_keyword_id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     keyword_name = db.Column('keyword_name', db.String(255))
#     count_keyword = db.Column('count_keyword', db.Integer)
#     count_datetime = db.Column('search_datetime', db.DateTime, default=func.current_date())
#
#     def __init__(self, keyword_name, count_keyword):
#         self.keyword_name = keyword_name
#         self.count_keyword = count_keyword
#         self.count_datetime = func.current_date()


