from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yx_res = response.text
soup = BeautifulSoup(yx_res, "html.parser")

titles = soup.find_all(name="span", class_="titleline")
links = []
for title in titles:
    link = title.find(name="a").get("href")
    if link:
        links.append(link)

print(links)

# print(titles)

# import lxml

# with open("Day45 - Web Scraping/website.html", "r") as file:
#     contents = file.read()

# # print(contents)

# soup = BeautifulSoup(contents, "html.parser")
# # yg ini cuman nyari first thing
# print(soup.a)

# # yg ini nyaro whole thing
# print(soup.find_all(name="a"))

# for tag in soup.find_all(name="a"):
#     print(tag.getText())
#     print(tag.get('href'))

# print(soup.find(name="h1", id="name").getText())

# print(soup.find(name="h3", class_="heading").getText())

# company_url = soup.select_one(selector="p a")
# print(company_url)

# all_urls = soup.select('.heading')
# for all in all_urls:
#     print(all.getText())
# print(all_urls)