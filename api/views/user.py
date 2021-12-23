from flask import Blueprint, request, make_response, jsonify, abort, render_template
from api.models import User, UserSchema
import json
from werkzeug.exceptions import BadRequest
from myexception import MyException, InputException, ServerException

# ルーティング設定
user_router = Blueprint('user_router', __name__)

@user_router.route('/users', methods=['GET'])
def getUserList():
  users = User.getUserList()
  user_schema = UserSchema(many=True)
  
  if len(users) == 0:
    return "no users found";
  else:
    return make_response(jsonify({
      'code': 200,
      'users': user_schema.dump(users)
    }))

@user_router.route('/users/list', methods=['GET']) #整形されたview: ディレクトリのリファクタは後で
def showUserList():
  users = User.getUserList()
  user_schema = UserSchema(many=True)
  
  if len(users) == 0:
    return "no users found";
  else:
    return render_template('user_list.html', title = 'user_list.html')

@user_router.route('/users/new', methods=['GET']) #新規作成用フォーム
def showUserForm():
    return render_template('user_new.html', title = 'new.htmll')

@user_router.route('/users', methods=['POST'])
def registUser():
  if request.headers["Content-Type"] != "application/json":
    raise BadRequest
  # jsonデータを取得する
  
  jsonData = json.dumps(request.json)
  userData = json.loads(jsonData)
  user = User.registUser(userData)
  user_schema = UserSchema(many=True)

  return make_response(jsonify({
    'code': 200,
    'user': user
  }))

@user_router.errorhandler(BadRequest)
def bad_error_handler(e):
  res = jsonify({
    "error": {
        "name": e.name, 
        "description": e.description 
    }      
  })
  return res, e.code
