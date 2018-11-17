# -*- coding: utf-8 -*-
from flask import Blueprint

pay_web_v1 = Blueprint('pay_web_v1', __name__)

from . import views
