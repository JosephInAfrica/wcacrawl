# with open('wcausa.txt','r') as file:
#     urls=file.read()

# urls=urls.split('\n')

import requests
a=requests.get('https://www.baidu.com/')

print (a.text)

with open('baidu.html','wb') as file:
    file.write(a.text.encode('utf-8'))