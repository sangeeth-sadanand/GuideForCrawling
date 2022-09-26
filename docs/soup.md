# BeautifulSoup

Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree.

## Installing Beautiful Soup

``` bash
pip install beautifulsoup4
```



## Parsers

|  Parser                | Remarks|
|---------------------- |---------------------------------------------------------------------|
|  lxml's HTML parser    | Very fast but has external C dependancy|
|  Python's html.parser  | Slower than lxml parser, no external dependancies|
|  html5lib              | Very slow, but very accurate and parse the html as the browser does|


## Making a soup

``` python
from bs4 import BeautifulSoup

with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

soup = BeautifulSoup("<html>a web page</html>", 'html.parser')
```

## Kinds of objects

There are four kinds of objects

|  Object                             |  Remarks  |
| --- | --- |
|  Tag                                 | A Tag object corresponds to an XML or HTML tag in the original document|
|  NavigableString                     | A string corresponds to a bit of text within a tag. Beautiful Soup uses the NavigableString class to |contain these bits of text
|  BeautifulSoup                       | The BeautifulSoup object represents the parsed document as a whole.|
|  Comments and other special strings  | The Comment object is just a special type of NavigableString|


## Navigating the tree

Here's the "Three sisters" HTML document again

``` python
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
```

### Navigating using tag names

The simplest way to navigate the parse tree is to say the name of the tag you want.

``` python
soup.head
# <head><title>The Dormouse's story</title></head>

soup.title
# <title>The Dormouse's story</title>
```

### .contents and .children

A tag's children are available in a list called .contents

``` python
head_tag = soup.head
head_tag
# <head><title>The Dormouse's story</title></head>

head_tag.contents
# [<title>The Dormouse's story</title>]

title_tag = head_tag.contents[0]
title_tag
# <title>The Dormouse's story</title>
title_tag.contents
# ['The Dormouse's story']

text = title_tag.contents[0]
text.contents
# AttributeError: 'NavigableString' object has no attribute 'contents'

for child in title_tag.children:
    print(child)
# The Dormouse's story
```

### .descendants

The .contents and .children attributes only consider a tag's direct children. The .descendants attribute lets you iterate over all of a tag's children, recursively

``` python
head_tag.contents
# [<title>The Dormouse's story</title>]

for child in head_tag.descendants:
    print(child)
# <title>The Dormouse's story</title>
# The Dormouse's story
len(list(soup.children))
# 1
len(list(soup.descendants))
# 26

```

### .string

If a tag has only one child, and that child is a NavigableString, the child is made available as .string

``` python
title_tag.string
# 'The Dormouse's story'
```

### .strings and stripped_strings

If there's more than one thing inside a tag, you can still look at just the strings These strings tend to have a lot of extra whitespace, which you can remove by using the .stripped_strings generator instead

``` python
for string in soup.strings:
    print(repr(string))
    '\n'
# "The Dormouse's story"
# '\n'
# '\n'
# "The Dormouse's story"
# '\n'
# 'Once upon a time there were three little sisters; and their names were\n'
# 'Elsie'
# ',\n'
# 'Lacie'
# ' and\n'
# 'Tillie'
# ';\nand they lived at the bottom of a well.'
# '\n'
# '...'
# '\n'

for string in soup.stripped_strings:
    print(repr(string))
# "The Dormouse's story"
# "The Dormouse's story"
# 'Once upon a time there were three little sisters; and their names were'
# 'Elsie'
# ','
# 'Lacie'
# 'and'
# 'Tillie'
# ';\n and they lived at the bottom of a well.'
# '...'
```

### .parent and .parents

You can access an element's parent with the .parent attribute. You can iterate over all of an element's parents with .parents.

``` python
title_tag = soup.title
title_tag
# <title>The Dormouse's story</title>
title_tag.parent
# <head><title>The Dormouse's story</title></head>

link = soup.a
link
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
for parent in link.parents:
    print(parent.name)
# p
# body
# html
# [document]
```

### .next_sibling and .previous_sibling

You can use .next_sibling and .previous_sibling to navigate between page elements that are on the same level of the parse tree

``` python
sibling_soup.b.next_sibling
# <c>text2</c>

sibling_soup.c.previous_sibling
# <b>text1</b>
```

