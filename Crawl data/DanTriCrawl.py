import requests
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame(columns = ['Title','Description','DateTime','Link'])
allLinks = []
allTitles = []
allBody = []
allDateTime = []

try:
    for i in range(1,31,1):
        url = "https://dantri.com.vn/xa-hoi/" + str(i) + "-8-2020.htm"
        response = requests.get(url)
        post = BeautifulSoup(response.content, 'html.parser')

        pageTitle = post.findAll('h3',class_ = 'news-item__title')
        pageBody = post.findAll('a',class_ = 'news-item__sapo')

        for title in pageTitle:
            query = title.find('a').get('data-utm')
            if (query[:19] == "Cate_XaHoi|MainList"):
                allTitles.append(title.find('a').text.replace('\n',''))
                allLinks.append(title.find('a').attrs["href"])

        for des in pageBody:
            query = des.get('data-utm')
            if (query[:19] == "Cate_XaHoi|MainList"):
                allBody.append(des.text)

        print('Completed ' + str(i) + ' day!')

    for link in allLinks:
        subres = requests.get('https://dantri.com.vn/' + link)
        subpost = BeautifulSoup(subres.content,'html.parser')

        pageDateTime = subpost.findAll('span',class_='dt-news__time')
        print(pageDateTime)
        if pageDateTime != []:
            allDateTime.append(pageDateTime[0].text)
        else:
            allDateTime.append(None)
except:
    pass


print(len(allBody))
print(len(allLinks))
print(len(allTitles))
print(len(allDateTime))

df = pd.DataFrame({'Title':allTitles,'Description':allBody,'Datetime':allDateTime,'Link':allLinks})
df.to_csv('DanTri_thang_8.csv')
