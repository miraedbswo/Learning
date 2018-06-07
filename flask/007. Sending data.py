from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('data.html')
    # '/' URL 접속하면 data.html 파일을 띄워준다.


"""
( data.html )
<!doctype html>
<html>
   <body>
   
      <form action = "http://localhost:8080/result" method = "POST">
         <p>Name <input type = "text" name = "Name" /></p>
         <p>Age <input type = "text" name = "Age" /></p>
         <p>Birthday <input type = "text" name = "Birthday" /></p>
         // input type이 text인 세 변수의 값을 입력받음
         <p><input type = "submit" value = "submit" /></p>
         // submit 함
      </form>
      
   </body>
</html>
"""


@app.route('/result', methods=['GET', 'POST'])
# GET과 POST 메소드를 사용 할 것이라고 명시
def result():
    if request.method == 'POST':
        # 메소드가 POST 면
        finally_result = request.form
        # request.form에는 {} 형태로  있음. 따라서 변수 finally_result = 딕셔너리
        return render_template('result.html', result=finally_result)
        # 데이터가 저장된 딕셔너리를 result라는 변수에 넣음.


"""
( result.html )
<!doctype html>
<html>
   <body>
      <table border = 0.5>
      
         {% for key, value in result.items() %}
         // 위의 코드에서 받아온 result 딕셔너리의 key, value 값을 for 문을 이용해 뽑아냄
            <tr>
               <th> {{ key }} </th>
               // key를 head ( 두꺼운 글씨 ) 로 넣음
               <td> {{ value }} </td>
               // value를 ( 일반 글씨 ) 로 넣음
            </tr>
         // tr = 테이블의 한 행  
         {% endfor %}
         // for 문이 여러번 돌아가기 때문에 다시 돌아가면 tr 태그가 다시 나오므로 2번째 행에 넣어짐
      </table>
      
   </body>
</html>
"""

if __name__ == '__main__':
    app.run(debug=True)
