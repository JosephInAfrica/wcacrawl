from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager,Shell
from app import create_app
from app.models import Company, Contact
from app.parse import startParse

app=create_app('default')
manager=Manager(app)
db=SQLAlchemy(app)
manager=Manager(app)


def make_shell_context():
    return dict(app=app,db=db,Company=Company,Contact=Contact,parse=startParse)

manager.add_command('shell',Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
