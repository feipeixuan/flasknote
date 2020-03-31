from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    # 每个字段类都接受一个描述或别名作为第一个参数，并生成一个实例来作为LoginForm的类属性。
    # 你在一些字段中看到的可选参数validators用于验证输入字段是否符合预期
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
