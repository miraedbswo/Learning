from flask import Flask
from flask import Blueprint

# flask application은 blueprint들의 집합으로 고려한다.
# blueprint의 집합체 = flask application 이라고 볼 수 있음.
# blueprint를 사용해서 모듈화 된 flask application을 만들기에 적합한 구조를 만들 수 있다.

blueprint = Blueprint('my_first_blueprint', __name__)

# blueprint의 구현은 이런 식으로 되어있다
#  def __init__(self, name, import_name, static_folder=None, static_url_path=None,
#               template_folder=None, url_prefix=None, subdomain=None, url_defaults=None)

# 2가지의 인자값은 name과 import_name이다.
# name은 중복될 수 없는 값이며, blueprint의 name을 설정해주는 인자 값이다.
# 모듈 마다 각각의 blueprint를 만들어 주는 경우 blueprint의 이름을 __name__으로 해도 좋다.


@blueprint.route('/')
# Blueprint의 객체인 blueprint를 사용해서 route를 해준다.
# Flask app 객체와 비슷한 route 형식을 가지고 있다.
def test_blueprint():
    return 'made my first blueprint!!'


app = Flask(__name__)
app.register_blueprint(blueprint, url_prefix='/prefix')
# Flask 객체를 얻어서, app 객체에 blueprint를 등록시켜준다.
# blueprint 들이 많다면, 각 모듈에서 blueprint를 import 해서 한 app 객체에서 묶어주는 작업이 필요하다.
# url_prefix는 **options 인자값에 해당되며, 해당 blueprint에 해당하는 URL의 prefix를 지정해 주는 option이다.

if __name__ == "__main__":
    app.run()
