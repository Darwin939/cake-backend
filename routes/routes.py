# -*- coding: utf-8 -*-
from flask import render_template , jsonify ,request
from app import app , db
from app.models import Order,User
from flask_login import current_user,login_required, login_user, logout_user
from flask import  Flask, render_template, request, redirect, url_for, flash, make_response, session



@app.route('/api/', methods =['POST','GET'] )
def index():
    return jsonify({"is_authenticated":str(current_user.is_authenticated)})


@app.route('/api/register/',methods=['POST', 'GET'])
def register():
    if request.method == "POST":
        try:   
            password = request.get_json()["password"]
            number  = request.get_json()["number"]
            iscooker = request.get_json()["iscooker"]
            user = User(password = password,number=number,is_cooker = iscooker)
            #telephone number validation
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            return jsonify({"Wrong data":str(e)})

        user_num = db.session.query(User).filter(User.number == number).first()
        login_user(user,remember=True)
        return jsonify({"Database_status":"db updated","is_authenticated":str(current_user.is_authenticated)}) 
    return jsonify({"Wrong data":"Need login and password,number"})

#----------------------??????????????-------------------
@app.route('/api/login/',methods=['post', 'get'])
def login():
    req = request.get_json()
    number = req["number"]
    password = req["password"]
    user = db.session.query(User).filter(User.number == number).first()
    if user and  user.password ==password:
        login_user(user)
        return jsonify({"is_authenticated":str(current_user.is_authenticated)})
    else:
        return jsonify({"Wrong data":"Password or Login Incorrect"})
    return jsonify({"Wrong data":"Need login and password"})
#---------------------??????????????---------------------

@app.route('/api/user/<id>/',methods = ["POST","GET"]) # TO-DO поменять путь к профилям людей по их юзернейм
def user_profile(id):
    if request.method == "GET":
        try:
            x = {}
            user = db.session.query(User).get(id)
            x['number'] = user.number
            x['creation_date'] = user.creation_date
            x['name'] = user.name
            x['secondname'] = user.secondname
            x['updated_on'] = user.updated_on
            x['is_cooker'] = user.is_cooker
            x['biography'] = user.biography
            orders = db.session.query(Order).filter(Order.user_id == id).all()
            y = {}
            for order in orders:
                z = {}
                z['body'] = order.body
                z['deadline'] = order.deadline
                z['creation_date'] = order.creation_date
                z['status'] = order.status
                y[order.id] = z 
            x["orders"] = y
            return jsonify(x)      
        except Exception as e:
            return jsonify({"Wrong data":"maybe this user doesnt exist","Exception":str(e)})


    return jsonify({"Wrong data":"This person doesnt exist","Exception":"may be you dont have right permission"})

@app.route('/api/user/myprofile/todo/',methods = ["POST","GET"]) # TO-DO поменять путь к профилям людей по их юзернейм
def user_profile_todo():
    if request.method == "GET" and current_user.is_authenticated:   #check current user function
        id = current_user.get_id()
        x = {}
        orders = db.session.query(Order).filter(Order.worker_id==id).all()
        for order in orders:
            y = {}
            y['id'] = order.id
            y['body'] = order.body
            y['creation_date'] = order.creation_date
            y['deadline'] = order.deadline
            y['updated_on'] = order.updated_on
            y['status'] = order.status
            y['user_id']  = order.user_id
            y['worker_id'] = order.worker_id
            y['title'] = order.title
            x[order.id] = y
        return x        
    if request.method == "POST" and current_user.is_authenticated:
        req = request.get_json()
        id = req["order_id"]
        status = req["status"]
        order = db.session.query(Order).filter(Order.id==id).first()
        order.status = status
        db.session.add(order)
        db.session.commit()
        return redirect(url_for('user_profile_todo', id = current_user.get_id()))
        

    return {"Wrong data":"maybe this user doesnt exist or you dont have this permission"}

@app.route("/api/myprofile", methods =["GET","POST"])
@login_required
def myprofile():
    if request.method == "GET" and current_user.is_authenticated :
        x = {}
        id = current_user.get_id()
        user = db.session.query(User).get(id)
        x['number'] = user.number
        x['creation_date'] = user.creation_date
        x['name'] = user.name
        x['secondname'] = user.secondname
        x['updated_on'] = user.updated_on
        x['is_cooker'] = user.is_cooker
        x['biography'] = user.biography
        orders = db.session.query(Order).filter(Order.user_id == id).all()
        y = {}
        for order in orders:
            z = {}
            z['body'] = order.body
            z['deadline'] = order.deadline
            z['creation_date'] = order.creation_date
            z['status'] = order.status
            y[order.id] = z 
        x["orders"] = y
        return jsonify(x)
    if request.method == "POST" and current_user.is_authenticated:   #check current user function
        try:
            req = request.get_json()  
            password = req["password"]
            name  = req["name"]
            secondname = req["secondname"]
            #social = req["social"]
            #avatar = req["???"] image file
            id = current_user.get_id()
            user = db.session.query(User).filter(User.id == id).first()
            user.password = password
            user.name = name
            user.secondname = secondname
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            return jsonify({"Wrong data":str(e)})
        # user = db.session.query(User).get(id)
        # x['username'] = user.username 
        return redirect(url_for('myprofile'))
    return {"Wrong data":"maybe this user doesnt exist or you dont have this permission"}

@app.route('/api/logout/')
def logout():
    logout_user()
    return jsonify({"is_authenticated":str(current_user.is_authenticated)})


@app.route('/api/orders', methods =['POST','GET'])
def orders():
    if request.method == 'POST' and current_user.is_authenticated:
        req_data = request.get_json()
        body = req_data['body']
        deadline = req_data['deadline']
        # tags = req_data['tags'][0]
        user_id = current_user.get_id()
        order = Order(body=body,deadline = deadline,user_id = user_id)  #поменять тайм дать ей функцию без скобок
        db.session.add(order)
        db.session.commit()
        return redirect(url_for('orders')) 
    x = {} 
    # orders = Order.query.all()
    req = request.get_json()
    price_array = req["filter"]["price"]
    weight_array = req["filter"]["weight"]
    page = req['page_num']
    page_s = req['page_size']
    orders = Order.query.filter(Order.price>price_array[0], Order.price<price_array[1]).paginate(page,page_s,False).items
    # o = db.session.query(Order).filter(Order.price>price_array[0], Order.price<price_array[1]).all()
    
    # orders = Order.query.paginate(page,page_s,False).items   #pagination
    for order in orders:
        y = {}
        y['body'] = order.body
        y['deadline'] = order.deadline
       # y['tags'] = order.tags
        y['creation_date'] = order.creation_date
        y['price'] = order.price
        y['weight'] = order.weight
        z = {}
        z[int(db.session.query(User).get(order.user_id).id)] = str(db.session.query(User).get(order.user_id).name)
        y['user'] = z
        x[int(order.id)] = y
    return x
