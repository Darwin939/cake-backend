# -*- coding: utf-8 -*-
from flask import render_template , jsonify ,request
from app import app , db


from app.models import Order




@app.route('/', methods =['POST','GET'] )
def orders():
    if request.method == 'POST':
        
        req_data = request.get_json()
        discription = req_data['discription']
        deadline = req_data['deadline']
        tags = req_data['tags']
        order = Order(discription=discription,deadline = deadline, tags = tags)
        db.session.add(order)
        db.session.commit()
        return "Db has updated"
    x = {} 
    orders = Order.query.all()
    for order in orders:
        y = {}
        y['discription'] = order.discription
        y['deadline'] = order.deadline
        y['tags'] = order.tags
        y['creation_date'] = order.creation_date
        x[int(order.id)] = y
    return x