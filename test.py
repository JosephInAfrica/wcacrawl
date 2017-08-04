import requests
from bs4 import BeautifulSoup
import re
import os
import time
import shutil

basedir = os.path.abspath(os.path.dirname(__file__))
tempdir_base = basedir+'\\temp\\'
# tempdir = {'us': tempdir_base+'\\usa\\',
#            'uk': tempdir_base+'\\uk\\',
#            'canada': tempdir_base+'\\canada\\',
#            'malaysia': tempdir_base+'\\malaysia\\'}


class tempdir(object):

    def __getattr__(self, attr):
        return basedir+'\\%s\\' % attr

print(tempdir.us)
