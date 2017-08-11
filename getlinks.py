from bs4 import BeautifulSoup as soup
import re
import os

cid_re = re.compile(u'members.asp\?cid=\w+')

file_path = os.path.abspath(os.path.join(os.getcwd(), 'agentpages'))
output_path = os.path.abspath(os.path.join(os.getcwd(), 'outputurllists'))

if not os.path.exists(output_path):
    os.makedirs(output_path)
if not os.path.exists(file_path):
    os.makedirs(file_path)


def parse_name(name):
    pattern = re.compile(r'(\w+)\.html')
    return re.findall(pattern, name)


def parse_folder(folder=file_path):
    for file_name in os.listdir(r'D:\joseph\wcacrawler\agentpages'):
        # name = parse_name(file_name)

        # if name is None:
        #     continue
        # print file_name
        print(file_name)
        country = os.path.splitext(file_name)[0]
        get_country_links(country)


def get_country_links(country_name):
    with open(os.path.join(file_path, '%s.html' % country_name, ), 'rb') as file:
        chunk = file.read()

    chunk_soup = soup(chunk, 'html.parser')

    trs = chunk_soup.find_all('tr')

    cids = [tr.find('a')['href'] for tr in trs if tr.find('a') != None]

#   cids=[ul.find('a').href for ul in uls]


#   # cids=re.findall(cid_re,chunk)
    def clean(url):
        base = 'http://www.wcaworld.com/eng/'
        if url[:4] != 'http':
            url = '%s%s' % (base, url)
        return url

    cids = [clean(cid) for cid in cids]
    print(cids)

    with open(os.path.join(output_path, 'wca%s.txt' % country_name), 'w+') as file:
        file.write('\n'.join(cids))
    print('%s written' % cids)

    # return cids
parse_folder()

# def get_us_links(country_name='us'):
#     with open('%s.html' % country_name, 'rb') as file:
#         chunk = file.read()

#     chunk_soup = soup(chunk, 'html.parser')

#     trs = chunk_soup.find_all('tr')

#     cids = [tr.find('a')['href'] for tr in trs if tr.find('a') != None]

# #   cids=[ul.find('a').href for ul in uls]


# #   # cids=re.findall(cid_re,chunk)
#     def clean(url):
#         base = 'http://www.wcaworld.com/eng/'
#         if url[:4] != 'http':
#             url = '%s%s' % (base, url)
#         return url

#     cids = [clean(cid) for cid in cids]
#     print(cids)

#     with open('wca%s.txt' % country_name, 'w+') as file:
#         file.write('\n'.join(cids))


# if __name__ == '__main__':
#     parse_folder()
