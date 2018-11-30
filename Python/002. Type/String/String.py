# String 타입
# 문자, 문자열 모두 string 타입이다.

# iterable 형임. 인덱스가 존재한다

a = 'Life is short, You need Python'
print(a[0])
# L
# 0번 인덱스의 'L'을 출력하였다

print(a[0:4])
# Life
# 슬라이싱 또한 가능

# 문자열 선언
a = 'Hello'
a = "Hello"
# 특별한 경우가 아니라면 작은따옴표 사용

a = '''
hello
my name is
goming
'''

a = """
hello
my name is
goming
"""

# 따옴표 3개를 연속으로 이어 붙여서 선언할 수도 있음
# 1. """를 사용해서 문자열에 '를 넣고 싶은 경우 또는 '''으로 ".
# 2. 여러 줄에 걸쳐 문자열을 표현하기 위해서.
