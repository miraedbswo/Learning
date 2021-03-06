# Set . 수학의 집합과 비슷함
# Set의 가장 큰 특징

# 1. 중복을 허용하지 않는다.
# 2. 순서가 없다.

# 자료형의 중복을 제거하기 위해서 사용되기도 함
s1 = set([1, 2, 3])
print(s1)
# {1, 2, 3}

s2 = set("Hello")
print(s2)
# {'e', 'H', 'l', 'o'}
# l이 2번 있기 때문에 중복을 제거하고 1개만 출력. 순서가 없음


# -- 교집합, 합집합 , 차집합 구하기

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
# 둘의 교집합인 4, 5, 6이 출력

s1.intersection(s2)
# intersection 함수를 통해 s1와 s2의 교집합을 출력할 수도 있음.


print(s1 | s2)
# 합집합 . {1, 2, 3, 4, 5, 6, 7, 8, 9}. 이 때 4, 5, 6처럼 중복된 값은 한 번만 출력된다.

s1.union(s2)
# union 함수를 통해 s1와 s2의 합집합을 구할 수 있음


print(s1 - s2)
# {1, 2, 3}
# s1과 s2에서 중복된 값을 제거한 나머지를 리턴함
print(s2 - s1)
# {8, 9, 7}

s1.difference(s2)
# difference 함수를 통해 차집합을 구할 수 있다.


# Set 기타 메서드
s1.add(7)
print(s1)
# 7 요소 추가

s1.update([7, 8, 9])
print(s1)
# 7, 8, 9를 추가시켜 update함

s1.remove(2)
print(s1)
# 2 요소 제거