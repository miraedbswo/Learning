from flask import Flask
from flask_validation import Validator, json_required

# callsign-viper ( 프로젝트팀 이름 ) 에서 입력 데이터를 검증하기 위한 extension을 만들었음
# json 기반 요청 데이터를 처리해주는 라이브러리이다.


app = Flask(__name__)
Validator(app)
# Validator 에 Flask 인스턴스를 넣어줌으로써 validation을 사용할 수 있다


@json_required()
# Content-Type이 application/json 형태가 아닐경우 400 BAD REQUEST를 반환, json일 경우 200 OK.
# 입력 받은 데이터가 json인지를 검증해주는 데코레이터
@app.route('/')
def hello():
    return 'hello!'


from flask_validation import validate_keys
# validate_keys 는 요청받는 json의 형태를 제한하여 검증해주는 데코레이터이다.
# 필요하지 않은 다른 json 값을 받아오지 않을 수 있고, 필요한 데이터만 받아낼 수 있다.


@validate_keys(['name', 'age', {'position': ['lati', 'longi']}])
@app.route('/index', methods=['POST'])
def index():
    return 'index!'

# {"name": "Goming", "age": 17, "position": {"lati": 35.24, "longi": 127.681146}}
# 이런 식으로 json 타입을 보내는지 아닌지 검증을 해준다.


from flask_validation import validate_common, validate_with_fields, validate_with_jsonschema
# 이 외에도 여러가지 검증을 할 수 있는 데코레이터들이 있다.
# validate_common 데코레이터는, validate_keys 처럼 사용하지만, type까지 검증할 수 있다.


if __name__ == '__main__':
    app.run()
