# closure 이란 , 함수 선언 안에 함수를 선언하는 방식
def get_sum_func():
    def sum(a, b):
        return a + b
    return sum
    # 내부 함수인 sum을 return


sum = get_sum_func()
print(sum(2, 3))
# 2 + 3 값인 5 출력


def get_number_printer(n):
    def print_n():
        print(n)
    return print_n

# 내부함수가 외부 함수의 지역변수에 접근할 수 있음
# 외부 함수가 종료됨가 동시에 사라지지 않고 지역변수가 그대로 남아있기 때문
# 이를 closure라고 부름


# 내부 함수를 반환하고 지역변수를 가지고 있는 외부 함수가 있다고 하자.
def outer_function(something):
    def inner_function():
        print(something)

        return inner_function
    return outer_function


print_something = outer_function('Hello, world!')
print_something()
# something이 inner_function에서 출력됨.
