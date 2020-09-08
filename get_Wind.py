import requests
import sys
from time import sleep
#from bs4 import BeautifulSoup

def clearLastLine():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

def getHtml(webUrl):
    print('Accessing URL...')
    htmlContent = requests.get(webUrl)
    clearLastLine()
    if htmlContent.status_code == 200:
        print("URL reached successfully.")
        return htmlContent.text
    else:
        print('Error '+ str(htmlContent.status_code) +' ' + htmlContent.reason)
        return None


def saveHtml(webUrl, webPage):
    print('Saving web page ...')
    with open(webUrl.split('/')[-1]+'.html', 'w') as myPage:
        myPage.write(webPage)
    sleep(2)
    clearLastLine()
    print('Page Saved.')

url = 'http://www.meteo.nc/nouvelle-caledonie/observations/dernieres-24h'
saveHtml(url,getHtml(url))
