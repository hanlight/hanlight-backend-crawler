from app import db

from app.utils.models import BaseModel
from app.utils.mixins import BaseMixin


class MealModel(BaseModel, BaseMixin):
    __tablename__ = 'api_meal'

    date = db.Column(db.Date, nullable=False)
    detail = db.Column(db.String(150), nullable=False)

    def __init__(self, date: str, detail: str):
        self.date = date
        self.detail = detail

    @staticmethod
    def add_lunch(date: str, detail: str):
        if not MealModel.get_lunch(date, detail):
            return MealModel(date, detail).save()

    @staticmethod
    def get_lunch(date: str, detail: str):
        return MealModel.query.filter_by(date=date, detail=detail).first()