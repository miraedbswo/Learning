# 데코레이터는 함수 형태로 동작한다.


def decorator(function):
    def wrapper():
        print('Func will be called')

        return function()
    return wrapper
# decorator 함수에 인자로 전달된 function을 실행하여 그 결과를 반환하는 wrapper 함수 선언


def print_Hello():
    print('Hello!')


decorated_print_Hello = decorator(print_Hello())
# decorator 함수는 wrapper 함수를 출력하며 function을 받음.
decorated_print_Hello()
# wrapper 함수를 호출하며, Func will be called 가 출력되며 인자로 넣어준 function이 실행되고 그 결과를 반환한다.

# 데코레이터를 쓰는 이유는 이미 만들어져 있는 코드를 수정하지 않고도 여러가지 기능을 추가하기 위해서이다.
# 일반적으로 위처럼 데코레이터 함수를 호출하여 새로운 함수를 반환받는 구문은 잘 사용하지 않고, '@' 심볼을 사용


@decorator
def print_something():
    print('Hello!')


print_something()
# Func will be called와 Hello 가 출력된다 decorator를 사용했기 떄문
# @ 다음 줄에 함수를 선언해 주면 그 함수가 위에서 decorator(function)에서 function으로 들어가짐

# 인자를 가진 함수를 데코레이팅 하려면, 인자를 추가하고 함수를 호출할 때 인자를 전달하자.
def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@decorator
def print_msg(msg):
    print(msg)


print_msg('Hello?')

# 데코레이터 자체가 인자를 가져야 한다면 def를 하나 추가해주면 됨. 그리고 @decorator(*args) 해주면 됨
# 전달할 인자가 없더라도 함수를 호출하는 형태로 사용해야 한다.
