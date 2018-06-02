from flask import Flask
app = Flask(__name__)


@app.route('/python')
# URL 마지막에 슬래쉬가 있는 것과 없는 것의 차이
# 뒤에 슬래쉬가 있는 경우 웹 페이지에서
# localhost:5000/python에서는 정상 작동 하지만
# localhost:5000/python/ 에서는 404 Not Found가 뜬다
def print_hello():
    return 'Hello world!'


@app.route('/flask/')
# 슬래쉬가 없는 경우
# 둘 다 정상 작동 한다
def print_flask():
    return 'Hello flask!'


if __name__ == '__main__':
    app.run()

