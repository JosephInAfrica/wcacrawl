import os
import re
from bs4 import BeautifulSoup as soup
import csv

basedir = os.path.abspath(os.path.dirname(__file__))

tempdir = {'us': basedir+'\\temp'+'\\us\\', 'uk': basedir +
           '\\temp'+'\\uk\\', 'canada': basedir+'\\temp'+'\\canada\\',
           'malaysia': basedir+'\\temp\\'+'malaysia\\',
           'newzealand': basedir+'\\temp\\'+'newzealand\\'}


class Company(object):

    def __init__(self):
        self.name, self.wca_id, self.address, self.phone = '', '', '', ''


class Contact(object):

    def __init__(self):
        self.name, self.email, self.phone, self.title = '', '', '', ''


def get_soup(file):
    with open(file, 'rb') as file:
        result = soup(file.read(), 'lxml')
    return result


def get_table_soup(file):
    with open(file, 'rb') as file:
        # text=file.read().decode('utf-8')
        # print (text)
        # result=re.findall(re.compile(r'<table[.\s]*</table>'),text)
        result = soup(file.read(), 'lxml').find_all('table', recursive=True)
        # print (result)
    return result[0] if (len(result) == 1) else None


def clean_para(para):
    para = re.sub(r'\n+\s', '\n', para)
    return para
# 把多个空行和空格换成一个空行。。。对付错乱的格式


def clean(str):
    str = re.sub(r'\s+', ' ', str)
    str = re.sub(r'^\s', '', str)
    str = re.sub(r'\s$', '', str)
    return str
# 这里清除空行，多余空格和首尾空格


def clean_id(str):
    str = clean(str)
    str = re.findall(r'\d+', str)[0]
    return str
# 只剩下数字，找wca id 用


def clean_title(str):
    str = clean(str)
    str = str.replace(':', '')
    return str.lower()
# 去掉冒号 并小写，作为标题


def clean_comapny_name(str):
    str = re.sub(re.compile('\(.+\)'), '', str)
    return str
# 去掉括号


def get_namenid(file):
    try:
        name = clean_comapny_name(
            clean(get_soup(file).find('div', class_='member_name').text))
        # name=clean(get_soup(file).find('div',class_='member_name').text)
    except:
        name = clean_comapny_name(get_soup(file)[0].find('b'))
    try:
        id = clean_id(get_soup(file).find('div', class_='member_id').text)
    except:
        id = ''
    return (name, id)
# 得到公司名和id


def get_profile_table(file):

    table = get_table_soup(file)

    trs = table.find_all('tr')

    trs = [[clean(td.text) for td in tr.find_all('td')][:2] for tr in trs]
    # return trs
    return trs
# 找到每行的两个元素，空行也有


def get_company_obj(file):
    trs = get_profile_table(file)
    company = Company()
    # company={}
    for tr in trs:
        if len(tr) == 1 and 'contact' in clean_title(tr[0]).lower():
            # print ('find contact')
            # print(trs.index(tr))
            break
        if clean(tr[0]) == '':
            continue
        try:
            company.__setattr__(clean_title(tr[0].lower()), clean(tr[1]))
        except:
            pass
    company.name, company.wca_id = get_namenid(file)

    return company
# 得到公司的信息


def get_contact_obj(file):
    trs = get_profile_table(file)

    contacts = []
    start_point = None
    for tr in trs:
        if len(tr) == 1 and 'contact' in clean_title(tr[0]).lower():
            start_point = trs.index(tr)
            print('start poind found %s' % start_point)
        continue

    # return start_point

    contact = Contact()
    rest = trs[start_point+1:]

    if rest is not None:
        for tr in trs[start_point+1:]:
            if tr[0] == '':
                dic = contact.__dict__
                contact.phone = ','.join([dic[attr] for attr in dic if (
                    'line' in attr.lower() or 'phone' in attr.lower() and dic[attr] != '')])

                contacts.append(contact)
                contact = Contact()
                continue
            contact.__setattr__(clean_title(tr[0]), tr[1])
            # print (tr)

    return contacts


def file_to_row(file):
    company = get_company_obj(file)
    contacts = get_contact_obj(file)

    rows = [[contact.name, contact.email, company.name, contact.title,
             contact.phone, 'WCA', ]for contact in contacts]
    if len(contacts) == 0:
        return [[company.name,  company.email, company.name, '', company.phone, 'WCA'], ]
    return rows


def parse(nation):
    with open(basedir+'\\%s_wca.csv' % nation, 'w+', encoding='utf-8', newline='') as output_file:
        writer = csv.writer(output_file, dialect='excel')
        for file in os.listdir(tempdir[nation]):
            print('%s is being parsed...\n' % file)
            if not os.path.isfile(tempdir[nation]+file):
                continue

            rows = file_to_row(tempdir[nation]+file)
            for row in rows:
                writer.writerow(row)
                print(row)


parse('newzealand')
# file=tempdir['us']+'wcaworld.comengmembers.aspcid=103354.txt'

# print (get_table_soup(file))
# print (get_soup(file).find_all('table',recuImport / Exportrsive=True))
# print (get_profile_table(file))Import / ExportImport / Export
# print (get_contact_obj(file).__dict__)
# print (file_to_row(file))
