from app import db


class Company(db.Model):
    __tablename__='companies'

    def __init__(self, address='', telephone='', fax='', website='', email=''):
        self.address = address
        self.telephone = telephone
        self.fax = fax
        self.website = website
        self.email = email

    id=db.Column(db.Integer(32),primary_key=True)
    wca_id=db.Column(db.Integer(16))
    name=db.Column(db.String(64))
    address=db.Column(db.String(128))
    telephone=db.Column(db.String(64))
    fax=db.Column(db.String(64))
    website=db.Column(db.String(128))
    email=db.Column(db.String(128))
    contacts=db.Relationship('Contact',backref='company',lazy='dynamic')

    def __repr__(self):
        return '<Company %s>%sself.name'


class Contact(db.Model):
    __tablename__='contacts'

    def __init__(self, name='', title='', email='', phone=''):
        self.name = name
        self.title = title
        self.email = email
        self.phone = phone
    id=db.Column(db.Integer,primary_key=True)
    company_id=db.Column(db.Integer,db.foreign_key('companies.id')
    name=db.Column(db.String(128))
    email=db.Column(db.String(64))
    phone=db.Column(db.String(164))
    title=db.Column(db.String(64))
