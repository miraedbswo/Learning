# 문자 열에 특정 값을 집어넣기 위해서 사용
# 특정 값은 보통 변수를 사용

# 1. 포맷 코드 사용

username = 'Goming'
age = 17

print("Hello %s , your age is %d" % (username, age))

# 2. 문자열 객체의 .format 메서드 사용

print("Hello {} , your age is {}".format(username, age))

# placeholder를 사용해서 index 값을 넣어줄 수 있음
print("Hello {0} , your age is {1}".format(username, age))

# 3. fstring
print(f"Hello {username} , your age is {age}")
# Python 3.5 부터 지원하는 방식이라고 함
# 중괄호 속에 넣어서 format()보다 보기 쉽다
# .format 메서드보다 연산 처리 속도가 빠르다는 장점이 있다.
