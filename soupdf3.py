"""
simple script for downloading all the PDFs from given URL
using python 3
"""
from bs4 import BeautifulSoup
import urllib
import urllib.request
import shutil
import re


url = input('Enter url:')  # u'http://www.some.thing/'
htm = urllib.request.urlopen(url)
soup = BeautifulSoup(htm, 'html.parser')

pdfs = []
for link in soup.find_all('a'):
    s = link.get('href')
    if re.search('\.pdf', s):
        if u'http' not in s:
            urlparsed = urllib.parse.urlparse(url)
            s = urlparsed.scheme + '://' + urlparsed.netloc + '/' + s
        pdfs.append(s)

for i, pdfurl in enumerate(pdfs, 1):
    print('downloading {} out of {}'.format(i, len(pdfs)))
    print(pdfurl)
    with urllib.request.urlopen(pdfurl) as response, open("{}.pdf".format(i), 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
