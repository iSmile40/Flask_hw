from sqlalchemy import exc
import errors
from app import db
from datetime import datetime


class BaseModelMixin:

    @classmethod
    def by_id(cls, obj_id):
        obj = cls.query.get(obj_id)
        if obj:
            return obj
        else:
            raise errors.NotFound

    def add(self):
        db.session.add(self)
        try:
            db.session.commit()
        except exc.IntegrityError:
            raise errors.BadLuck


class Ads(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    text = db.Column(db.String(500), index=True)
    owner = db.Column(db.String(64), index=True)
    date_create = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())


    def __str__(self):
        return f'Advertisement {self.title}>'

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'text': self.text,
            'owner': self.owner,
            'date_create': self.date_create
        }