### .next_siblings and .previous_siblings

You can iterate over a tag's siblings with .next_siblings or .previous_siblings

``` python
for sibling in soup.a.next_siblings:    
    print(repr(sibling))
    
# ',\n'# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# ' and\n'# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# '; and they lived at the bottom of a well.'for sibling in 

soup.find(id="link3").previous_siblings:    

print(repr(sibling))
# ' and\n'# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a># ',\n'# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a># 'Once upon a time there were three little sisters; and their names were\n'
```

### .next_element and .previous_element

The .next_element attribute of a string or tag points to whatever was parsed immediately afterwards The .previous_element attribute is the exact opposite of .next_element.

``` python
last_a_tag = soup.find("a", id="link3")
last_a_tag
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
last_a_tag.next_sibling
# ';\nand they lived at the bottom of a well.'


last_a_tag.previous_element
# ' and\n'
last_a_tag.previous_element.next_element
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
```

### .next_elements and .previous_elements

You can use these iterators to move forward or backward in the document as it was parsed

``` python
for element in last_a_tag.next_elements:
    print(repr(element))
# 'Tillie'
# ';\nand they lived at the bottom of a well.'
# '\n'
# <p class="story">...</p>
# '...'
# '\n'
```

### find and find_all

Both are used to search the elements in soup tree.

``` python
find_all(name, attrs, recursive, string, limit, **kwargs)
```

``` python
## Using tags strings
soup.find_all('b')
# [<b>The Dormouse's story</b>]

## Regular expressions
import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
# body
# b

## A List
soup.find_all(["a", "b"])
# [<b>The Dormouse's story</b>,
#  <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

## True
for tag in soup.find_all(True):
    print(tag.name)
# html
# head
# title
# body
# p
# b
# p
# a
# a
# a
# p


## A function - The function should return True if the argument matches, and False otherwise.
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
soup.find_all(has_class_but_no_id)
# [<p class="title"><b>The Dormouse's story</b></p>,
#  <p class="story">Once upon a time there were…bottom of a well.</p>,
#  <p class="story">...</p>]


## Using attributes
data_soup.find_all(attrs={"data-foo": "value"})
# [<div data-foo="value">foo!</div>]
```

### find_parents() and find_parent()

``` python
find_parents(name, attrs, string, limit, **kwargs)
find_parent(name, attrs, string, **kwargs)
```

### find_next_siblings() and find_next_sibling()

``` python
find_next_siblings(name, attrs, string, limit, **kwargs) 
find_next_sibling(name, attrs, string, **kwargs)
```

### find_previous_siblings() and find_previous_sibling()

``` python
find_previous_siblings(name, attrs, string, limit, **kwargs)
find_previous_sibling(name, attrs, string, **kwargs)
```

### find_all_next() and find_next()

``` python
find_all_next(name, attrs, string, limit, **kwargs)
find_next(name, attrs, string, **kwargs)
```

### find_all_previous() and find_previous()

``` python
find_all_previous(name, attrs, string, limit, **kwargs)
find_previous(name, attrs, string, **kwargs)
```

### CSS selectors

``` python
##  find tags
soup.select("title")
# [<title>The Dormouse's story</title>]
soup.select("p:nth-of-type(3)")
# [<p class="story">...</p>]

##Find tags beneath other tags
soup.select("body a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie"  id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
soup.select("html head title")
# [<title>The Dormouse's story</title>]

## Find tags directly beneath other tags
soup.select("head > title")
# [<title>The Dormouse's story</title>]

## Find the siblings of tags:
soup.select("#link1 ~ .sister")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie"  id="link3">Tillie</a>]
soup.select("#link1 + .sister")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

## Find tags by CSS class:
soup.select(".sister")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
soup.select("[class~=sister]")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

## Find tags by ID:
soup.select("#link1")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
soup.select("a#link2")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

## Find tags that match any selector from a list of selectors:
soup.select("#link1,#link2")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

## Test for the existence of an attribute:
soup.select('a[href]')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

## Find tags by attribute value:
soup.select('a[href="http://example.com/elsie"]')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
soup.select('a[href^="http://example.com/"]')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
soup.select('a[href$="tillie"]')
# [<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
soup.select('a[href*=".com/el"]')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

#There’s also a method called select_one(), which finds only the first tag that matches a selector:
soup.select_one(".sister")
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
```

