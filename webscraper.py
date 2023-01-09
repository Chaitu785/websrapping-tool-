import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')


# Get the title of the HTML page
title = soup.title

# Get all the paragraphs from the page
paras = soup.find_all('p')

anchors = soup.find_all('a')
all_links = set()
# Get all the links on the page:
for link in anchors:
    if(link.get('href') != '#'): 
        linkText = "https://codewithharry.com" +link.get('href')
        all_links.add(link)
        # print(linkText)

navbarSupportedContent = soup.find(id='navbarSupportedContent')


elem = soup.select('#loginModal')[0] 
print(elem)
