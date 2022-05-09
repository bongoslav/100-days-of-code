# tutorial:
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name='a', class_="titlelink")
# get the news with the highest upvotes
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
highest_score_index = article_upvotes.index(max(article_upvotes))

print(article_texts[highest_score_index])
print(article_links[highest_score_index])



# playground:
# with open("X:\\Programming\\100DaysOfCode\\day-45-beautiful-soup\\website.html", encoding="utf8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'lxml')
# # print(soup.title.string)
# # print(soup.a)

# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)

# # for tag in all_anchor_tags:
# #     print(tag.getText())

# # heading = soup.find(name="h1", id="name")  # look for all h1 where id="name"
# # print(heading)

# # section_heading = soup.find(name="h3", class_="heading")  # look for all h3 where class="heading"
# # print(section_heading.get("class"))

# company_url = soup.select_one(selector="p a")  # looking for a inside p
# print(company_url)

# print(soup.select(".heading"))  # selecting the element with class of heading