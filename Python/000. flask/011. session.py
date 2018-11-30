# 세션 (Session)

# 사용자 정보 파일을 브라우저에 저장하는 쿠키와 달리 세션은 서버 측에서 관리한다.
# 세션 ID를 부여하며 웹 브라우저가 서버에 접속해서 브라우저를 종료할 때까지 인증상태를 유지합니다.
# 사용자에 대한 정보를 서버에 두기 때문에 쿠키보다 보안에 좋지만, 사용자가 많아질수록 서버 메모리를 많이 차지하게 됨.

"""
session:
클라이언트가 서버에 접속 시 세션 ID를 발급

클라이언트는 세션 ID에 대해 쿠키를 사용해서 저장 ( 이 때 쿠키 이름은 JSESSIONID이다. )  ->

클라이언트가 서버에 다시 접속 시 이 쿠키를 이용해서 세션 ID 값을 서버에 전달
"""
from flask import Flask, request, session

app = Flask(__name__)


@app.route('/session', methods=['GET', 'POST', 'DELETE'])
def index():
    if request.method == 'DELETE':
        session.pop('username')
        # session.pop은 username을 출력하며 삭제함
        return 'session deleted'

    else:
        if 'username' in session:
            return 'Hello {}'.format(session['username'])
        # 세션 안에 'username'이 있으면 'Hello {username}'을 반환

        else:
            # 세션 안에 'username'이 없다면
            session['username'] = 'value'
            # 'username'을 'vaule'로 설정
            print(session['username'])
            # 출력
            return 'Session appended!'


if __name__ == '__main__':
    app.run(debug=True)
