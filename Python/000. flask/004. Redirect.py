from flask import Flask, redirect, url_for
# flask.app에 Flask, redirect, url_for를 import 한다.
"""
설명 :
redirect() = 인자의 값으로 다시 direct함
    
url_for() = 인자의 값의 절대 주소값를 리턴하는 함수
    ex ) 밑에서의 코드에서 url_for('hello_admin') 일 경우
    hello_admin 이라는 함수가 정의된 URL을 리턴. 즉, /admin이 리턴됨.
"""
app = Flask(__name__)


@app.route('/admin')
def hello_admin():
    return 'hello admin !'
    # /admin 에 접속할 경우 hello_admin 함수가 실행되며 return 값으로 'hello admin !'이라는 string이 반환


@app.route('/guest/<name>')
def hello_guest(name):
    return 'Hello %s !' % name
    # /guest/<name> name의 값에 따라 URL의 뒤에 있는 <name>은 달라짐.
    # hello_guest의 함수에서 'hello {name} !' 을 리턴.


@app.route('/user/<name>')
# /user/{name} 으로 접속하면 name 변수에 값이 들어감
def hello_user(name):
    if name == 'admin':
        # name이 admin 이면
        return redirect(url_for('hello_admin'))
        # hello_admin의 주소로 redirect해줌.
        # == localhost:8080/admin으로 접속 해 준다.
    else:
        return redirect(url_for('hello_guest', name=name))
        # name이 admin이 아니면,
        # url에서 /user/<name>에서 name 변수를 /guest/<name> 에서 name 변수 값으로 넣어준다.
        # 그 후 localhost:8080/guest/<name> 으로 다시 접속 해줌.


if __name__ == '__main__':
    app.run(debug=True, port=8080)
