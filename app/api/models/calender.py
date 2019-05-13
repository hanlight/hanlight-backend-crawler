from app import db

from app.utils.models import BaseModel
from app.utils.mixins import BaseMixin


class CalenderModel(BaseModel, BaseMixin):
    __tablename__ = 'api_calender'

    date = db.Column(db.Date, nullable=False)
    detail = db.Column(db.String(50), nullable=False)

    def __init__(self, date: str, detail: str):
        self.date = date
        self.detail = detail

    @staticmethod
    def add_schedule(date, detail: str):
        if not CalenderModel.get_schedule(date, detail):
            return CalenderModel(date, detail).save()

    @staticmethod
    def get_schedule(date: str, detail: str):
        return CalenderModel.query.filter_by(date=date, detail=detail).first()