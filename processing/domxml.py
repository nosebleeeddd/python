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
    print("Author: {}".format(book.getElementsByTagName('author')[0].childNodes[0].data))
    print("title: {}".format(book.getElementsByTagName('title')[0].childNodes[0].data))
    print("genre: {}".format(book.getElementsByTagName('genre')[0].childNodes[0].data))
    print("price: {}".format(book.getElementsByTagName('price')[0].childNodes[0].data))
    print("published: {}".format(book.getElementsByTagName('publish_date')[0].childNodes[0].data))
    print("desc: {}".format(book.getElementsByTagName('description')[0].childNodes[0].data))

# list the changes we want to the XML, then write it to the file
books[2].getElementsByTagName('author')[0].childNodes[0].nodeValue = "John Doe"
books[0].setAttribute('id','777')
books[3].getElementsByTagName('price')[0].childNodes[0].nodeValue = "1000"
domtree.writexml(open('data.xml', 'w'))
