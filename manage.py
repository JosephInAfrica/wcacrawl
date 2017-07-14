from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from database import Company,Contact
from flask_script import Manager

basedir = os.path.abspath(os.path.dirname(__file__))
tempdir = basedir+'\\temp\\'+'\\usa\\'
file = tempdir+'wcaworld.comengmembers.aspcid=62361.txt'

app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
manager=Manager(app)


def startParse(dir):
    for file in dir:
        try:
            company=get_company_obj(file)
            contacts=get_contact_obj(file)
        except:

            print ('info not generated.')
        try:
            db.session.add(company)
            for contact in contacts:
                db.session.add(contact)
        except:
            print('info not added')
            db.session.rollback()





# test1()
if __name__=='__main__':
    manager.run()