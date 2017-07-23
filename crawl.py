import requests
from bs4 import BeautifulSoup
import re
import os
import time
import shutil

basedir = os.path.abspath(os.path.dirname(__file__))
tempdir_base = basedir+'\\temp\\'
tempdir = {'us': tempdir_base+'\\usa\\',
           'uk': tempdir_base+'\\uk\\',
           'canada': tempdir_base+'\\canada\\'}


url = 'http://www.wcaworld.com/eng/mem_signin.asp'

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
           }

data = {'username': 'chipro', 'password': '382896', 'Rememberme': '1',
        'REMOTE_ADDR': '113.110.149.149', 'language': 'eng', 'referer': 'http://www.wcaworld.com'}


def get_login_session():
    session = requests.Session()
    req = session.get(url, headers=headers)
    bsobj = BeautifulSoup(req.text, 'html.parser')
    login_addr = bsobj.find('form', {'name': 'login'})['action']
    log = session.post(login_addr, data=data, headers=headers)
    return session


def purge_name(name):
    name = name.replace('?', '')
    name = name.replace('\\', '')
    name = name.replace('/', '')
    return name[9:]


def get_text(url, session, destined_dir):

    text = session.get(url, headers=headers)
    with open(destined_dir + purge_name(url) + '.txt', 'wb') as file:
        file.write(text.text.encode('utf-8'))
    # print (url+'written \n')
    # time.sleep(1)


def read_urls(file):
    with open(basedir+'\\'+file, 'r') as file:
        urls = file.read().split('\n')
    return urls


def crawl_wca(file, destined_dir):
    session = get_login_session()
    for url in read_urls(file):
        destined_file_name = purge_name(url)+'.txt'

        if destined_file_name in os.listdir(destined_dir):
            print(url+'was collected before.')
            continue
        try:
            print(url+'is being collected...')

            get_text(url, session, destined_dir)
        except:
            print('connection Error: Trying to reconect in 10s')
            time.sleep(10)
            print('connection Restarted')
            session = get_login_session()
            get_text(url, session, destined_dir)
        finally:
            print(url+'  collection finished.')


def select_wca(file, destined_dir):
    for url in read_urls(file):
        destined_file_name = purge_name(url)+'.txt'
        if destined_file_name in os.listdir(destined_dir):
            shutil.copyfile(destined_dir+destined_file_name,
                            destined_dir+'selected\\%s' % destined_file_name)


if __name__ == '__main__':
    crawl_wca('wcacanada.txt', tempdir['canada'])
    # select_wca('wcacanada.txt',tempdir['canada'])
