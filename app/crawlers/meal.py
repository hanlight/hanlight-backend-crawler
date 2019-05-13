import requests, json, re, datetime

from app.api.models.meal import MealModel


# 정규식
pattern = re.compile('[가-힣]+')

date = datetime.datetime.now()

data = {
    'schl_cd': 'B100000662',
    'type_cd': 'M',
    'year': date.year,
    'month': date.month
}

# url 정의
url = "https://www.foodsafetykorea.go.kr/portal/sensuousmenu/selectSchoolMonthMealsDetail.do"

res = requests.post(url, data=data)

json_datas = res.text
json_datas = json.loads(json_datas)['list']

def show_data(data):
    try:
        # 날짜
        date = data['inqry_mm'] + data['dd_date'].zfill(2)
        date = datetime.datetime.strptime(date, '%Y%m%d').date()
        # lunch 배열 정리
        detail = data['lunch'].split(',')
        # 음식 이름만 가져오도록 정규표현식으로 처리
        detail = list(map(lambda food: pattern.findall(food)[0], detail))
        # list -> string으로 변환
        detail = ','.join(detail)
    except:
        return False

    # Meal에 레코드 추가
    MealModel.add_lunch(date, detail)

list(map(show_data, json_datas))