## Modifying the tree

Beautiful Soup's main strength is in searching the parse tree, but you can also modify the tree and write your changes as a new HTML or XML document.

### Changing tag names and attributes

``` python
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b

tag.name = "blockquote"
tag['class'] = 'verybold'
tag['id'] = 1
tag
# <blockquote class="verybold" id="1">Extremely bold</blockquote>

del tag['class']
del tag['id']
tag
# <blockquote>Extremely bold</blockquote>

```

### .string

``` python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, 'html.parser')

tag = soup.a
tag.string = "New link text."
tag
# <a href="http://example.com/">New link text.</a>

```

### append()

``` python
soup = BeautifulSoup("<a>Foo</a>", 'html.parser')
soup.a.append("Bar")
soup
# <a>FooBar</a>soup.a.contents# ['Foo', 'Bar']
```

### extend()

``` python
soup = BeautifulSoup("<a>Soup</a>", 'html.parser')
soup.a.extend(["'s", " ", "on"])
soup
# <a>Soup's on</a>soup.a.contents# ['Soup', ''s', ' ', 'on']
```

### NavigableString() and .new_tag()

``` python
soup = BeautifulSoup("<b></b>", 'html.parser')
tag = soup.btag.append("Hello")
new_string = NavigableString(" there")
tag.append(new_string)

tag# <b>Hello there.</b>tag.contents# ['Hello', ' there']
```

### insert()

``` python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'

soup = BeautifulSoup(markup, 'html.parser')
tag = soup.atag.insert(1, "but did not endorse ")

tag

# <a href="http://example.com/">I linked to but did not endorse <i>example.com</i></a>tag.contents
# ['I linked to ', 'but did not endorse', <i>example.com</i>]
```

### insert_before() and insert_after()

``` python
soup = BeautifulSoup("<b>leave</b>", 'html.parser')

tag = soup.new_tag("i")

tag.string = "Don't"

soup.b.string.insert_before(tag)

soup.b
# <b><i>Don't</i>leave</b>div = soup.new_tag('div')div.string = 'ever'soup.b.i.insert_after(" you ", div)soup.b
# <b><i>Don't</i> you <div>ever</div> leave</b>soup.b.contents# [<i>Don't</i>, ' you', <div>ever</div>, 'leave']
```

### clear()

``` python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'

soup = BeautifulSoup(markup, 'html.parser')
tag = soup.atag.clear()
tag
#<a href="http://example.com/"></a>
```

### extract()

``` python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, 'html.parser')
a_tag = soup.a

i_tag = soup.i.extract()

a_tag
# <a href="http://example.com/">I linked to</a>

i_tag
# <i>example.com</i>

print(i_tag.parent)
# None
```

### decompose()

``` python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, 'html.parser')
a_tag = soup.a
i_tag = soup.i

i_tag.decompose()
a_tag
# <a href="http://example.com/">I linked to</a>
```

### replace_with()

``` python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, 'html.parser')
a_tag = soup.a

new_tag = soup.new_tag("b")
new_tag.string = "example.net"
a_tag.i.replace_with(new_tag)

a_tag
# <a href="http://example.com/">I linked to <b>example.net</b></a>
```

### wrap()

``` python
soup = BeautifulSoup("<p>I wish I was bold.</p>", 'html.parser')
soup.p.string.wrap(soup.new_tag("b"))
# <b>I wish I was bold.</b>

soup.p.wrap(soup.new_tag("div"))
# <div><p><b>I wish I was bold.</b></p></div>
```

### unwrap()

``` python
markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup, 'html.parser')
a_tag = soup.a

a_tag.i.unwrap()
a_tag
# <a href="http://example.com/">I linked to example.com</a>
```

### smooth()

``` python
soup = BeautifulSoup("<p>A one</p>", 'html.parser')
soup.p.append(", a two")

soup.p.contents
# ['A one', ', a two']

print(soup.p.encode())
# b'<p>A one, a two</p>'

print(soup.p.prettify())
# <p>
#  A one
#  , a two
# </p>
```