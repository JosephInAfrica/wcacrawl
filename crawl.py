import requests
from bs4 import BeautifulSoup
import re
import os
import time

basedir=os.path.abspath(os.path.dirname(__file__))
tempdir=basedir+'\\temp\\'
url='http://www.wcaworld.com/eng/mem_signin.asp'

headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
}

data={'username':'slszcn','password':'83981222','Rememberme':'1','REMOTE_ADDR':'113.110.149.149','language':'eng','referer':'http://www.wcaworld.com'}

def get_login_session():

	session=requests.Session()
	req=session.get(url,headers=headers)
	bsobj=BeautifulSoup(req.text,'html.parser')

	login_addr=bsobj.find('form',{'name':'login'})['action']

	log=session.post(login_addr,data=data,headers=headers)

	return session


def purge_name(name):
	name=name.replace('?','')
	name=name.replace('\\','')
	name=name.replace('/','')
	return name[9:]

def get_text(url,session):
	
	text=session.get(url,headers=headers)
	with open(tempdir + purge_name(url) +'.txt','wb') as file:
		file.write(text.text.encode('utf-8'))
	print (url+'written \n')
	time.sleep(1)


def read_urls(file):
	with open(basedir+'\\'+file,'r') as file:
		urls=file.read().split('\n')
	return urls


def crawl_wca(file):
	session=get_login_session()
	for url in read_urls(file):
		if purge_name(url)+'.txt' in os.listdir():
			continue
		print (url+'is being collected...')
		try:

			get_text(url,session)
		except ConnectionError:
			session=get_login_session()
			get_text(url,session)


if __name__=='__main__':
	crawl_wca('wcausa.txt')