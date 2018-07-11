# 불러서 쓰는 Python 모듈.
# 모듈은 mod1.py에서 컴파일 하는 것이 아닌 Module에서 import해 사용하는 것임.
# 내장 모듈들을 불러와 기능을 사용하는 경우가 많음.

# 다른 사람들이 이미 만들어 놓은 모듈을 사용할 수도 있고 우리가 직접 만들어서 사용할 수도 있다.
# 역할에 맞게 분리하기 위해 모듈을 사용한다. flask를 할 때에도 한 파일에 모든 기능을 구현하는 것이 아닌
# 여러 파일에 나누어 모듈을 import해 사용하는 식으로 사용된다.


def sum(a, b):
    return a+b


class cal():
    def mul(self, a, b):
        return a*b


# 함수를 불러와 사용할 수도 있고,
# class를 불러와 사용할 수도 있다.

num1 = 1
num2 = 2
# 변수 또한 가능하다

_private_num = 3
# _single_leading_underscore
# 주로 한 모듈 내부에서만 사용하는 private 클래스/함수/변수/메서드를 선언할 때 사용하는 컨벤션이다.
# 이 컨벤션으로 선언하게 되면 from module import *시 _로 시작하는 것들은 모두 임포트에서 무시된다.
# 그러나 파이썬은 완전한 private을 지원하지 않기 때문에 직접 import 하고 호출할 경우 사용이 가능하다.

__all_private_num = 4
# __double_leading_underscore
# 더블 언더스코어는 클래스 속성명을 맹글링하여 클래스간 속성명의 충돌을 방지하기 위한 용도로 사용된다.
# 하지만 이는 private을 위한 것이 아니며 private으로의 사용도 권장되지 않는다.


