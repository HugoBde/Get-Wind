import requests
import os
from time import sleep
#from bs4 import BeautifulSoup

def getHtml(webUrl):
    htmlContent = requests.get(webUrl)
    if htmlContent.status_code == 200:
        return htmlContent.text
    else:
        print('Error '+ str(htmlContent.status_code) +' ' + htmlContent.reason)
        return None


def saveHtml(webUrl):
    print('Downloading ' + webUrl + ' ...')
    filePath = webUrl.split('/')[-1]+'.html'
    with open(filePath, 'w') as myPage:
        try:
            myPage.write(getHtml(webUrl))
            print('Page Downloaded.')
        except:
            print(webUrl + ' was not downloaded.')
    

with open('url_List.txt' , 'r') as urlList:
    for url in urlList:
        url = url.replace("\n","")
        saveHtml(url)
print('Content Downloaded.')

for htmlFile in os.listdir():
    if htmlFile.split('.')[-1] == 'html':
        os.remove(htmlFile)
#input('Continue ...')