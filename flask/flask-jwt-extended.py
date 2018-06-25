from flask import Flask, jsonify, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

app = Flask(__name__)
# JWT extension 설정
app.config['JWT_SECRET_KEY'] = 'secret'
JWT = JWTManager(app)


@app.route('/login', method=['POST'])
def login():
    if not request.is_json:
        return jsonify({'msg': 'missing json in request'}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    # username과 password는 None으로 json 형태로 설정
    if not username:
        return jsonify({'msg': 'Missing username parameter'}), 400
    if not password:
        return jsonify({'msg': 'Missing password parameter'}), 400

    if username != 'goming' and password != 'abcd':
        return jsonify({'msg': 'bad username or password'}), 400

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


@app.route('protected', methods=['GET'])
@jwt_required
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user)


if __name__ == '__main__':
    app.run(debug=True)


