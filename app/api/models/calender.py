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
    def add_schedule(date: str, detail: str):
        return CalenderModel(date, detail).save()