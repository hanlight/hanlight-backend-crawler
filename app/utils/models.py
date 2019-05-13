from app import db


class BaseModel(db.Model):
    __abstract__ = True

    pk = db.Column(db.Integer, primary_key=True)
    createdAt = db.Column(db.DateTime, default=db.func.current_timestamp())
    updatedAt = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())