from flask import Flask, render_template,flash,redirect,url_for
import forms
app = Flask(__name__)
app.template_folder = "templates"
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    # flask_wtf类的validate_on_submit()
    # 方法校验两个地方：1 - 表单提交的方法2 - 提交的内容非空
    if form.validate_on_submit():
        # flask提供了一个非常有用的flash()
        # 函数，基于session实现的用于保存数据的集合，其特点是：使用一次就删除
        # 函数，传入消息内容
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('form.html', title='Sign In', form=form)

@app.route("/index")
def index():
    return render_template('index.html')



@app.route("/test")
def test():
    #视图函数也能找到对应的url路径，这可以通过url_for来完
    url=url_for('index')
    return redirect(url)

app.run(debug=True)
