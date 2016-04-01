from bs4 import BeautifulSoup
import os
import time


menuLink = 'http://www.gushiwen.org/gushi/quantang.aspx'
def downloadLink(menuLink):
  os.system('php sca1.php %s' %menuLink)
  with open("textPage.html","r") as f:
    docText = f.read()
    data = BeautifulSoup(docText)
  return data

data = downloadLink(menuLink)
links = data.find_all('a',target = "_blank")

newLinks=[]
for item in links:
  if 'wen_' in item['href']:
    newLinks.append('http://www.gushiwen.org'+item['href'])
    
# so at this point, i have all the links to the different poems.
# i will then download those pages.

with open('menuLink.txt','w') as g:
  for item in newLinks:
    g.write(item)
    
    


