# -*- coding: utf-8 -*-
from flask import request, g, jsonify, render_template, abort, url_for
from mypay.ext import db
from mypay.models import Users, Record
from . import pay_web_v1

@pay_web_v1.route('record', methods=['Get', 'POST'])
def pay_query():
    if request.method == 'POST':
        user_id = request.cookies.get('user_id')
        post_data = request.form['data']
        pay_num = post_data.get('num')
        description = post_data.get('description')
        pay_kind = post_data.get('pay_kind')
        if not (user_id and pay_num and description):
            return "Argument error"
        db.session.add(Record(user_id=user_id, pay_num=pay_num, 
            description=description, pay_kind=pay_kind))
        db.commit()
    else:
        user_id = request.cookies.get('user_id')
        if not user_id:
            return "Are you sure you had logon?"
        record_list = Record.query.filter_by(user_id=user_id).all()
        records = []
        for record in record_list:
            records.append({"pay_num": record.pay_num, "description": record.description, "pay_kind": record.pay_kind})
        return jsonify({"data": records})

@pay_web_v1.route('add', methods=['POST'])
def addPay():
    data = request.form
    verify_value = data.get('who')
    user_id = data.get('user_id')
    pay_num = data.get('pay_num')
    if not user_id or not pay_num or verify_value != "MrLiu":
        abort(104)
    des = data.get('description', 'Others')
    db.session.add(Record(
        user_id=user_id,
        pay_num=int(pay_num),
        description=des))
    db.session.commit()
    return "ok!" 

@pay_web_v1.route('index', methods=['GET'])
def index():
    return render_template("index.html")
