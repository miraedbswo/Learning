# Instance Method의 정의는 클래스 내부에 정의되어있는 함수를 호출할 때,
# Instance(객체)를 필요로 한다는 조건이 있는 것을 알 수 있습니다.
# 이때 첫번째 매개변수는 항상 self


class InstMethod:
    def __init__(self):
        self.name = 'paphopu'

    def print_name(self):
        print('my name is {}'.format(self.name))


# 인스턴스를 선언한다.
name_instance = InstMethod()

# print_name 이라는 함수를 호출하기 위해선 객체를 먼저 정의해줘야합니다.
# 이것이 인스턴스 메소드입니다.

name_instance.print_name()


# # Class Method

# 첫번째 매개변수를 보내는 일을 하지 않고,
# 클래스 자기 자신을 첫번째 매개변수로 받는 차이가 있습니다.

# Class Method는 @classmethod 데코레이터를 이용하여 선언합니다.

# 이 경우 self를 사용하지 않고 cls를 매개변수로 사용하여
# Class Method를 이용합니다.


class ClassMethod:

    @classmethod
    def print_name(cls):
        print('my name is {}'.format(cls.__class__.__name__))


# 객체를 따로 선언해줄 필요없이 함수를 호출할 수 있습니다.
# 이것이 클래스 메소드입니다.
ClassMethod.print_name()
# >>my name is type


# # Static Method

# 인스턴스나 클래스를 인자로 받지 않습니다.
# static method의 특징은 클래스를 통해서도,
# 인스턴스를 통해서도 호출이 가능하다는 점입니다.

# Static Method는 클래스 내부에 선언되어 클래스 네임스페이드 안에 저장된다

class StaticMethod:

    @staticmethod
    def print_name(name):
        return '내 이름은 {} 입니다.'.format(name)


# 클래스를 통해서 호출가능

print(StaticMethod.print_name('minsoo'))
# >>내 이름은 minsoo 입니다.

# 인스턴스를 통해서도 호출이 가능

me = StaticMethod()
print(me.print_name('minsoo'))
# >>내 이름은 minsoo 입니다.


