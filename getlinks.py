from bs4 import BeautifulSoup as soup
import re

cid_re=re.compile(u'members.asp\?cid=\w+')
with open('us.html','r') as file:
	chunk=file.read()

# print (chunk)

chunk_soup=soup(chunk,'html.parser')

cids=[cid['href'] for cid in chunk_soup.find_all('a')]


# cids=re.findall(cid_re,chunk)
def clean(url):
	base='http://www.wcaworld.com/eng/'
	if url[:4] !='http':
		url='%s%s'%(base,url)
	return url

cids=[clean(cid) for cid in cids]

with open('wcausa.txt','w+') as file:
	file.write('\n'.join(cids))

print (cids)