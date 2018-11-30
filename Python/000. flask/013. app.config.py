from flask import Flask

app = Flask(__name__)

app.config['config'] = 'hello?'
# app.config를 통해 설정 값들을 저장할 수 있음.

print(app.config)
''' 
<Config {'ENV': 'production', 'DEBUG': False, ......... 'config': 'hello?'}>
'''
# 대충 이러한 기본 config를 가지고 있는데, config를 추가해서 'config':'hello?' 값이 추가된 것을 볼 수 있다.

app.config.update({
    'CONFIG_1': 1,
    'CONFIG_2': True
})
# app.config.update으로 추가해 줄 수도 있다.

del app.config['CONFIG_2']
# config 삭제
print('CONFIG_2' in app.config)
# False 값 return. CONFIG_2를 삭제했기 때문임

# app.config는 많은 기본 값들을 가지고 있는데
# 이미 들어가 있는 해당 설정 값들의 일부는 즉시 접근 가능하다
print(app.debug, app.testing, app.secret_key)


class Someconfig(object):
    SOME_CONFIG = 1


app.config.from_object(Someconfig)
print(app.config['SOME_CONFIG'])
