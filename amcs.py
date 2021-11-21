import requests
import zipfile
import io
from bs4 import BeautifulSoup
from contextlib import redirect_stdout

mod_id = input('Type the ID of the mod')
page = requests.get('https://smods.ru/?s=' + mod_id + '&app=255710')
soup = BeautifulSoup(page.text, 'html.parser')

p_items = soup.find_all('p')
for p in p_items:
    #es una lista el coso de finder
    finder = p.find(class_="skymods-excerpt-btn")
    if finder != None:
        if "Download" in finder:
            print(finder)
            printed_text = finder

with open('txt.tmp', 'w') as f:
    with redirect_stdout(f):
        print(printed_text)

with open('txt.tmp', 'r') as file:
    data = file.read().rstrip()

#Q: Why are you grabbing the print output, saving it, and reloading it again?
#Wouldn't it be more efficient to just set it as a variable?
#A: Beacuse for some reason when setting it as a variable it ends up as "NoneType"
#and the only way to fix it is doing this I think. I don't know that much about coding
#so feel free to correct me or find whats wrong.

soup = BeautifulSoup(data, "html.parser")

for a in soup.find_all('a', href=True):
    urlfound = a['href']

print("URLFOUND:")
print(urlfound)

#idfinder function
if 'modsbase.com' in urlfound:
    if 'https://' in urlfound:
        dom_removed = urlfound.replace('https://modsbase.com/', '')
    elif 'http://' in urlfound:
        dom_removed = urlfound.replace('http://modsbase.com/', '')
    else:
        print('No HTTPS or HTTP protocol found in "urlfound".')
        exit()
else:
    print('No modsbase.com found.')
    exit()





download_id = dom_removed.split('/')[0]

if '.html' in dom_removed:
    nohtml = dom_removed.replace('.html', '')
    mod_archivename = nohtml.split('/')[1]

print('DOWNLOAD_ID: ' + download_id)
print(mod_archivename)

cookies = {
    'aff': '10384',
    'lang': 'spanish',
    'ref_url': 'https%3A%2F%2Fsmods.ru%2F',
    'we-love-cookies': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://modsbase.com',
    'Alt-Used': 'modsbase.com',
    'Connection': 'keep-alive',
    'Referer': urlfound,
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'TE': 'trailers',
}

data = {
  'op': 'download2',
  # the id is important, changes everything
  'id': download_id,
  'rand': '',
  'referer': 'https://smods.ru/',
  'method_free': 'Liberta Descarga',
  #Premium? is there a paywall or something?
  'method_premium': ''
}

response = requests.post(urlfound, headers=headers, cookies=cookies, data=data)

print(response.status_code)
print(response.url)
print("request_zip set")
request_zip = requests.get(response.url)
print("io zip")
z = zipfile.ZipFile(io.BytesIO(request_zip.content))

print("extracting")
z.extractall()
