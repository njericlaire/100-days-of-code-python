from bs4 import BeautifulSoup
import requests

response=requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page=response.text

soup=BeautifulSoup(yc_web_page,"html.parser")
articles=soup.find_all(name='a', class_='storylink')
for article_tag in articles:
    print(article_tag.getText())
    article_link= article_tag.get('href')
    print(article_link)


article_upvote=[int(score.getText().split()[0]) for score in soup.find_all(name='span',class_='score')]
print(article_upvote)






















# with open("website.html") as file:
#     contents = file.read()
# soup=BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.prettify())
# all_anchor_tags=soup.find_all(name="a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
# heading=soup.find(name='h1',id='name')
#
# print(heading)
# contact_me=soup.select_one(selector='p a')#u can use any css selector including id and classes
# print(contact_me)