from app import db







class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    discription = db.Column(db.String(1000))
    creation_date = db.Column(db.Integer)
    deadline = db.Column(db.Float, index=True)
    tags = db.Column(db.String(1000))
    
    def __repr__(self):
        return '<Orders {}>'.format(self.body)
        



    
    