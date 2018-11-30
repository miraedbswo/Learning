from flask import Flask, g
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
print(app.logger)

# Flask.logger는 'flask.app'이라는 이름의 logger를 반환
# 여기에 custom logger를 붙여줄 수 있다


@app.before_request
#  되기 전에 실행할 것
def before_first_request():
    def make_logger():
        handler = RotatingFileHandler('server_log.log', maxBytes=10000, backupCount=3)
        # RotatingFileHandler
        # 첫 번째 인자 -> 로그 파일의 이름
        # 두 번째 인자 -> max치를 설정. maxBytes를 채우면 새 로그 파일을 생성
        # 세 번째 인자 -> n번째 로그 파일이 생성되면 원래 있던 로그파일을 버리고 새로운 로그 파일 생성

        formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")
        # logging.Formatter를 사용하여 로그 포매팅

        handler.setFormatter(formatter)
        # handler에 Formatter 설정
        app.logger.addHandler(handler)
        # app의 logger에 handler 추가
        """
        <logger's level>
        CRITICAL = 50
        FATAL = CRITICAL
        ERROR = 40
        WARNING = 30
        WARN = WARNING
        INFO = 20
        DEBUG = 10 
        NOTSET = 0
        """
        app.logger.setLevel(logging.INFO)
        # logger의 level을 세팅
        # -> 기본 level은 WARNING

    make_logger()
    g.logger = app.logger
    print(g.logger)

    g.logger.info('<=====server logging=====>')


@app.route('/index1')
def index():
    g.logger.info('Access <index> router')
    return 'logging', 200


if __name__ == '__main__':
    app.run(debug=True)
