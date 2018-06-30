# flask.app.Flask.add_url_rule
from flask import Flask

app = Flask(__name__)


def index():
    return 'Hi'
# 데코레이터 없이 함수를 선언


app.add_url_rule('/index', view_func=index, methods=['GET'])
# add_url_rule이라는 메서드로 리소스를 추가한다.
# rule, endpoint, view function 순서로 넣어주어야 하지만 지정해서 넣어줄 수도 있음. 메소드도 설정 가능

app.run(debug=True)
