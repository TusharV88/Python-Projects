# Learning Web Scraping

import requests
from bs4 import BeautifulSoup


url = "https://codewithharry.com"

# Step 1 : Get the HTML

webContent = requests.get(url)

# print(webContent) # show response

htmlContent = webContent.content

# print(htmlContent) # show content of website

# Step 2 : Parse the HTML

soup = BeautifulSoup(htmlContent, 'html.parser')


# print(soup.prettify)  # Show data in readable format


# Step 3 : HTML Tree Traversal

title = soup.title

# print("\n",title.string)  # Show the Title


# print(soup.find('p'))  # Show the p tag ,para

# Show all the p tag in html
# paras = soup.find_all('p')
# print(paras)
# for i in paras:
#     print(i)

# Show all the Anchors
# anchors = soup.find_all('a')
# print(anchors)


# Commonly used types of objects:
# print(type(title)) # 1. Tag
# print(type(title.string)) # 2. NavigableString
# print(type(soup)) # 3. BeautifulSoup
# # 4. Comment
# markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup)
# print("\n\n",type(soup2.p.string),"\n\n")


# Get classes of any element in the HTML page
# print(soup.find('p')['class'])


# find all the elements with class lead
# print(soup.find_all("p", class_="lead"))


# Get the text from the tags/soup
# print(soup.find('p').get_text())
# print(soup.get_text())


# Get all the anchor tags from the page
anchors = soup.find_all('a')
all_links = set()


# Get all the links on the page:
for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://codewithharry.com" + link.get('href')
        all_links.add(link)
        # print(linkText)

# exit()


navbarSupportedContent = soup.find(id='navbarSupportedContent')

# .contents - A tag's children are available as a list, slow
# .children - A tag's children are available as a generator, fast
# for elem in navbarSupportedContent.contents:
# print(elem)


# for item in navbarSupportedContent.strings:
#     print(item)


# for item in navbarSupportedContent.stripped_strings:
#     print(item)


# print(navbarSupportedContent.parent)


# for item in navbarSupportedContent.parents:
#     print(item.name)


# print(navbarSupportedContent.next_sibling.next_sibling) # Count Spaces as sibling

# print(navbarSupportedContent.previous_sibling.previous_sibling)


# elem = soup.select('.modal-footer')
# print(elem)


# elem = soup.select('#loginModal')[0]
# print(elem)
