from selenium import webdriver
import bs4
import requests
import re
import matplotlib.pyplot as plt
from selenium import webdriver
import threading, time
Barley = []
Canola = []
Corn = []
Flaxseed = []
Lentils = []
Oats = []
Rye = []
Peas = []
Soybeans = []
Wheat = []
xaxis = ["December 2018","March 2019","July 2019","December 2019","March 2020"]
types = ["Barley", "Canola", "Corn", "Flaxseed", "Lentils", "Oats", "Rye", "Peas", "Soybeans", "Wheat"]
types2 = [Barley, Canola, Corn, Flaxseed, Lentils, Oats, Rye, Peas, Soybeans, Wheat]
path = r'C:\Users\Parth\Downloads\Chromedriver'
driver = webdriver.Chrome(executable_path = path)

driver.get('https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=3210000701')
def getgrains(row, vari, labeler):
    y = row
    for x in range(2,7):
        xx= str(x)
        yy=str(y)
        driver.implicitly_wait(45)
        links = driver.find_elements_by_css_selector('#viewHtml > table > tbody > tr:nth-child('+yy+') > td:nth-child('+xx+')')

        temp = [link.text for link in links]
        temp = re.sub('\D',"", temp[0])
        temp = int(temp)
        vari.append(temp)
    #plt.plot(xaxis, vari, label = labeler)
    print(vari)
for  x in range(2,11):
    threadObj = threading.Thread(target=getgrains(x, types2[x-2], types[x-2]))
    threadObj.start()
    plt.plot(xaxis, types2[x-2], label = types[x-2])

driver.close()
plt.legend()
plt.show()
