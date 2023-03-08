from bs4 import BeautifulSoup
import requests

page = int(input("Enter page number: "))
url = "https://news.ycombinator.com/" + f"?p={page}"
http_text = requests.get(url)

soup = BeautifulSoup(http_text.content, 'lxml')

headline_text = soup.find_all('tr', class_="athing")
detail_block = soup.find_all("td", class_="subtext")


def get_headline(i):
    headline = i.find("span", class_="titleline").a.text
    return headline


def get_link(i):
    link = i.find("span", class_="titleline").a["href"]
    if "https" not in link:
        return "https://news.ycombinator.com/" + link
    else:
        return link


def get_score(i):
    score = i.find("span", class_="score")
    if score is None:
        return 0
    else:
        return score.text.split(" ")[0]


headline_list = []
link_list = []
score_list = []

for j in headline_text:
    headline_list.append(get_headline(j))
    link_list.append(get_link(j))


for n, j in enumerate(detail_block):
    if int(get_score(j)) > 100:
        print(f"Headline: {headline_list[n]}\nScore: {get_score(j)}\nLink: {link_list[n]}")
