from flask import Flask, request, Response

app = Flask(__name__)
# HTTP는 Stateless 라는 특징을 가진다.
# 한번의 요청과 응답을 거치면 응답을 받은 후에 유지되지 않고 끊긴다
# login을 해야만 들어가지는 mypage 같은 기능들을 구현하려면 로그인이 유지되어야 하는데
# HTTP 특성상 stateless이기 때문에 cookie나 session을 통해 강제로 statefull 상태를 유지하도록 만들어준다.

"""
cookie :
쿠키에는 클라이언트 로컬에 저장되는 키와 값이 들어있는 작은 데이터 파일이다.
일정 시간동안 데이터를 저장할 수 있다.

클라이언트가 서버에게 Request를 보낸다. ( 클라이언트가 브라우저로 웹 페이지에 접속 )
서버는 웹페이지를 전송할 때 쿠키까지 전송한다
클라이언트가 요청한 웹페이지를 전송받으면서 쿠키 하드에 저장한다.
쿠키는 클라이언트 쪽에 저장되며 클라이언트를 재받문시 cookie를 같이 request하는 방식임. 

Response Header에 Set-cookie 속성을 사용하면 클라이언트에 쿠키를 만들 수 있다.

쿠키의 예시:
자동 로그인, "오늘 더 이상 이 창을 보지 않음" 등등.
"""


@app.route('/cookie', methods=['GET', 'POST'])
def send_cookie():
    if request.method == 'GET':
        response = Response('cookie')
        # 쿠키를 주려면 Response 객체가 필요하다
        response.set_cookie('cookie', 'value')

        return response
    elif request.method == 'POST':
        response = Response('Hi')
        response.set_cookie('cookie', '', expires=0)

        # 쿠키 제거는 expires를 0으로 해주면 된다

        return response
    else:
        return '', 405


if __name__ == '__main__':
    app.run(debug=True)
