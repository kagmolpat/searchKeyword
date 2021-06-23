from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
import json
from sqlalchemy.ext.declarative import DeclarativeMeta

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)


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

    def to_join(self):
        return {
            'count_id': self.count_id,
            'count_date': self.count_date,
            'count_output': self.serialize_count
        }


class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)
