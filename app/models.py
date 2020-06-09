from app import db,login_manager

from datetime import datetime
from time import time
from flask_login import LoginManager, UserMixin

class User(db.Model,UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    number = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    creation_date = db.Column(db.Integer, default = time)
    name = db.Column(db.String(200))
    secondname = db.Column(db.String(200))
    updated_on = db.Column(db.Integer, default = time,  onupdate=time)
    is_cooker = db.Column(db.Boolean)
    biography = db.Column(db.String(20000))
    rating = db.Column(db.Integer)
    #orders - заказы которые сделал он
    #w_orders - заказы для работы
    def __repr__(self):
        return "<{}:{}>".format(self.id, self.number)


class Order(db.Model):
    #row order activ/inactive
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000)) 
    body = db.Column(db.String(1000))
    creation_date = db.Column(db.Integer, default = time)
    deadline = db.Column(db.Float)
    updated_on = db.Column(db.Integer, default = time,  onupdate=time)
    status = db.Column(db.Boolean, default = True)
    weight = db.Column(db.Integer)
    price = db.Column(db.Integer)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    worker_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    user = db.relationship("User",foreign_keys = [user_id],backref='orders')
    worker = db.relationship("User",foreign_keys = [worker_id], backref ='w_orders')
    

    def __repr__(self):
        return '<Orders {}>'.format(self.body)


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)

#from app import db
#from app.models import Order, User
#u = User(number = "8755555",password = "admin")
#db.create_all()
#db.drop_all()
#order1  = Order(body='dasdsfd',deadline = 45456,user_id = 1,worker_id = 1)
#db.session.add(order1)
#db.session.commit()
#t1 = Tag(name="refactoring")
#t2 = Tag(name="refactoring")
#source venv/bin/activate  ---- Activate env
#db.session.add_all([t1,t2,order1,order2])
#order1.tag.extend([t2, t1])