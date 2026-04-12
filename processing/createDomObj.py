# DOM module views the xml file as
# a tree, every element is a branch
# in that tree.

# Also parses cleaner than SAX
#as we dont need to create a buffer to
#fix formatting issues.

# we can also manipulate the XML file
#unlike SAX

import xml.dom.minidom

# parsed xml file and loads tree in RAM
domtree = xml.dom.minidom.parse('data.xml')

# gets the root of the DOM tree, element containing objects/attributes
catalog = domtree.documentElement

# gets book tag in element catalog
books = catalog.getElementsByTagName('book')

# loop thru each tag/subnode and if it has an id we print it
for book in books:
    print("\n-----Book-----")
    if book.hasAttribute('id'):
        print("ID: {}".format(book.getAttribute('id')))

    # select first element found in collection,access first child node then data
    print("author: {}".format(book.getElementsByTagName('author')[0].childNodes[0].data))
    print("title: {}".format(book.getElementsByTagName('title')[0].childNodes[0].data))
    print("genre: {}".format(book.getElementsByTagName('genre')[0].childNodes[0].data))
    print("price: {}".format(book.getElementsByTagName('price')[0].childNodes[0].data))
    print("published: {}".format(book.getElementsByTagName('publish_date')[0].childNodes[0].data))
    print("desc: {}".format(book.getElementsByTagName('description')[0].childNodes[0].data))

# create new object, append then write it to the XML file

newbook = domtree.createElement('book')
newbook.setAttribute('id', '2000')

author = domtree.createElement('author')
author.appendChild(domtree.createTextNode('Paul Miller'))

title = domtree.createElement('title')
title.appendChild(domtree.createTextNode('Best book'))

genre = domtree.createElement('genre')
genre.appendChild(domtree.createTextNode('Horror'))

price = domtree.createElement('price')
price.appendChild(domtree.createTextNode('3000'))

published = domtree.createElement('publish_date')
published.appendChild(domtree.createTextNode('2001-09-10'))

description = domtree.createElement('description')
description.appendChild(domtree.createTextNode('The day before the great fake'))

newbook.appendChild(author)
newbook.appendChild(title)
newbook.appendChild(genre)
newbook.appendChild(price)
newbook.appendChild(published)
newbook.appendChild(description)

catalog.appendChild(newbook)

domtree.writexml(open('data.xml', 'w'))
