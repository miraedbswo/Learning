from flask import Flask
# flask 폴더 안의 flask를 import.
# 정확히는 flask.app.Flask import 하는 것

app = Flask(__name__)
# app에 현재 모듈의 이름을 인자로 넣음


@app.route('/')
# 데코레이터를 사용. URL을 빌드하기 위해.
def hello_world():
    # '/' 라는 URL에 접근할 경우 실행되는 함수를 정의.

    return 'hello world!'
    # 'hello world!' 라는 문자열 return
    # '/'라는 URL에 접근할 경우 실행되는 함수의 반환값으로 웹 페이지에 출력되는 값을 뜻함


if __name__ == '__main__':
    # app.py가 실행될 경우 __name__라는 변수에는 __main__의 값이 저장됨
    # 말 그대로 app.py를 실행할 경우 True, 아니면 False.
    # 이 파일이 import 되어 사용될 경우 __name__ == '__main__'이 성립하지 않음

    app.run()
    # 서버 실행
    """
    options :
    host = Default 인 경우 127.0.0.1 (localhost)으로 설정 됨
    '0.0.0.0' = 외부의 ip에서도 접근 가능
    
    port = 서버의 포트 설정. Default는 5000.
    http://127.0.0.1:5000/ 뒤의 포트 값을 설정해주는 옵션.
    
    debug = debug=True 일 경우 debug 모드로 서버 실행
    app.debug = True / app.run(debug=True) 두 가지 방법으로 디버그 사용 가능하다
    오류가 났을 경우 웹페이지 상에서 Traceback 창이 뜨고 오류를 보여주며 코드를 수정할 수 있음.
    """
