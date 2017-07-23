import os
import re
from bs4 import BeautifulSoup as soup


class Company(object):
    pass


class Contact(object):
    pass

basedir = os.path.abspath(os.path.dirname(__file__))

tempdir = {'us': basedir+'\\temp'+'\\us\\', 'uk': basedir +
           '\\temp'+'\\uk\\', 'canada': basedir+'\\temp'+'\\canada\\', }
file = tempdir['uk']+'wcaworld.comengmembers.aspcid=78445.txt'
# # tempdir='D:\\Joseph\\wcacrawler\\temp\\us\\'


def get_soup(file):
    with open(file, 'rb') as file:
        result = soup(file.read(), 'html.parser')
    return result


def get_table_soup(file):
    with open(file, 'rb') as file:
        try:
            result = soup(file.read(), 'html.parser').find_all(
                'table', recursive=True)
        except:
            pass
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
    # print (trs)
    contacts = []
    start_point = None
    for tr in trs:
        if len(tr) == 1 and 'contact' in clean_title(tr[0]).lower():
            start_point = trs.index(tr)
            print('start poind found %s' % start_point)
        continue
# 这里专门loop一遍来找到哪个是contact行。
# 这里不能用break跳出，否则返回空，真怪事也。
    # return start_point

    contact = Contact()
    for tr in trs[start_point+1:]:
        if tr[0] == '':
            contacts.append(contact)
            contact = Contact()
            continue
        contact.__setattr__(clean_title(tr[0]), tr[1])
        # print (tr)
    return [[contact.name, contact.email, contact.title, company.name]]


def csv_row(contact):
    return [contact.name, contact.email, contact.phone, contact.company.name]

# def write_to_csv(dir):
#     with open(file,'w+') as csvfile:
#         writer=csv.writer(csvfile,dialect='excel')

#     for file in dir:
#         contacts=get_contact_obj(file)

#         for contact in contacts:
#             writer.writerow(csv_row(contact))


# print (get_company_obj(file).__dict__)
print(csv_row())
