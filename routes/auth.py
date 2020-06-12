# -*- coding: utf-8 -*-
from flask import render_template , jsonify ,request
from app import app , db
from app.models import Order,User
from flask_login import current_user,login_required, login_user, logout_user
from flask import  Flask, render_template, request, redirect, url_for, flash, make_response, session
