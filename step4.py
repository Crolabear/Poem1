import pickle
import random
import itertools
import re


over1 = pickle.load( open( "save.p", "rb" ) )
over2 = pickle.load(open( "save2.p", "rb" ))
endWordz = pickle.load(open( "endWord.p", "rb" ) )

overall = over1 + over2

individual = pickle.load(open( "Words.p", "rb" ))

terms = individual.keys()


# i want to use this to create a relative matrix.
sentences = []
for it1 in overall:
  for it2 in it1:
    search1 = bool(re.search('[0-9]+?_[0-9]=?',it2))
    if not search1:
      sentences.append(it2)
      


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


termPosition = {}
def findTermLocation(term,poemList):
  temp = []
  for item in poemList:
    if term in item:
      a = re.search(term, item).start()
      temp.append(a)
  return (term,temp)

for item in terms:
  k = findTermLocation(item,sentSegment)
  termPosition[k[0]] = k[1]  

pickle.dump(termPosition,open( "termPosition", "wb" ) )

  
# what do i do after i obtain the position of each word?
# it will be nice if i can have a map that tells me how words are related
# for a given word, i want a list of all words that 

#1 generate random words without any relationship

def pick1Word(location,wordList):
  temp = []
  for keyz,valz in wordList.items():
    if location in valz:
      temp.append(keyz)
  return random.choice(temp)    

def simpleGenWords(lines,wordPerLine, wordDictionary):
  newPoem = []
  for item in range(lines):
    tempSent = ''
    for item2 in range(wordPerLine):
      tempSent = tempSent + pick1Word(item2,wordDictionary)
    newPoem.append(tempSent)  
  return newPoem
  
  
# next i want to come up with a data structure to relate words
# the input should be sentSegment
bi = []
tri = []
for item in sentSegment:
  if len(item) == 5:
    bi.append(item[0:2])
    tri.append(item[2:5])
  if len(item) == 7:
    bi.append(item[0:2])
    bi.append(item[2:4])
    tri.append(item[4:7])




def pieceBiTri(leng,biList,triList):
  if leng == 5:
    newLine = random.choice(biList)+random.choice(triList)
  if leng == 7:
    newLine = random.choice(biList)+random.choice(biList)+random.choice(triList)
  return newLine
  
  
def genRymPoem(lines,wordPerLine,biList,triList):
  newPoem = []
  for item in range(lines):
    newPoem.append(pieceBiTri(wordPerLine,biList,triList)) 
  return newPoem  
  
  
example = genRymPoem(4,5,bi,tri)



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


def getitRhyme(numberLine,leng,endWordDic,biList,triList):
  storing = []
  line1 = random.sample(triList,1)[0]
  storing.append(line1)
  count = numberLine - 1
  for item in range(count):
    line1 = obtainNextLine(line1[-1],3,endWordDic,triList)
    storing.append(line1)
  newPoem = []
  if leng == 5:
    for item in storing:
      newPoem.append(random.choice(biList)+item)
  if leng == 7:
    for item in storing:
      twoItem = random.sample(biList,2)
      newPoem.append(twoItem[0]+twoItem[1]+item)

  return newPoem
  
 
  


  


