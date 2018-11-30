from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return '<html><body><h1>Hello World</h1></body></html>'
    # return 값을 html 폼으로 할 수 있다.
    # 하지만 python 코드에서 HTML를 생성하는 것은 번거롭기 때문에 사용하지 않습니다.


@app.route('/index')
def index_2():
    return render_template('hello.html')
    # HTML 코드을 반환하는 대신에 render_template() 함수 로 HTML 파일을 렌더링 할 수 있다.
    # Template 파일의 hello.html 파일을 렌더링함. == hello.html과 위 HTML 코드가 같다면 같은 결과 출력


"""
jinga2 템플릿 엔진을 사용하여 
HTML 코드에 넣어 템플릿이 렌더링 될 때 값으로 바뀌는 변수 및 표현식 사용 가능 ( Python 표현식과 동일 )
ex ) {% for key, value in result.iteritems() %}
         {{ key }}
         {{ value }}
     {% endfor %}

Jinga2 템플릿 엔진은 HTML과 구분하기 위해 다음 구분 기호를 사용
{% ~~~ %} ex ) {% if variable>60 %} {% else %} {% endif %}
{{ ~~~ }} ex ) {{name}}

등등 더 있지만 웹 템플릿과 Jinga2는 나중에 알아보려고 한다.
"""
if __name__ == '__main__':
    app.run(debug=True)
