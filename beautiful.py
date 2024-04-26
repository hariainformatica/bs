#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#https://pythonprogramming.net/introduction-scraping-parsing-beautiful-soup-tutorial/


import bs4 as bs
import urllib.request

url = 'https://pythonprogramming.net/parsememcparseface/'
source = urllib.request.urlopen(url).read()

soup = bs.BeautifulSoup(source, 'lxml')

#print(soup.title)

#print(soup.title.name)

#print(soup.title.string)

#print(soup.find_all('p'))