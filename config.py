# -*- coding: utf-8 -*-

import os

DEBUG = False

BASEDIR = os.path.abspath(os.path.dirname(__file__))

DATEBASE_URI = "mysql://root:passwd@127.0.0.1:3306/users"

try:
    from local_setting import *
except ImportError:
    pass
