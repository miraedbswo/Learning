from flask import Flask
app = Flask(__name__)


@app.route('/index1')
# 데코레이터를 통한 라우팅
# app.add_url_rule()을 통한 방법으로도 라우팅 할 수 있다
# 함수를 선언 해 주고 app.add_url_rule(rule, endpoint, 'view function') 으로 사용
def index1():
    # 해당 URL을 요청했을 때 실행되는 함수(view function)을 정의
    return 'Hello world'


@app.route('/index2')
def index2():
    return 'Hello Flask'


@app.route('/index3/<name>')
# 동적 URL 라우팅
def index3(name):
    # 변수를 '/index3/<name>' 에 들어갔을 때 실행되는 index3 함수에 인자로 넣어줌
    return 'Welcome ' + name
    # Welcome {name} 출력


@app.route('/index4/<int:num>')
# 동적 타입 변수 변환 (정수형)
def index4(num):
    return 'Your code is ' + num


if __name__ == '__main__':
    app.run()
