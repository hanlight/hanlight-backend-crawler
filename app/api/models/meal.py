from app import db

from app.utils.models import BaseModel
from app.utils.mixins import BaseMixin


class MealModel(BaseModel, BaseMixin):
    __tablename__ = 'api_meal'

    date = db.Column(db.Date, nullable=False)
    lunch = db.Column(db.String(150), nullable=False)

    def __init__(self, date: str, lunch: str):
        self.date = date
        self.lunch = lunch

    @staticmethod
    def add_lunch(date, lunch):
        return MealModel(date, lunch).save()