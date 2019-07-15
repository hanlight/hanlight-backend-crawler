import logging

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from apscheduler.schedulers.background import BackgroundScheduler


app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

logger =logging.getLogger()
logging.basicConfig(level=logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

from app.api.models import calender, meal, meal_order
try:
    db.create_all()
    print("DB 생성 성공")
except:
    print("DB 생성 실패")

from app.crawlers import meal
from app.api.controllers import meal_order as meal_order_controller
from app.api.controllers.meal_order import meal_order
from app.crawlers.meal import MealCrawler


app.register_blueprint(meal_order)

scheduler = BackgroundScheduler()
scheduler.start()

scheduler.add_job(meal_order_controller.update_meal_order, 'cron', day_of_week='mon')
scheduler.add_job(MealCrawler(), 'cron', day='*/3')

MealCrawler()()