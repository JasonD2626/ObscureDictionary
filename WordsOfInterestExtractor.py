from bs4 import BeautifulSoup
import requests
import random
from PyDictionary import PyDictionary
dc = PyDictionary() 
url = input("Enter link: ")
res = requests.get(url)
page = res.content
soup = BeautifulSoup(page, 'html.parser')
text = soup.find_all(text=True)
output = ''
blacklist = [
    '[document]',

   'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    'style',
]

commonWords = []

myFile = open("wiki-100k.txt", encoding="utf8")

myFile = myFile.read().splitlines()

for line in myFile:
    commonWords.append(line)


for t in text:
    if t.parent.name not in blacklist:
        output += '{} '.format(t)

wordsList = []
sentenceList = []



addedWord = ""
for i in output:
    if i != "" and i != "\n" and i != '' and i != " " and i.isnumeric() == False and i != "_" and i != "," and i != "." and i != "!" and i != "“" and i != "”" and i != "?" and i != "(" and i != ")" and i != "{" and i != "}":
        addedWord += i
    else:
        if addedWord != "":
            wordsList.append(addedWord)
            addedWord = ""

  

for i in wordsList:
    if i in commonWords or "#" in i or "[" in i or "(" in i or len(i) < 7 or ")" in i or i[0].istitle() == True: 
        wordsList.remove(i)


newWordsList = []

for i in wordsList:
    if i not in newWordsList:
        newWordsList.append(i)

for z in range(0, len(newWordsList)):
    print(str(z) + ":" + newWordsList[z])


userInput = ""

while userInput.lower() != "n":
    userInput = input("Type 'n' if you want to exit. Which number word do you want to see the meaning of?:  ").lower()
    if userInput.isdigit():
        print(dc.meaning(newWordsList[int(userInput)]))
    else:
        print('Please enter a valid response.')

    
    

