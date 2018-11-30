# 애플리케이션은 정확한 버전 넘버를 포함하여 모든 패키지 의존성을 기록한 requirements.txt 파일을 포함해야 한다.
# 가상 환경의 경우 컴퓨터에서 재생성해야 하기 때문에 중요하다.

# 이 파일은 pip를 사용하여 자동으로 생성할 수 있다.
# (venv) $ pip freeze >requirements.txt

# 가상 환경을 완벽하게 복사할 필요가 있을 때 새로운 가상 환경을 생성하고 다음과 같은 커맨드로 실행할 수 있다.
# (venv) $ pip install -r requirements.txt
