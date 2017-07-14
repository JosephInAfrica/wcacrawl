from bs4 import BeautifulSoup as soup
import re

cid_re=re.compile(u'members.asp\?cid=\w+')

def get_country_links(country_name):
	with open('%s.html'%country_name,'rb') as file:
		chunk=file.read()

	# print (chunk)

	chunk_soup=soup(chunk,'html.parser').find('div',id='showSearch')
	
	trs=chunk_soup.find_all('tr')
	
	cids=[tr.find('a')['href'] for tr in trs if tr.find('a') != None]

# 	cids=[ul.find('a').href for ul in uls]


# 	# cids=re.findall(cid_re,chunk)
	def clean(url):
		base='http://www.wcaworld.com/eng/'
		if url[:4] !='http':
			url='%s%s'%(base,url)
		return url

	cids=[clean(cid) for cid in cids]
	print (cids)

	with open('wca%s.txt'%country_name,'w+') as file:
		file.write('\n'.join(cids))


def get_us_links(country_name='us'):
	with open('%s.html'%country_name,'rb') as file:
		chunk=file.read()

	
	chunk_soup=soup(chunk,'html.parser')
	
	trs=chunk_soup.find_all('tr')
	
	cids=[tr.find('a')['href'] for tr in trs if tr.find('a') != None]

# 	cids=[ul.find('a').href for ul in uls]


# 	# cids=re.findall(cid_re,chunk)
	def clean(url):
		base='http://www.wcaworld.com/eng/'
		if url[:4] !='http':
			url='%s%s'%(base,url)
		return url

	cids=[clean(cid) for cid in cids]
	print (cids)

	with open('wca%s.txt'%country_name,'w+') as file:
		file.write('\n'.join(cids))



if __name__=='__main__':
	get_country_links('uk')