from bs4 import BeautifulSoup as soup
import os
import re
basedir = os.path.abspath(os.path.dirname(__file__))
tempdir = basedir+'\\temp\\'

file = tempdir+'wcaworld.comengmembers.aspcid=107056.txt'


class Company(object):

    def __init__(self, address='', telephone='', fax='', website='', email=''):
        self.address = address
        self.telephone = telephone
        self.fax = fax
        self.website = website
        self.email = email


class Contact(object):

    def __init__(self, company, name='', title='', email='', phone=''):
        self.company = company
        self.name = name
        self.title = title
        self.email = email
        self.phone = phone


def get_soup(file):
    with open(file, 'rb') as file:
        result = soup(file.read(), 'html.parser')

    return result


def clean(str):
    return re.sub(r'\s+', ' ', str)


def clean_title(str):
    str = str.replace(':', '')
    return str


def get_info(soup_demo):
    company_name = soup_demo.find('div', {'class': 'member_name'}).text

    member_id = soup_demo.find('div', {'class': 'member_id'}).text

    info_table = soup_demo.find(
        'div', class_='memberprofile_row table-responsive')

    rows = info_table.find_all('tr')

    return rows

def parse_rows(rows):
    for row in rows:
        company = Company()
        tds = row.find_all('td')
        row_name = clean_title(tds[0].text)
        if row_name == 'address':
            company.address = clean(tds[1].text)
        if row_name == 'telephone':
            company.telephone = clean(tds[1].text)
        if row_name == 'website':
            company.website = clean(tds[1].text)
        if row_name == 'email':
            company.email = clean(tds[1].text)
        if row_name=='contact':
        # 	
# print (get_info(get_soup(file)))

def test():
    # print (get_soup(file))
    print((get_soup(file).find(
        'div', {'class': 'memberprofile_row table-responsive'})))


test()
