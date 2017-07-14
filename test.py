from bs4 import BeautifulSoup as soup
import os
import re
basedir = os.path.abspath(os.path.dirname(__file__))
tempdir = basedir+'\\temp\\'+'\\usa\\'

class Company(object):

    def __init__(self, address='', telephone='', fax='', website='', email=''):
        self.address = address
        self.telephone = telephone
        self.fax = fax
        self.website = website
        self.email = email


class Contact(object):

    def __init__(self, company='', name='', title='', email='', phone=''):
        self.company = company
        self.name = name
        self.title = title
        self.email = email
        self.phone = phone

company=Company()

company.__setattr__('fax',123)

print (company.__dict__)