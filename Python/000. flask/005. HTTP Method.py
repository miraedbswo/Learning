# HTTP 프로토콜이란, (HyperText Transper Protocol)
# 클라이언트와 서버 사이에 이루어지는 요청과 응답의 프로토콜이다.
# 클라이언트가 서버로부터 요청(request)를 보내면, 서버가 요청에 대하여 응답(response) 하여 전달한다.
"""
HTTP Methods
Get = 정보를 받아오기 위해 URL 형식으로 서버측에 데이터를 요청

Head = 메세지 헤더 취득
    Get과 비슷하나 문서를 요청하는 것이 아닌 문서 정보를 요청함.
    == HTTP 헤더 정보만 보냄

Post = 내용 전송
    클라이언트에서 서버로 어떤 정보를 전송함.

Put = 내용 갱신 전송
    Post랑 비슷하지만 Put은 내용을 갱신해서 전송함.
    Put은 클라이언트 측이 서버측 구현에 관여하는 것으로 세밀한 Post를 더 많이 쓴다고 함.

Delete = 파일 제거
"""
from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'Hi %s' % name
# /success/<name>에서의 name을 넣은 문자열 반환


@app.route('/login', methods=['POST', 'GET'])
# route는 default일 경우 자동으로 'GET' 이지만 HTTP method를 지정해 줄 수 있다.
def login():
    if request.method == 'POST':
        # 요청 메소드가 POST일 경우 == 클라이언트에서 서버로 정보를 전송한 경우
        user = request.form['name']
        # user라는 변수에 요청을 받은 form 안에서 name을 파라미터로 넣어 정의함
        return redirect(url_for('success', name=user))
        # success라는 변수가 있는 주소에 redirect. success에서 name은 앞에서 선언한 user로 넣어줌.
    else:
        user = request.args.get('name')
        # name이라는 args를 get해서 user에 넣음
        return redirect(url_for('success', name=user))
        # name 매개 변수에 해당하는 값은 전과 같이 '/success'URL로 전달한다.


# POST를 통해서 클라이언트에서 정보를 받아오기 위해서는
# HTML 등을 통해서 받아 와야 하는데, document에서는 html을 사용한 template를 사용한다.
"""
templete ( login.html )

<html>
    <body>
        <form action = "http://localhost:5000/login" method = "post">
        // http://localhost:5000/login 의 method == post
            <p>Enter Name:</p>
            <p><input type = "text" name = "name"/></p>
            // text 형태로 input 함 name을 선언할 수 있음 ( 변수명 )
            <p><input type = "submit" value = "submit"/></p>
            // input type을 submit으로 하면 post하는 것. 서버로 전송함
        </form>
    </body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)

# http://localhost:5000/login URL의 경우 서버를 run 한 후 template로 들어가서 html을 실행시켜 쓸 수 있다.
