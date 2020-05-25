from app import db,login_manager

from datetime import datetime
from time import time
from flask_login import LoginManager, UserMixin



class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    discription = db.Column(db.String(1000))
    creation_date = db.Column(db.Integer, default = time)
    deadline = db.Column(db.Float, index=True)

    
    def __repr__(self):
        return '<Orders {}>'.format(self.discription)

#Ассоциативная таблица для отношений многие ко многим


order_tag = db.Table('order_tag',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)

class  Tag(db.Model):
    #TO-DO запросы many to many
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_on  =  db.Column(db.DateTime(), default=time) 
    order = db.relationship('Order', secondary=order_tag, backref='tag')
    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name)


class User(db.Model,UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    number = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    creation_date = db.Column(db.Integer, default = time)
    updated_on = db.Column(db.Integer, default = time,  onupdate=time)

    def __repr__(self):
        return "<{}:{}>".format(self.id, self.username)

@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)

#from app import db
#from app.models import Order,Tag,order_tag, User
#u = User(username = "admin",number = "8755555",password = "admin")
#db.create_all()
#db.drop_all()
#order1  = Order(discription='dasdsfd',deadline = 45456)
#db.session.add(order1)
#db.session.commit()
#t1 = Tag(name="refactoring")
#t2 = Tag(name="refactoring")
#source venv/bin/activate  ---- Activate env
#db.session.add_all([t1,t2,order1,order2])
#order1.tag.extend([t2, t1])