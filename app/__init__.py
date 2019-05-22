from flask import Flask

from flask_sqlalchemy import SQLAlchemy


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