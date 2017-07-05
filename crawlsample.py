import requests
from bs4 import BeautifulSoup
import re


url='http://pythonscraping.com/pages/files/processing.php'

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",

}

params={'firstname':'Joseph','lastname':'Li'}

session=requests.Session()

req=session.post(url,headers=headers,data=params)

print req.__dict__

bsobj=BeautifulSoup(req.text,'html.parser')


print bsobj
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