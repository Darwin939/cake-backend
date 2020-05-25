# -*- coding: utf-8 -*-
from flask import render_template , jsonify ,request
from app import app , db

from additional_func.now_time import time
from app.models import Order,User
from flask_login import current_user,login_requiredб login_user
from flask import  Flask, render_template, request, redirect, url_for, flash, make_response, session



@app.route('/orders', methods =['POST','GET'] )
def orders():
    if request.method == 'POST':
        
        req_data = request.get_json()
        discription = req_data['discription']
        deadline = req_data['deadline']
        tags = req_data['tags'][2]
        print (tags)
        order = Order(discription=discription,deadline = deadline, tags = tags, creation_date = time())  #поменять тайм дать ей функцию без скобок
        db.session.add(order)
        db.session.commit()
        return "Db has updated"
    x = {} 
    orders = Order.query.all()
    for order in orders:
        y = {}
        y['discription'] = order.discription
        y['deadline'] = order.deadline
       # y['tags'] = order.tags
        y['creation_date'] = order.creation_date
        x[int(order.id)] = y
    return x

@app.route('/', methods =['POST','GET'] )
def index():
    print (current_user.get_id())
    return "if you want check orders , please edir ulr to '/orders'"


#-------------------------For tests , in production shoul be deleted------------

@app.route('/admin/',methods=['post', 'get'])
def admin():
    if current_user.is_authenticated:
        return "Congrats"
    try:
        if session['id'] =='147555151651admin':
            return "Congrats you`re view this"
    except:
        pass
    return 'no auth', 401
    

@app.route('/login/',methods=['post', 'get'])
def login():
    try:
        user = db.session.query(User).filter(User.username == request.get_json()["username"]).first()
        print (user)
        login_user(user)
    except:
        pass
    return "Post and admin admin"
#-------------------------For tests , in production shoul be deleted------------


@app.route('/register/',methods=['post', 'get'])
def login():
    