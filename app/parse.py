import os
import re
from bs4 import BeautifulSoup as soup
from .models import Company,Contact

# basedir = os.path.abspath(os.path.dirname(__file__))

# tempdir = {'us':basedir+'\\temp\\'+'\\usa\\','uk':basedir+'\\temp\\'+'\\uk\\','canada':basedir+'\\temp\\'+'\\canada\\',}


def get_soup(file):
    with open(file, 'rb') as file:
        result = soup(file.read(), 'html.parser')
    return result

def get_namenid(file):
    name=clean(get_soup(file).find('div',class_='member_name').text)
    id=clean_id(get_soup(file).find('div',class_='member_id').text)
    return (name,id)

def clean_para(para):
    para=re.sub(r'\n+\s','\n',para)
    return para

def clean(str):
    str=re.sub(r'\s+', ' ', str)
    str=re.sub(r'^\s','',str)
    str=re.sub(r'\s$','',str)
    return str
# 这里清除空行，多余空格和首尾空格

def clean_id(str):
    str=clean(str)
    str=re.findall(r'\d+',str)[0]
    return str
# 只剩下数字，找wca id 用

def clean_title(str):
    str=clean(str)
    str = str.replace(':', '')
    return str
#去掉冒号

def get_namenid(file):
    try:
        name=clean(get_soup(file).find('div',class_='member_name').text)
    except:
        print('name not found for %s'%file)
        name=''
    try:
        id=clean_id(get_soup(file).find('div',class_='member_id').text)
    except:
        print('id not found for %s'%file)
        id=''
    return (name,id)

# 得到公司名和id

def get_profile_table(file):
    # table=get_soup(file).find('div',{'class':'memberprofile_row'})
    table=get_soup(file).find('table')

    trs=table.find_all('tr')
    # tds=[tr for tr in trs]
    tds=[[clean(td.text) for td in tr.find_all('td')][:2] for tr in trs]
    tds=[td for td in tds if (len(td)>0)]
    return tds
#找到每行的两个元素，空行也有

def get_company_obj(file):
    trs=get_profile_table(file)
    company=Company()
    # company={}
    for tr in trs:
        if len(tr)==1 and 'contacts' in clean_title(tr[0]).lower():
            break
        try:
            if clean(tr[1])=='':
                continue
            company.__setattr__(clean_title(tr[0].lower()),clean(tr[1]))
        except:
            pass
    company.name,company.wca_id=get_namenid(file)
    
    return company


def get_groups(file):
    group=get_profile_table(file)
    trs=group.find_all('tr')
    # group=group.split('\n\n')
    tr=[[clean(td.text) for td in tr.find_all('td')] for tr in trs]
    return tr


def get_contacts_info(file):
    contacts=get_profile_table(file)
    contact_index=contacts.index(['.*Contacts\w*'])
    result=contacts[contact_index:]
    return result
# 得到除去contact以上部分

def get_contact_obj(file):
    contact_dicts=get_contacts_info(file)
    contact_obj=Contact()
    contacts=[]
    for ele in contact_dicts:
        if ''.join(ele)=='':
            contacts.append(contact_obj)
            contact_obj=Contact()
        try:
            contact_obj.__setattr__(clean_title(ele[0]).lower(),ele[1])
        except:
            pass
    # return [contact.__dict__ for contact in contacts]
    return contacts

# def startParse(nation):

#     for file in os.walk(tempdir[nation]):
#         try:
#             company=get_company_obj(file)
#             contacts=get_contact_obj(file)
#         except:

#             print ('info not generated.')
#         try:
#             db.session.add(company)
#             for contact in contacts:
#                 db.session.add(contact)
#         except:
#             print('info not added')
#             db.session.rollback()


    


