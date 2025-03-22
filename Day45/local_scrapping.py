from bs4 import BeautifulSoup
# import lxml

with open("website.html", encoding="UTF-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser") # you can use lxml instead of html.parser
print(soup.title)           # <title>Angela's Personal Site</title>
print(soup.title.name)      # title
print(soup.title.string)    # Angela's Personal Site

print(soup)                 # raw code
print(soup.prettify())      # indentation

all_anchor_tags = soup.find_all(name="a")   # find all "a" tags in the document and return in list format
for tag in all_anchor_tags:
    print(tag.getText())    # print the text part of the tag
    print(tag.get("href"))  # access the attribute of the tag
    
heading = soup.find(name="h1", id="name")   # the first tag which has [tag name "h1" / tag id "name"]
print(heading)

section = soup.find(name="h3", class_="heading")    # find first tag which has [tag name "h3" / tag class "heading"]
print(section)

# Drilling HTML tag deeply. return first content met condition of css selector
company_url = soup.select_one("p a")    # find "a" tag inside "p" tag
my_name = soup.select_one("#name")      # find id "name"

# return whole contents
soup.select(".heading")                 # find all class "heading"