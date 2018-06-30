# 딕셔너리란 '사전' 이란 뜻임
# 사람을 예로 들자면, 사람의 이름 : 김윤재, 성별 : 남자, 나이 : 17
# Key와 vaule라는 것을 한 쌍으로 가진 자료형이다.

# 딕셔너리는 시퀀스 자료형과는 달리 Key를 통해 value를 얻는다.
# 이름이 무엇인가요 -> 라면 이름에 해당되는 vaule값을 반환해 그 이름 값을 얻게 되는 것이다.

dic = {'name': 'Goming', 'age': '17', 'birth': '0706'}
# 딕셔너리는 {과 }. 중괄호로 둘러싸여 있음.
# {key: vaule} 형태임

# Key에는 변하지 않는 값을 사용해야 하고, vaule 값에는 변하는 값과 변하지 않는 값 모두 사용할 수 있다.


# -- 딕셔너리 쌍 추가
a = {1: 'a'}
a[2] = 'b'
print(a)
# {1: 'a', 2: 'b'}

a['name'] = 'Goming'
print(a)
# {1: 'a', 2: 'b', 'name': 'Goming'}


# 딕셔너리 쌍 삭제
del a['name']
print(a)
# {1: 'a', 2: 'b'}


# -- 딕셔너리 기타 메서드
print(a.keys())
# 딕셔너리의 key만 리스트로 반환
# dict_keys([1, 2])

print(a.values())
# 딕셔너리의 value만 리스트로 반환
# dict_values(['a', 'b'])

print(a.items())
# 딕셔너리의 item을 (key, value) 형태의 튜플로 이루어진 리스트로 반환
# dict_items([(1, 'a'), (2, 'b')])

a.clear()
# 클리어