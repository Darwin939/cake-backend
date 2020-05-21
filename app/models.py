from app import db

from datetime import datetime
from time import time




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
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_on  =  db.Column(db.DateTime(), default=datetime.utcnow) #TO-DO поменять время
    order = db.relationship('Order', secondary=order_tag, backref='tag')
    def __repr__(self):
        return "<{}:{}>".format(self.id, self.name)


#from app import db
#from app.models import Order,Tag
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