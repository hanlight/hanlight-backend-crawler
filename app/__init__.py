from flask import Flask

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

from app.api.models import calender


try:
    db.create_all()
    print("DB 생성 성공")
except:
    print("DB 생성 실패")