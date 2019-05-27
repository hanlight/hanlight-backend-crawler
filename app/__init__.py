from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from apscheduler.schedulers.background import BackgroundScheduler


app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

from app.api.models import calender, meal, meal_order


try:
    db.create_all()
    print("DB 생성 성공")
except:
    print("DB 생성 실패")


from app.api.controllers.meal_order import meal_order


app.register_blueprint(meal_order)


from app.api.controllers import meal_order as meal_order_controller
from app.crawlers.meal import MealCrawler

scheduler = BackgroundScheduler()
scheduler.start()

scheduler.add_job(meal_order_controller.update_meal_order, 'cron', day='*/1')
scheduler.add_job(MealCrawler(), 'cron', day='*/3')