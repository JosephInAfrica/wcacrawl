# "This is to download pages from links list.已经下过的不会再下载"


import requests
from bs4 import BeautifulSoup
import re
import os
import time
import shutil


basedir = os.path.abspath(os.path.dirname(__file__))

destined_dir = os.path.join(basedir, 'outputurllists')
tempdir = os.path.join(basedir, 'temp')
# tempdir_base = basedir+'\\temp\\'
# tempdir = {'us': tempdir_base+'\\usa\\',
#            'uk': tempdir_base+'\\uk\\',
#            'canada': tempdir_base+'\\canada\\',
#            'malaysia': tempdir_base+'\\malaysia\\',
#            'newzealand': tempdir_base+'\\newzealand\\'}


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
    with open(os.path.join(destined_dir, purge_name(url) + '.txt'), 'wb')as file:
        file.write(text.text.encode('utf-8'))
    # print (url+'written \n')
    # time.sleep(1)


def read_urls(file):
    with open(file, 'r') as file:
        urls = file.read().split('\n')
    return urls


def crawl_wca(destined_dir=destined_dir, tempdir=tempdir):
    session = get_login_session()

    for file_name in os.listdir(destined_dir):
        output_dir = os.path.join(tempdir, os.path.splitext(file_name)[0])
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        print('%s is being parsed...' % file_name)

        for url in read_urls(os.path.join(destined_dir, file_name)):
            destined_file_name = purge_name(url)+'.txt'

            if url == '':
                continue

            if destined_file_name in os.listdir(output_dir):
                print(url+'was collected before.')
                continue

            try:
                print(file_name+'>>'+url+'is being collected...')
                get_text(url, session, output_dir)
            except:
                print('connection Error: Trying to reconect in 10s')
                time.sleep(10)
                print('connection Restarted')

                session = get_login_session()
                try:
                    get_text(url, session, output_dir)
                except:
                    print('%s failed after trying twice.' % url)
            finally:
                print(url+'  collection finished.')


if __name__ == '__main__':
    crawl_wca()
