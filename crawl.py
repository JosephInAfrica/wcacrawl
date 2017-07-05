import requests
from bs4 import BeautifulSoup
import re


url='http://www.wcaworld.com/eng/mem_signin.asp'

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",'Cookie':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',"Connection":"keep-alive"
}

params={'username':'slszcn','password':'83981222','Rememberme':'1','REMOTE_ADDR':'113.110.149.149','language':'eng','referer':'http://www.wcaworld.com'}

session=requests.Session()

req=session.get(url,headers=headers)

bsobj=BeautifulSoup(req.text,'html.parser')

# bsobj=BeautifulSoup(open('index.html','r'),'html.parser')
# print bsobj
login_addr=bsobj.find('form',{'name':'login'})['action']

# random_no=re.compile('\d+').findall(login_addr)[0]

# print req.__dict__
# print '\n\n'
# print req.headers.__dict__
# print '\n\n'
print login_addr

log=session.post(login_addr,data=params,headers=headers,cookies=req.cookies)

# print log.__dict__
print session.headers.__dict_
_print '\n\n'
print log.headers.__dict__
print log.cookies.get_dict()

# logobj=BeautifulSoup(log.text,'html.parser')

# with open('login.html','w+') as file:
# 	file.write(logobj.encode('utf-8'))

# # print session.cookies
# print session.headers

# print .write(request.get(url,headers=headers).open())
# with open('index.html','w+') as file:
# 	file.write(bsobj.encode('utf-8'))

# print bsobj