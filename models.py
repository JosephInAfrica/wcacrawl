from . import db


class Company(db.Model):
    __tablename__ = 'comapnies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    fax = db.Column(db.String(64))
    address = db.Column(db.String(256))
    telephone = db.Column(db.String(128))
    email = db.Column(db.String(128))
    wca_id = db.Column(db.String(128))
    contacts = db.relationship('Contact', backref='company', lazy='dynamic')

    def __repr__(self):
        return '<Company %s>' % self.name


class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    title = db.Column(db.String(64))
    company_id = db.Column(db.Integer, db.ForeignKey('comapnies.id'))

    def __repr__(self):
        return '<Contact %s>' % self.name
