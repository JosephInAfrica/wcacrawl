from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager,Shell
from app import create_app
from app.models import Company, Contact
from config import tempdir
from app.parse import get_company_obj,get_contact_obj

app=create_app('default')
manager=Manager(app)
db=SQLAlchemy(app)
manager=Manager(app)

def startParse(nation):

    for file in os.listdir(tempdir[nation]):
        if not os.path.isfile(tempdir[nation]+file):
            continue
        print ('parsing %s'%file)
        company=get_company_obj(tempdir[nation]+file)
        contacts=get_contact_obj(tempdir[nation]+file)
        print ('%s parsed'%file)
        try:
            db.session.add(company)
            for contact in contacts:
                db.session.add(contact)
        except:
            print('info not added')
            db.session.rollback()

# def parse_file():
    

def make_shell_context():
    return dict(app=app,db=db,Company=Company,Contact=Contact,parse=startParse)

manager.add_command('shell',Shell(make_context=make_shell_context))
# test1()
if __name__=='__main__':
    manager.run()