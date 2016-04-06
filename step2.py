from bs4 import BeautifulSoup
import os
import time
import pickle


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
for item in link2[400:902]:
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
pickle.dump(overallStr,open( "save2.p", "wb" ) )
    
    


import re
# to input:
over1 = pickle.load( open( "save.p", "rb" ) )
over2 = pickle.load(open( "save2.p", "rb" ))
overall = over1 + over2

sentences = []
for it1 in overall:
  for it2 in it1:
    search1 = bool(re.search('[0-9]+?_[0-9]=?',it2))
    if not search1:
      sentences.append(it2)

# break down into words
wordDictionary = {}
i=0
for item in sentences:
  i = i + 1
  temp = item.replace(u'\u3002','').replace(u'\uff0c','')
  for word in temp:
    if word in wordDictionary.keys():
      wordDictionary[word] = wordDictionary[word] + 1
    else:
      wordDictionary[word] = 1


# sort the values
import operator
sorted_Value = sorted(wordDictionary.items(), key=operator.itemgetter(1))
sorted_Value.reverse()

# print the top words
topChoice = 100
for item in sorted_Value[0:topChoice]:
  print item[0]



# titleAND author
author = []
for it1 in overall:
  for it2 in it1:
    search1 = bool(re.search('[0-9]+?_[0-9]=?',it2))
    if search1:
      author.append(it2)


# '\u300d' is the utf8 code for 」, it is at the end of every title. so i can use this to locate author

authorName = map(lambda x:x.replace(' ','').split(u'\u300d')[-1],author)
authorCount = {}
for item in authorName:
  if item in authorCount.keys():
    authorCount[item] = authorCount[item] + 1
  else:
    authorCount[item] = 1

sorted_author = sorted(authorCount.items(), key=operator.itemgetter(1))
sorted_author.reverse()
topChoice = 10
for item in sorted_author[0:topChoice]:
    print item[0], item[1]




pickle.dump(wordDictionary,open( "Words.p", "wb" ) )



# obtain ending word


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