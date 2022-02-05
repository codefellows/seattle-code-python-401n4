import requests
from bs4 import BeautifulSoup

URL = 'https://testing-www.codefellows.org/courses/code-400/'
page = requests.get(URL)

# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

results = soup.find(class_="course-details")
# print(results.prettify())

titles = results.find_all('h3')
# print(titles)

# for title in titles:
#     print(title.text)

anchors = results('a')
# print(anchors)

links = [anchor['href'] for anchor in anchors]

# for link in links:
#     print(link)

python_link = links[1]
# print(python_link)

new_url = 'https://testing-www.codefellows.org' + python_link
# print(new_url)

link_content = requests.get(new_url)
# print(link_content.content)
link_soup = BeautifulSoup(link_content.content, 'html.parser')

# print(link_soup)

article = link_soup('article')[1]

# print(article)

list_items = article.select(' ul li ul li ')
# print(list_items[5])

for li in list_items:
    print(li.text)
