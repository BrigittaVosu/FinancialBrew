import urllib.request
import csv
import re
from bs4 import BeautifulSoup

rank_page = 'https://finance.yahoo.com/quote/MALOX/performance?p=MALOX'
req = urllib.request.Request(rank_page, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'})
page = urllib.request.urlopen(req)
soup = BeautifulSoup(page, 'html.parser')

divTags = soup.find('div', attrs={'class': 'Mb(25px)', 'data-reactid': '56'}).find_all('div')

# malox_raw = row.find('div', attrs={'style': 'float: left; width: 80px;'})
# if malox_raw is not None:
#     malox = malox_raw.span.text.strip()

#file = open('firstextract.csv', 'wt')
#writer = csv.writer(file)

# #write title row
# writer.writerow(['Return', 'MALOX', 'Category'])

for divTag in divTags:
    perfTitle = divTag.find('span', attrs={'class': 'W(50%) D(b) Fl(start) Ta(s)'})
    # if perfTitle is not None:
    #     perfTitle = perfTitle.span.text.strip()
    if perfTitle is not None:
        for row1 in perfTitle:
            if row1 is not None:
                try:
                    row1 = row1.text.strip()
                except:
                    pass
    

    performances = divTag.find('span', attrs={'class': 'W(20%) D(b) Fl(start) Ta(e)'})
    if performances is not None:
        for row2 in performances:
            if row2 is not None:
                try:
                    row2 = row2.text.strip()
                except:
                    pass
        
    #views = views.span.text.strip()
    #views = channel.find_all('span', attrs={'class': 'Fl(start)'}).span.text.strip()

    print (row1 + ' ' + row2)
    #writer.writerow([uploads.encode('utf-8')])

#file.close() 