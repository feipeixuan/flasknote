
from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World!</h1>"

# 路由中带有变量名
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

# 请求上下文
# 在Flask中有两个上下文：程序上下文和请求上下文 通过app.app_context()来调用程序上下文的
@app.route('/index1')
def index1():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

# 函数需要用不同的状态代码回复响应时，它就会把一个数值添加在相应文本后，作为第二个返回值
@app.route('/index2')
def index2():
    return '<h1>Bad Request</h1>', 400


@app.route('/urls')
def urls():
    # Map([ index1>, urls>, index>, ' (OPTIONS, GET, HEAD) -> static>, ' (OPTIONS, GET, HEAD) -> user>])
    return str(app.url_map)


# 请求钩子
# before_first_request: 在处理第一个请求之前执行该注册函数
# before_request:       在每个请求前都执行该注册函数
# after_request:        在每个请求之后都执行该注册函数,如果没有未被处理的错误的话。
# teardown_request:     在每个请求之后都执行该注册函数,即使有未被处理的错误

@app.before_request
def after_request():
    print("222")

# make_response()函数可以取1、2或3个参数，这些值被作为视图函数的响应统一作为一个对象response返回。

@app.route('/index3')
def index3():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


@app.route('/index4')
def index4():
    return redirect('http://www.baidu.com')

app.run(debug=True) #开发模式下,支持热更新