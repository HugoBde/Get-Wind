import requests
import sys
import os
from time import sleep
#from bs4 import BeautifulSoup

def clearLastLine():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

def getHtml(webUrl):
    print('Accessing ' + webUrl + '...')
    htmlContent = requests.get(webUrl)
    #clearLastLine()
    if htmlContent.status_code == 200:
        print("URL reached successfully.")
        return htmlContent.text
    else:
        print('Error '+ str(htmlContent.status_code) +' ' + htmlContent.reason)
        return None


def saveHtml(webUrl, webPage):
    print('Saving web page ...')
    with open('Saved_Pages/'+webUrl.split('/')[-1]+'.html', 'w') as myPage:
        myPage.write(webPage)
    #clearLastLine()
    print('Page Saved.')


if not os.path.exists('Saved_Pages/'):
    os.mkdir('Saved_Pages/')
urlList = open('url_List.txt' , 'r')
for url in urlList:
    url = url.replace("\n","")
    saveHtml(url,getHtml(url))
