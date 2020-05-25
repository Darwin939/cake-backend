# -*- coding: utf-8 -*-
from flask import render_template , jsonify ,request
from app import app , db

from additional_func.now_time import time
from app.models import Order,User
from flask_login import current_user,login_required, login_user, logout_user
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
    return jsonify({"is_authenticated":str(current_user.is_authenticated)})

#-------------------------BEGIN For tests , in production shoul be deleted------------

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
    

#------------------------- END For tests , in production shoul be deleted------------


@app.route('/register/',methods=['POST', 'GET'])
def register():

    if request.method == "POST":
        
        username = request.get_json()["username"]
        password = request.get_json()["password"]
        number  = request.get_json()["number"]
        user = User(username = username,password = password,number=number)
        db.session.add(user)
        db.session.commit()
        return "updated"
        
    return ""


@app.route('/login/',methods=['post', 'get'])
def login():
    username = request.get_json()["username"]
    password = request.get_json()["password"]
    user = db.session.query(User).filter(User.username == username).first()
    if user and  user.password ==password:
        login_user(user)
        return jsonify({"is_authenticated":str(current_user.is_authenticated)})
    else:
        return jsonify({"Wrong data":"Password or Login Incorrect"})
    return jsonify({"Wrong data":"Need login and password"})


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return jsonify({"is_authenticated":str(current_user.is_authenticated)})