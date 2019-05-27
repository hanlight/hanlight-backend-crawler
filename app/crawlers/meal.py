import requests, json, re, datetime

from app.api.models.meal import MealModel
from app import logger


class MealCrawler:
    def __init__(self):
        # 정규식
        self.pattern = re.compile('[가-힣]+')

        self.date = datetime.datetime.now()

        self.data = {
            'schl_cd': 'B100000662',
            'type_cd': 'M',
            'year': self.date.year,
            'month': self.date.month
        }

        # url 정의
        self.url = "https://www.foodsafetykorea.go.kr/portal/sensuousmenu/selectSchoolMonthMealsDetail.do"

        self.res = requests.post(self.url, data=self.data)

        self.json_datas = self.res.text
        self.json_datas = json.loads(self.json_datas)['list']

    def __call__(self, *args, **kwargs):
        logger.info('Starting MealCrawler...')
        list(map(self.save_data, self.json_datas))
        logger.debug('Meal Crawling Finish!!')

    def save_data(self, data):
        try:
            # 날짜
            date = data['inqry_mm'] + data['dd_date'].zfill(2)
            date = datetime.datetime.strptime(date, '%Y%m%d').date()
            # lunch 배열 정리
            detail = data['lunch'].split(',')
            # 음식 이름만 가져오도록 정규표현식으로 처리
            detail = list(map(lambda food: self.pattern.findall(food)[0], detail))
            # list -> string으로 변환
            detail = ','.join(detail)
        except:
            return False

        # Meal에 레코드 추가
        MealModel.add_lunch(date.month, date.day, detail)
        logger.debug('Add Meal Record in DataBase!!')