from flask import Flask, render_template

app = Flask(__name__)
# 设置模板文件夹路径
app.template_folder="html"

@app.route('/index')
def index():
    return render_template('index.html')
# 它以模板的文件名作为自己的第一个参数，附加参数以键/值对的形式为在模板文件中引用的变量赋值
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/info')
def info():
    class person:
        def __init__(self):
            self.name = "GGGfei"
            self.age = 22
    p=person()
    # 可以使用点（.）来访问变量的属性，作为替代，也可以使用所谓的“下标”语
    # 法（ [] ）。下面的几行效果是一样的:
    return render_template('userinfo.html', p=p)

@app.route("/foreach")
def foreachtest():
    aa=[22,3,4,5,6]
    return render_template('foreach.html', nums=aa)


@app.route("/extend")
def extend():
    return render_template('extend.html')

@app.route("/macro")
def macro():
    return render_template('macro.html')

# lask允许程序自己定义基于基础模板的错误页面，就像常规路由一样。有两个最常见的错误代码分别是404和500
@app.errorhandler(404)
def error1(e):
    return "404444"

# https://www.cnblogs.com/wongbingming/p/6807771.html
# http://docs.jinkan.org/docs/jinja2/templates.html#builtin-filters
app.run(debug=True)



