import requests                 #Importing all necessary libraries
import os
import json
from time import sleep
from bs4 import BeautifulSoup

def getSettings (settingsFile):
    urls = []
    timeSettings = []
    windSpeedSetings = []
    for webSite in json.load(settingsFile):
        urls.append(webSite['url'])
        timeSettings.append(webSite['time'])
        windSpeedSetings.append()

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


def fetchData(mySoup , tag , classAttr = None): #Fetches data from the given files, by looking for the speicifed tag and optional class attributes
    data = []
    if classAttr == None:
        for elem in mySoup.find_all(tag):
            data.append(elem.get_text())
    else:
        for elem in mySoup.find_all(tag,classAttr):
            data.append(elem.get_text())
    return data

def displayData(times, speeds):                 #Display fetched data into a more readable format
    try:
        print('|\t TIME \t\t|\t AVERAGE \t|\t MAX \t\t|')
        for i in range (len(times)):
            print('|\t' + times[i] + '\t|\t' + speeds[2*i] + '\t|\t' + speeds[2*i+1] + '\t|\t')
    
    except IndexError:
        print('A formatting error has occured. \n RAW DATA: \n')
        for i in range (0, len(speeds), 2):
            print(speeds[i] + '\t' + speeds[i+1])


with open('settings.json' , 'r') as settingsFile:
    settings = json.load(settingsFile)

for webPage in settings:
    url = webPage['url']
    timeSettings = webPage['time']
    windSpeedSettings = webPage['wind']
    saveHtml(url)
    for htmlFile in os.listdir():
        if htmlFile.split('.')[-1] == 'html':
            with open(htmlFile) as myFile:
                mySoup = BeautifulSoup(myFile , 'lxml')
                timeData = fetchData(mySoup , timeSettings['tag'] , timeSettings['class'])
                windData = fetchData(mySoup , windSpeedSettings['tag'] , windSpeedSettings['class'])
                displayData(timeData , windData)
            os.remove(htmlFile)

input('Continue ...')