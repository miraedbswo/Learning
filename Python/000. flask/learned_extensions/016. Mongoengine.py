from mongoengine import *

# pip install mongoengine 으로 install 할 수 있다.
# 참조 : http://docs.mongoengine.org/guide/connecting.html

connect('Mongo')
# mongoDB는 스키마가 없는 Nosql Database 이다.
# 테이블이 없는 구조를 통해 데이터베이스를 구현해 볼 수 있다.
# 일반 ORM의 구조와 비슷함.

# 사용자의 필드와 사용자가 저장할 데이터 자료형을 명시해야 함


class User(Document):

    # 틀은 Field(max_length=None, min_length=None, **kwargs) 대충 이러함
    # required = True == 필수로 입력되어야 하는 값
    # primary_key = True 일 경우 식별자가 됨
    # unique = True 일 경우 유일한 값이어야 함.

    username = StringField(primary_key=True)
    # 식별자일 경우 필수로 입력되어야 하기 때문에 required는 사용하지 않았음.

    password = StringField(required=True)

    nickname = StringField(default='test_nickname', max_length=6)
    # default 값을 지정할 수 있음


from flask import Flask, Response, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def using_mongo_engine():
    username = request.form['username']
    password = request.form['password']
    nickname = request.form['nickname']
    # 세 가지 값 입력 받음

    User(
        username=username,
        password=password,
        nickname=nickname
    ).save()
    # User에 새로운 값 insert.

    return Response('successful', 200)


@app.route('/find', methods=['POST'])
def find_values_from_mongo():
    username = request.form['username']

    find_value = User.objects(username=username).first()
    # 입력받은 username이 User Collection에 존재할 경우, 그 값의 row를 가져옴.

    print(find_value)

    user = User.objects()
    print(list(user))
    # list casting

    print(find_value.username)
    # 찾은 value 안에서의 username을 출력함.


@app.route('/update', methods=['POST'])
def update():
    username = request.form['username']
    new_password = request.form['new_password']

    u = User.objects(username=username).first()

    print(u.password)
    # 현재 password

    u.update(password=new_password)

    print(u.password)
    # 바뀐 password 적용.


@app.route('/delete', methods='DELETE')
def delete():
    User.objects().delete()
    # delete of crud


if __name__ == '__main__':
    app.run()

