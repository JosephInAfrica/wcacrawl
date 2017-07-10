from bs4 import BeautifulSoup as soup

def get_soup(file):
	with open(file) as file:
		soup=soup(file.read())

	return soup


def get_info(soup):
	