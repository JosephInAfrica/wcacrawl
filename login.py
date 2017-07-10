import requests
from bs4 import BeautifulSoup
import re
import 

url='http://www.wcaworld.com/eng/mem_signin.asp'

headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
}

params={'username':'slszcn','password':'83981222','Rememberme':'1','REMOTE_ADDR':'113.110.149.149','language':'eng','referer':'http://www.wcaworld.com'}


cookie=[
{
    "domain": ".wcaworld.com",
    "expirationDate": 1562742470,
    "hostOnly": false,
    "httpOnly": false,
    "name": "__utma",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "107036932.625727288.1499221663.1499657663.1499666426.13",
    "id": 1
},
{
    "domain": ".wcaworld.com",
    "expirationDate": 1499672270,
    "hostOnly": false,
    "httpOnly": false,
    "name": "__utmb",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "107036932.15.10.1499666426",
    "id": 2
},
{
    "domain": ".wcaworld.com",
    "hostOnly": false,
    "httpOnly": false,
    "name": "__utmc",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "107036932",
    "id": 3
},
{
    "domain": ".wcaworld.com",
    "expirationDate": 1499671044,
    "hostOnly": false,
    "httpOnly": false,
    "name": "__utmt",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "1",
    "id": 4
},
{
    "domain": ".wcaworld.com",
    "expirationDate": 1515438470,
    "hostOnly": false,
    "httpOnly": false,
    "name": "__utmz",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "107036932.1499221663.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)",
    "id": 5
},
{
    "domain": "www.wcaworld.com",
    "hostOnly": true,
    "httpOnly": false,
    "name": "ASPSESSIONIDAACDCDQR",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "HEDPMONACCBMIGNILJMGFOIG",
    "id": 6
},
{
    "domain": "www.wcaworld.com",
    "hostOnly": true,
    "httpOnly": false,
    "name": "member",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "yes",
    "id": 7
},
{
    "domain": "www.wcaworld.com",
    "expirationDate": 1499825584.274171,
    "hostOnly": true,
    "httpOnly": false,
    "name": "password",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "382896",
    "id": 8
},
{
    "domain": "www.wcaworld.com",
    "expirationDate": 1514786100,
    "hostOnly": true,
    "httpOnly": false,
    "name": "showsc",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "no",
    "id": 9
},
{
    "domain": "www.wcaworld.com",
    "expirationDate": 1499825584.274172,
    "hostOnly": true,
    "httpOnly": false,
    "name": "username",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "chipro",
    "id": 10
}
]

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