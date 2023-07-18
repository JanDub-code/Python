import requests
from bs4 import BeautifulSoup

url = 'https://www.seznam.cz/'

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

titles = soup.select('.link')  # Vyhledání elementů s třídou "article-title"
názvy = soup.select('.article__text-box')

#for title in titles:
#    print(title.text)

print("####################################")

for název in názvy:
    print(název.text)

print("####################################")