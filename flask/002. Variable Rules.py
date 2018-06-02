from flask import Flask
app = Flask(__name__)


@app.route('/hello/<name>')
# route 데코레이터는 /hello라는 URL 뒤에 <name>이라는 variable이 있음.
# name이라는 변수는 <>에 감싼다
def hello_name(name):
    # name 이라는 variable를 인자로 받는 hello_name을 선언
    return 'hello %s !' % name
    # hello_name의 인자값인 name을 넣어 출력


@app.route('/User_Num/<int:num>')
# 뒤의 변수를 int형으로 선언.
# ex ) localhost:5000/User_Num/12 일 경우 num은 int형 변수인 12가 됨.
def Show_User_Num(num):
    # 12가 인자가 됨
    return 'Your user id is %d' % num
    # 문자열 포맷팅


@app.route('/User_Score/<float:score>')
# float형 변수
def Show_User_Score(score):
    return 'Your score is %s' % score
    # 위와 동일


if __name__ == '__main__':
    app.run()
