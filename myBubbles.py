from linebot.models import *
from bs4 import BeautifulSoup
import requests
#####Doctor List and Link###############
DrLists=[]
DrLinks=[]
target_url='https://wwwv.tsgh.ndmctsgh.edu.tw/Doclist/194/30000/25075'
responses=requests.get(target_url)
soup=BeautifulSoup(responses.text,"html.parser")
myDivs=soup.find_all('div',{'class':'column column-block lg-txt'})
for myDiv in myDivs:
  myLink=myDiv.find('a')
  DrLists.append(str(myLink.contents[0]))
  DrLinks.append(f"https://wwwv.tsgh.ndmctsgh.edu.tw/{myLink.get('href')}")

#######OPD list and links#############
OPDLists=[]
OPDLinks=[]
target_url='https://wwwv.tsgh.ndmctsgh.edu.tw/unit/30000/28387'
responses=requests.get(target_url)
soup=BeautifulSoup(responses.text,"html.parser")
myDiv=soup.select_one('div.systems-information')
myList=myDiv.find_all('a')
for tag in myList:
  OPDLists.append(tag.contents[0])
  myLink=str(tag.get('href'))
  myLink=f"https://wwwv.tsgh.ndmctsgh.edu.tw/{myLink}"
  OPDLinks.append(myLink)

######News List and links#############
NewsLists=[]
NewsLinks=[]
target_url='https://wwwv.tsgh.ndmctsgh.edu.tw/news/194/30000/24181'
responses=requests.get(target_url)
soup=BeautifulSoup(responses.text,"html.parser")
myNews=soup.find_all('a',{'id':'clickElement'})
for i, news in enumerate(myNews):
  NewsLists.append(str(news.contents[0]).replace('\n','').replace('\r',' '))
  NewsLinks.append('https://wwwv.tsgh.ndmctsgh.edu.tw'+news.get('href'))

#######Fee list and links##########
FeeLists1=[]
FeeLinks1=[]
target_url='https://wwwv.tsgh.ndmctsgh.edu.tw/unit/30000/16048'
response=requests.get(target_url)
soup=BeautifulSoup(response.text, 'html.parser')
myDiv=soup.select_one('div.systems-information')
FeeLists=myDiv.find_all('a')
for i, tag in enumerate(FeeLists):
  FeeLists1.append(tag.contents[0].strip())
  FeeLinks1.append(tag.get('href'))

#####Fee Bubble for FlexSendMessage##########
def myBubble_Fee( * message):
  myContents_6=[]
  i=0
  for i in range(len(FeeLists1)):
    myContent=ButtonComponent(style='link',height='sm',action=URIAction(label=FeeLists1[i],uri=FeeLinks1[i]))
    myContents_6.append(myContent)
  myBubble_6=BubbleContainer(
      body=BoxComponent(
          layout='vertical',
          spacing='sm',
          contents=myContents_6
      )
  )
  return myBubble_6


###News Bubble for FlexSendMessage##########
def myBubble_News( * message):
  myContents_5=[]
  i=0
  for i in range(len(NewsLists)):
    myContent=ButtonComponent(style='link',height='sm',action=URIAction(label=NewsLists[i],uri=NewsLinks[i]))
    myContents_5.append(myContent)
  myBubble_5=BubbleContainer(
      body=BoxComponent(
          layout='vertical',
          spacing='sm',
          contents=myContents_5
      )
  )
  return myBubble_5

##OPD bubble for flexSendMessage###########
def myBubble_OPDs( * message):
  myContents_4=[]
  i=0
  for i in range(len(OPDLists)):
    myContent=ButtonComponent(style='link',height='sm',action=URIAction(label=OPDLists[i],uri=OPDLinks[i]))
    myContents_4.append(myContent)
  myBubble_4=BubbleContainer(
      body=BoxComponent(
          layout='vertical',
          spacing='sm',
          contents=myContents_4
      )
  )
  return myBubble_4

###Doctors bubble for flexSendMessage#############
def myBubble_doctors( * message):
  myContents_3=[]
  i=0
  for i in range(len(DrLists)):
    myContent=ButtonComponent(style='link',height='sm',action=URIAction(label=DrLists[i],uri=DrLinks[i]))
    myContents_3.append(myContent)
  myBubble_3=BubbleContainer(
      body=BoxComponent(
          layout='vertical',
          spacing='sm',
          contents=myContents_3
      )
  )
  return myBubble_3


def myBubble_greeting( * meesage):
  myList_2=['三總北投分院網站','三總北投分院臉書','24hr自殺防治專線']
  myLink_2=['https://beitou.tsgh.ndmctsgh.edu.tw/','https://zh-tw.facebook.com/pages/category/Hospital/三軍總醫院北投分院-204568046633204/','tel:+886-2-800-395-995']
  myContents_2=[]
  i=0
  for i in range(len(myList_2)):
    myContent=ButtonComponent(style='link',height='sm',action=URIAction(label=myList_2[i],uri=myLink_2[i]))
    myContents_2.append(myContent)
  myBubble_2=BubbleContainer(
      hero=ImageComponent(
          url='https://i.imgur.com/9KAkYf4.jpg',
          size='full',
          aspect_ratio='20:13',
          aspect_mode='cover',
          action=URIAction(uri='https://beitou.tsgh.ndmctsgh.edu.tw/',label='三總北投分院')
      ),
      body=BoxComponent(
          layout='vertical',
          spacing='sm',
          contents=myContents_2
      )
  )
  return myBubble_2