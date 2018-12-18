from flask import request, g, jsonify
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
        record_list = Record.query.filter_by(Record.user_id==user_id).all()
        records = []
        for record in record_list:
            records.append({"pay_num": record.pay_num, "description": record.description, "pay_kind": record.pay_kind})
        return jsonify({"data": records})

@pay_web_v1.route('add', methods=['POST'])
def addPay():
    data = request.form
    user_id = data.get('user_id')
    pay_num = data.get('pay_num')
    des = data.get('description', 'Others')
    if not (user_id and pay_num):
        abort(104)
    db.session.add(Record(
        user_id=user_id,
        pay_num=int(pay_num),
        description=des))
    db.session.commit()
    return "ok!" 
