from flask import request, g
from ..models import Users, Record
from . import pay_web_v1

@pay_web_v1.route('record', method=['Get', 'POST'])
def pay_query():
    if request.method == 'POST':
        user_id = request.cookies.get('user_id')
         = request.form['data']
