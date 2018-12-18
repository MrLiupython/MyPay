#! -*- coding: utf-8 -*-

from flask_script import Manager, Shell
from flask_migrate import MigrateCommand, Migrate
from mypay.ext import db
from mypay import init_app
from mypay.models import *

app = init_app()

manage = Manager(app)
migrate = Migrate(app, db)

manage.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manage.run()
