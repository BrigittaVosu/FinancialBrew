import urllib.request
import csv
import re
from bs4 import BeautifulSoup

rank_page = 'https://finance.yahoo.com/quote/MALOX/performance?p=MALOX'
req = urllib.request.Request(rank_page, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'})
page = urllib.request.urlopen(req)
soup = BeautifulSoup(page, 'html.parser')

channels = soup.find('div', attrs={'class': 'Mb(25px)'}).find_all('div')

# malox_raw = row.find('div', attrs={'style': 'float: left; width: 80px;'})
# if malox_raw is not None:
#     malox = malox_raw.span.text.strip()

#file = open('firstextract.csv', 'wt')
#writer = csv.writer(file)

# #write title row
# writer.writerow(['Return', 'MALOX', 'Category'])

for channel in channels:
    #username = channel.find('span', attrs={'class': 'Fl(start)'}).a.text.strip()
    uploads = channel.find('span', attrs={'class': 'Fl(start)'})
    if uploads is not None:
        uploads = uploads.span.text.strip()
    
    views = channel.find('span', attrs={'class': 'Fl(end)'})
    if views is not None:
        for view in views:
            if view is not None:
                print(view)
        
    #views = views.span.text.strip()
    #views = channel.find_all('span', attrs={'class': 'Fl(start)'}).span.text.strip()

    #print (uploads + ' ' + views)
    #writer.writerow([uploads.encode('utf-8')])

#file.close() 