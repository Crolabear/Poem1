from bs4 import BeautifulSoup
import os
import time



def downloadLink(menuLink):
  os.system('php sca1.php %s' %menuLink)
  with open("textPage.html","r") as f:
    docText = f.read()
    data = BeautifulSoup(docText)
  return data


with open('menuLink.txt','r') as f:
  linkz = f.read()
link2 = linkz.split('http://') 



def parsePoem(link2Item):
  test = link2Item
  data = downloadLink(test)

  a=data.find(**{"class": "son2s"})
  c=str(a).split('<br/><br/>')
  utfString = []
  for item in c:
    if '<' not in item:
       utfString.append(item.decode('utf8'))
  return utfString




# now loop through each one and print them
import codecs
import random
import time

i=0
overallStr = []
for item in link2[300:400]:
  print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
  print i
  i=i+1
  poemLine = parsePoem(item)
  overallStr.append(poemLine)
  
  # then i want to wait before downloading:
  Rint=random.choice([3,4,5,6,7,8,9])  
  time.sleep(Rint)
  
  with codecs.open('PoemRecord.txt','a',"utf-8") as f:
    f.write(item+'/n')
    for item2 in poemLine:
      f.write(item2)
    f.write('/n')
  


# back up the string we saved
import pickle
pickle.dump(overallStr,open( "save.p", "wb" ) )
    
    

# 
# 
# 
# from HTMLParser import HTMLParser
# 
# class MLStripper(HTMLParser):
#     def __init__(self):
#         self.reset()
#         self.fed = []
#     def handle_data(self, d):
#         self.fed.append(d)
#     def get_data(self):
#         return ''.join(self.fed)
# 
# def strip_tags(html):
#     s = MLStripper()
#     s.feed(html)
#     return s.get_data()  