from flask import Blueprint, jsonify, make_response

from app import db, logger
from app.api.models.meal_order import FeedOrderModel


meal_order = Blueprint('meal_order', __name__, url_prefix='/meal-order/')


@meal_order.route('/update/')
def update_meal_order():
    feed_order = FeedOrderModel.latest_feed_order()

    new_feed_order = feed_order.order.split('-')
    last_class = new_feed_order.pop()
    new_feed_order.insert(0, last_class)
    new_feed_order = '-'.join(new_feed_order)
    feed_order.order = new_feed_order

    db.session.commit()
    logger.debug('Update MealOrder!!')


@meal_order.route('/get/')
def get_meal_order():
    return make_response(jsonify({
        "success": True,
        "data": {
            "feed_order": FeedOrderModel.latest_feed_order().order
        }
    }), 200)