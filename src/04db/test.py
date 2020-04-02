
import app



u = app.User(username='susan', email='susan@example.com')
# app.db.session.add(u)
# app.db.session.commit()
# print(u)
users = app.User.query.all()
print(users)