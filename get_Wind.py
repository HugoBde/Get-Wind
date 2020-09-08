import requests                 #Importing all necessary libraries
import os
from time import sleep
from bs4 import BeautifulSoup

def getHtml(webUrl):            #Download the html code of a page hosted at webUrl
    htmlContent = requests.get(webUrl)
    if htmlContent.status_code == 200:  #If the GET request is successful, page is downloaded
        return htmlContent.text
    else:                               #Otherwise the error message is returned to the user
        print('Error '+ str(htmlContent.status_code) +' ' + htmlContent.reason)
        return None


def saveHtml(webUrl):           #The html code is then stored into a file in the program directory
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
        with open(htmlFile) as myFile:
            mySoup = BeautifulSoup(myFile, 'lxml')
            for cell in mySoup.td:
                if 'obs' in cell['class']:
                    print (cell.get_text())
            
        #os.remove(htmlFile)

#input('Continue ...')