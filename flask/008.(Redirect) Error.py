from flask import Flask, redirect, url_for, abort, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))
    # login 함수 있는 곳으로 redirect


@app.route('/login')
def login():
    abort(401)
    # '/login' 에 접속할 경우 abort(args)
    # abort()는 괄호 안에 지정된 에러 코드를 가지고 요청을 중단한다.
    this_is_never_executed()
    # 앞에서 에러가 발생했을 경우 뒤의 코드는 실행되지 않는다.

# 에러 페이지를 변경하고 싶다면 errorhander() 데코레이터를 사용할 수 있다.


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html', 404)
    # 페이지의 상태 코드가 404를 Flask에게 말해 준다.
