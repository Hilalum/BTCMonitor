import flask,json
server = flask.Flask(__name__)
from Include.Sqllite import insert_register
@server.route('/register',methods=['get'])
def register():
    username = flask.request.values.get('username',type=str,default='')
    pwd = flask.request.values.get('pwd',type=str,default='')
    email = flask.request.values.get('email',type=str,default='')
    tax = flask.request.values.get('tax',type=str,default='')
    weekmoney = flask.request.values.get('weekmoney',type=str,default='')
    if username == '' or pwd ==  ''or email ==  ''or weekmoney ==  '':
        res = {'msg': '缺失参数'}
        return json.dumps(res, ensure_ascii=False)
    insert_register(username,tax,weekmoney,email,pwd)
    res = {'msg':'注册成功'}
    return json.dumps(res,ensure_ascii=False)