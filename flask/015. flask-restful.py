# flask-restful 모듈을 통한 REST API 구현

# REST는 Representational State Transfer라는 용어의 약자로서 웹의 장점을 최대한 활용할 수 있는 아키텍처
# 최근의 서버 프로그램은 다양한 브라우저와 안드로이폰, 아이폰과 같은 모바일 디바이스에서도 통신을 할 수 있어야 한다.

"""
REST의 특징
1. Uniform ( 유니폼 인터페이스 )
*
 
2. Stateless ( 무상태성 )
* REST는 무상태성 성격을 가짐. 작업을 위한 상태정보를 따로 저장하고 관리하지 않는다.
* 세션 정보나 쿠키 정보를 별도로 저장하고 관리하지 않기 때문에 API 서버는 들어오는 요청만을 단순히 처리하면 된다.

3. Cacheable ( 캐시 가능 )
* REST의 가장 큰 특징은 HTTP라는 기존 웹 표준을 그대로 사용하기 때문에 웹에서 사용하는 기존 인프라를 그대로 활용이 가능하다.

이 외에도 Self-descriptiveness( 자체 표현 구조 ), 
Client-server 구조 (클라이언트와 서버에서 개발해야 할 내용이 명확해지고 서로간 의존성이 줄어듬)
계층형 구조 가 있음.
"""
# more exception - http://meetup.toast.com/posts/92

from flask import Flask, abort, request
from flask_restful import Api, Resource
# flask_restful을 이용해 라우팅하려면, flask_restful.Resource를 사용하자.
# Resource 클래스를 상속받은 클래스는 하나의 uri에 대한 자원이 된다.

app = Flask(__name__)
api = Api(app)


class Hello_world(Resource):
    # class를 이용한 routing 구현
    def get(self):
        # http 메서드를 Hello_world의 메서드 이름으로 지정해준다
        # print(request.args['key'])
        # 요청 데이터에 접근할 때, 해당 key가 존재하지 않는다면 자동으로 '400 bad request'를 abort해 준다

        return {'name': 'goming', 'age': '17'}
        # 원래 flask routing에서는 오류가 나지만, flask-restful에서는 Content type이 application/json으로 반환됨.


api.add_resource(Hello_world, '/')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
