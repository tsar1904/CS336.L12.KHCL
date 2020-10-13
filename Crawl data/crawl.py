import requests
from bs4 import BeautifulSoup
import pandas as pd

allTitles = []
allBody = []
allCategory = []
allLinks = []
allDateTime = []

for i in range(1,22,1):
    url = "https://vnexpress.net/category/day?cateid=1001005&fromdate=1597338000&todate=1600448399&allcate=1001005&page=" + str(i)
    response = requests.get(url)
    post = BeautifulSoup(response.content, 'html.parser')

    pageTitle = post.findAll('h3',class_ = 'title-news')
    pageBody = post.findAll('p',class_ = 'description')
    pageCategory = post.findAll('p',class_ = 'meta-news')


    titles = [title.find('a').text.replace('\n','') for title in pageTitle]
    [allTitles.append(title) for title in titles]

    descript = [des.find('a').text for des in pageBody]
    [allBody.append(des) for des in descript]

    links = [link.find('a').attrs["href"] for link in pageTitle]
    # [allLinks.append(link) for link in links]
    for link in links:
        allLinks.append(link)

        subres = requests.get(link)
        subpost = BeautifulSoup(subres.content,'html.parser')

        pageDateTime = subpost.findAll('span',class_='date')

        dates = [date.text for date in pageDateTime]
        print(dates)
        [allDateTime.append(date) for date in dates]


    category = [cate.find('a').text for cate in pageCategory]
    [allCategory.append(cate) for cate in category]

    # for date in pageDateTime:
    #     if (date.has_attr('datetime')):
    #         allDateTime.append(date)


df = pd.DataFrame({'Title':allTitles,'Description':allBody,'Category':allCategory,'Datetime':allDateTime,'Link':allLinks})

df.to_csv('Crawl_30_days.csv')
