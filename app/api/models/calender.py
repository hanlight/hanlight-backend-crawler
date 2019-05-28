from app import db

from app.utils.models import BaseModel
from app.utils.mixins import BaseMixin


class CalenderModel(BaseModel, BaseMixin):
    __tablename__ = 'Calendars'

    year = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Integer, nullable=False)
    detail = db.Column(db.String(50), nullable=False)

    def __init__(self, year: int, month: int, date: int, detail: str):
        self.year = year
        self.month = month
        self.date = date
        self.detail = detail

    @staticmethod
    def add_schedule(year: int, month: int, date: int, detail: str):
        if not CalenderModel.get_schedule(year, month, date, detail):
            return CalenderModel(year, month, date, detail).save()

    @staticmethod
    def get_schedule(year: int, month: int, date: int, detail: str):
        return CalenderModel.query.filter_by(year=year, month=month, date=date, detail=detail).first()