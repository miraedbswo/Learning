import mod1
# mod1을 import함

from mod1 import sum
# sum이라는 함수만 import함

from mod1 import *
# *은 mod1 모듈에 있는 모든 것을 import하다는 점이다.
# 하지만 모든 것이 import되는 것은 아니다.
# 자세한 내용은 mod1.py의 주석을 확인하자.

print(sum(1, 2))
# import 했기 때문에 사용 가능하다

new_instance = cal()
print(new_instance.mul(3, 4))
# class 또한 import 해서 정상적으로 사용이 가능하다.

print(_private_num)
print(__all_private_num)
