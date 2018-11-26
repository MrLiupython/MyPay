# -*- coding: utf-8 -*-
import os
import logging
import logging.handlers import RotatingFileHandler
from flask import Flask
from .core import api, db
from .models import Users, Record
from .pay import pay_web_v1

def init_app():
    app = Flask(__name__)
    api.init_app(app)
    db.init_app(app)
    if not app.debug:
        file_handler = RotatingFileHandler(
            os.path.abspath(os.path.join('/tmp/', 'mypay.log')),
            maxBytes=50 * 1024 * 1024,
            backupCount=5,
            encoding='utf-8'
        )
        file_handler.setFormatter(Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.DEBUG)
        app.logger.addHandler(file_handler)
    app.register_blueprint(pay_web_v1)
 
