import requests
from bs4 import BeautifulSoup
import re


url='https://www.whatismybrowser.com/'

headers={"User-Agent":"Mozilla/5.0 (Macintosh;Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",

}

params={'firstname':'Joseph','lastname':'Li'}

session=requests.Session()

req=session.get(url,headers=headers)

# print req.__dict__

print req.cookies.get_dict()

bsobj=BeautifulSoup(req.text,'html.parser')


print bsobj.find('div',{'class':'string-major'})
print session.__dict__


# # bsobj=BeautifulSoup(open('index.html','r'),'html.parser')
# login_addr=bsobj.find('form',{'name':'login'})['action']

# random_no=re.compile('\d+').findall(login_addr)[0]

# print login_addr

# print random_no


# log=session.post(login_addr,params=params,headers=headers)

# logobj=BeautifulSoup(log.text,'html.parser')
# with open('login.html','w+') as file:
# 	file.write(logobj.encode('utf-8'))

# print session.cookies
# print session.headers

# # print .write(request.get(url,headers=headers).open())
# # with open('index.html','w+') as file:
# # 	file.write(bsobj.encode('utf-8'))

# # print bsobj