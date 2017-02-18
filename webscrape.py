from bs4 import BeautifulSoup
import urllib2

url = "http://www.webpagefx.com/tools/emoji-cheat-sheet/"

req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
content = urllib2.urlopen( req)

# content = urllib2.urlopen(url).read()

emojiNames = []
alternateNames = []
myDict = {}

soup = BeautifulSoup(content)
all_span = soup.findAll("span")

for i in all_span:
    if i.has_attr('data-alternative-name'):
        emojiName = i.text
        emojiNames.append(i.text)
        alternateString = i['data-alternative-name']
        altNames = alternateString.split(", ")

        for name in altNames:
            myDict[name] = emojiName;

for i in emojiNames:
    myDict[i] = i

#for i in myDict:
#    print i, myDict[i]

print myDict['teeth']
print myDict['grimacing']
print myDict['mask']

#for i, j in enumerate(myDict):
#    print i,j
