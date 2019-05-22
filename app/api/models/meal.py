from app import db

from app.utils.models import BaseModel
from app.utils.mixins import BaseMixin


class MealModel(BaseModel, BaseMixin):
    __tablename__ = 'Meals'

    month = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Integer, nullable=False)
    detail = db.Column(db.String(150), nullable=False)
    createdAt = None
    updatedAt = None

    def __init__(self, month: int, date: int, detail: str):
        self.month = month
        self.date = date
        self.detail = detail

    @staticmethod
    def add_lunch(month: int, date: int, detail: str):
        if not MealModel.get_lunch(month, date):
            return MealModel(month, date, detail).save()

    @staticmethod
    def get_lunch(month: int, date: int):
        return MealModel.query.filter_by(month=month, date=date).first()