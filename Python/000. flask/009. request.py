from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/request/args', methods=['GET'])
def args():
    return request.args['keys']
    # keys를 가져옴 ( GET )


@app.route('/request/form', methods=['POST'])
def form():
    return request.form['keys']
    # keys를 리턴함 ( POST일 때 )


@app.route('/request/json')
def json():
    req = request.get_json()

    print(type(req))
    # json 타입은 dict타입 또는 list 타입으로 바뀜
    return req


if __name__ == '__main__':
    app.run(debug=True)
