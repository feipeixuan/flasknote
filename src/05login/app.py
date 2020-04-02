from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask import *
from flask_login import current_user, login_user,LoginManager,logout_user
import myapp

app = Flask(__name__)
login_manager = LoginManager(app)
app.template_folder = "templates"
app.config.from_object(myapp.Config)
app.config['SECRET_KEY'] = 'you-will-never-guess'
myapp.db.init_app(app)
Migrate(app, myapp.db)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = myapp.LoginForm()
    # flask_wtf类的validate_on_submit()
    # 方法校验两个地方：1 - 表单提交的方法2 - 提交的内容非空
    if form.validate_on_submit():
        # flask提供了一个非常有用的flash()
        # 函数，基于session实现的用于保存数据的集合，其特点是：使用一次就删除
        # 函数，传入消息内容
        user=myapp.User.query.filter_by(username=form.username.data).first()
        print(user)
        if user is not None:
            login_user(user, remember=True)
            flash('Login requested for user {}, remember_me={}'.format(
                form.username.data, form.remember_me.data))
            return redirect('/index')
    return render_template('form.html', title='Sign In', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/index", methods=['GET'])
def index():
    if current_user.is_authenticated:
        return render_template('index.html')
    else:
        return redirect(url_for("login"))


@app.route("/create", methods=['GET'])
def create():
    username = request.args.get('name')
    print(username)
    print(app.config['SQLALCHEMY_DATABASE_URI'])
    myapp.db.session.add(myapp.User(username=username))
    myapp.db.session.commit()
    users = myapp.User.query.all()
    return render_template("users.html", users=users)



# This sets the callback for reloading a user from the session. The function you set should take a user ID (a unicode)
# and return a user object, or None if the user does not exist.
@login_manager.user_loader
def load_user(user_id):
    user = myapp.User.query.get(user_id)
    return user


if __name__ == "__main__":
    app.run(debug=True)
