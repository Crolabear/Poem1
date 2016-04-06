import pickle
import random
import itertools


over1 = pickle.load( open( "save.p", "rb" ) )
over2 = pickle.load(open( "save2.p", "rb" ))
overall = over1 + over2

individual = pickle.load(open( "Words.p", "rb" ))

terms = individual.keys()

termTranslate = {}
i=0
for item in terms:
  termTranslate[item] = i
  i= i + 1


import re
# i want to use this to create a relative matrix.
sentences = []
for it1 in overall:
  for it2 in it1:
    search1 = bool(re.search('[0-9]+?_[0-9]=?',it2))
    if not search1:
      sentences.append(it2)
      
wordinNumber = []
for it3 in sentences:
  temp = []
  for it4 in it3:
    try:
      temp.append(termTranslate[it4])
    except KeyError:
      pass
  wordinNumber.append(temp)
  

import itertools
matrix1 = map(lambda x: map(tuple,itertools.permutations(x,2)),wordinNumber)

# this is very slow, + is slow, append as faster.
# combineMat = []
# for item in matrix1:
#   combineMat = combineMat + item
#   

combineMat2 = []
for item in matrix1:
  for item2 in item:
    combineMat2.append(item2) 



matrix2 = []
for item in range(len(termTranslate.values())):
  for item2 in combineMat2:
    temp = []
    if item2[0] == item:
      matrix2.append(temp)





# split into categories, 5 words, 7 words ... 


splited = []
temp1 = []
for itm1 in overall:
  for itm2 in itm1:
    search1 = bool(re.search('[0-9]+?_[0-9]=?',itm2))
    if search1:
      splited.append(temp1)
      temp1 = []
    else:
      temp1.append(itm2)
      


lines = []
for item in sentences:
  temp = item.replace(u'\u3000','').split(u'\u3002')[0:-1]
  temp2 = []
  for item in temp:
    temp2.append(item.split(u'\uff0c'))
  for i3 in temp2:
    lines.append(i3)


chain = itertools.chain(*lines)
sentSegment = list(chain)     

def generatePoemBySentences(numberLine,wordPerLine,sentenceSegment = None):
  if sentenceSegment != None:
    wordz = []
    for item in sentenceSegment:
      if len(item) == wordPerLine:
        wordz.append(item)
    lenz = len(wordz)
    indez = random.sample(range(lenz),numberLine)
    newPoem = []
    for item2 in indez:
      newPoem.append(wordz[item2])
  else:
    newPoem = []
    
  for item in newPoem:
    print item  
  return newPoem
  

# next i want to find out the location of each word in the sentence
# if 5 terms, then first 2, middle, last 2
# if 7 words, then first 2, middle 2, last 3


# so each term will have 3 numbers, the first 1 is the number of occurance in first 2
# number of times it show up in middle, number of times it show up in last 2
IndexFor5 = {}
for item in terms:
  temp = []
  for item2 in sentSegment:
    if (len(item2) == 5) and (item in item2):
      temp.append(re.search(item, item2).start())
  IndexFor5[item] = temp    
      
pickle.dump(IndexFor5,open( "WordsANDposition.p", "wb" ) )
 
 
IndexFor7 = {}
for item in terms:
  temp = []
  for item2 in sentSegment:
    if (len(item2) == 7) and (item in item2):
      temp.append(re.search(item, item2).start())
  IndexFor7[item] = temp        

pickle.dump(IndexFor7,open( "Words7position.p", "wb" ) )



# obtain ending words, it's an ordered pair (A,B) 
# A is the ending word in the first line, B is the ending word in the second line.
# AB form the 1 sentence. 

orderedWord = []
for item in lines:
  try:
    orderedWord.append((item[0][-1],item[1][-1]))
  except IndexError:
    pass


# turn ordered pair into dictionary:
endWordDic= {}
wordlist = []
for item in orderedWord:
  wordlist.append(item[0])
  
  
newDic =   {}
for item in set(wordlist):
  temp = []
  for i2 in orderedWord:
    if item == i2[0]:
      temp.append(i2[1])
  newDic[item] = temp
  
# next we want to know how the program goes.
# i want to begin with a random line
# then base on the final word, come up with the next line
# base on the final word, come up with another line


  
# for fun
numOccurs = []
for x,y in newDic.items():
  numOccurs.append((x,len(y)))
 
import operator
# this is how we sort base on the 2nd paramenter
numOccurs.sort(key=operator.itemgetter(1),reverse = True)
  
for item in numOccurs[0:30]:
  print item[0],item[1]
  
  
  

def obtainNextLine(endWord,charNum,endWordDictionary,list1):
  indez = []
  temp = []
  
  # this is to filter out all sentences of not matching length
  for item in list1:
    if len(item) == charNum:
      temp.append(item)

# now i want to use the endword provided to come up with a different end word that associates with it.
  try:
    possibleMatch = random.choice(endWordDictionary[endWord])
  except KeyError:
    possibleMatch = u'\u5b8c'
  
  i = 0    
  for item2 in temp:
    if possibleMatch == item2[-1]:
      indez.append(i)
    i=i+1
  
  if indez: 
    int1 = random.choice(indez)
    sent = temp[int1]
    print 1
  else:
    int2 = random.choice(range(len(temp)))
    sent = temp[int2]
    print 2
  return sent  




  
def generatePmHarder(numberLine,wordPerLine, endWordDic,sentenceSegment = None):
  if sentenceSegment != None:
    wordz = []
    for item in sentenceSegment:
      if len(item) == wordPerLine:
        wordz.append(item)
    lenz = len(wordz)
    line1 = random.sample(wordz,1)[0]
    storing = []
    storing.append(line1)
    
    count = numberLine - 1
    for item in range(count):
      line1 = obtainNextLine(line1[-1],wordPerLine,endWordDic,sentenceSegment)
      storing.append(line1)
    
      newPoem= storing
  else:
    newPoem = []
    
  for item in newPoem:
    print item  
  return newPoem
  

# so all we need is to type generatePmHarder to get a new poem
randomPoem = generatePmHarder(4,7,newDic,sentSegment)
