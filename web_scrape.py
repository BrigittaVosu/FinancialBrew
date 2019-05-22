import urllib.request
import csv
import re
from bs4 import BeautifulSoup

rank_page = 'https://finance.yahoo.com/quote/MALOX/performance?p=MALOX'
req = urllib.request.Request(rank_page, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'})
page = urllib.request.urlopen(req)
soup = BeautifulSoup(page, 'html.parser')

perfReturns = soup.find('section', attrs={'class': 'Pb(20px) smartphone_Px(20px) smartphone_Mt(20px)'}).find_all('span')

# print(perfReturns)

# file = open('firstextract.csv', 'wt')
# writer = csv.writer(file)

# #write title row
# writer.writerow(['Return', 'MALOX', 'Category'])

for row in perfReturns:
    realReturn = row.find('span', attrs={'class': 'W(50%) D(b) Fl(start) Ta(s)'})
# #     MALOX = row.find('div', attrs={'style': 'float: left; width: 80px;'}).span.text.strip()
# #     category = row.find_all('div', attrs={'style': 'float: left; width: 150px;'})[1].span.text.strip()

print(realReturn)

# #     print (realReturn + ' ' + MALOX + ' ' + category)
# #     writer.writerow([realReturn.encode('utf-8'), MALOX.encode('utf-8'), category.encode('utf-8')])

# file.close()
