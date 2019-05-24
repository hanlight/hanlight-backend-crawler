from app import db
from app.utils.models import BaseModel
from app.utils.mixins import BaseMixin


class FeedOrderModel(BaseModel, BaseMixin):
    __tablename__ = 'MealOrders'

    order = db.Column(db.String, nullable=False)
    count = db.Column(db.Integer, nullable=False)

    def __init__(self, order: str, count: int):
        self.order = order
        self.count = count

    @staticmethod
    def add_feed_order(order: str, count: int):
        return FeedOrderModel(order, count).save()

    @staticmethod
    def latest_feed_order():
        return FeedOrderModel.query.order_by(FeedOrderModel.createdAt.desc()).limit(1).first()

    @staticmethod
    def get_feed_order():
        return FeedOrderModel.query.filter_by(pk="1").first()