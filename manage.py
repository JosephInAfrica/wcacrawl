from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager,Shell
from app import create_app
from app.models import Company, Contact


app=create_app('default')
manager=Manager(app)
db=SQLAlchemy(app)
manager=Manager(app)


def make_shell_context():
    return dict(app=app,db=db,Company=Company,Contact=Contact)

@manager.shell_context()

# test1()
if __name__=='__main__':
    manager.run()
