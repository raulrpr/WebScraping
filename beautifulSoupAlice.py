from bs4 import BeautifulSoup

with open("Alice.html", "r") as file:
    alice_html = file.read()

soup = BeautifulSoup(alice_html, 'html.parser')

print(soup.title)
        # <title>The Dormouse's story</title>

print(soup.title.parent.name)
        # u'head'

print(soup.p)
        # <p class="title"><b>The Dormouse's story</b></p>

print(soup.p['class'])
        # u'title'

print(soup.a)
        # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

# Find all <a> elements...
elems_a = soup.find_all('a')
print(elems_a)
        # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
        #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
        #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# Find the element with id = "link3"...
elem_link3 = soup.find(id="link3")
print(elem_link3)
        # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>


# Extracting all the URLs found within a page’s <a> tags:
for link in soup.find_all('a'):
    print(link.get('href'))
        # http://example.com/elsie
        # http://example.com/lacie
        # http://example.com/tillie

