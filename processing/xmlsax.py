#Simple Api for Xml module(SAX)

# SAX can only read/process data in
#a script, but cannot change data

import xml.sax


# handler works with file
# parser translates the file

# we inherit sax content handler for our class
class CatalogHandler(xml.sax.ContentHandler):

    # start method gets called when handler processes an elements
    # name is element tag, attrs is object with elems attributes
    # we accumulate text in buffer to strip later fixing format
    def startElement(self, name, attrs):
        self.current = name
        self.buffer = ""
        if self.current == "book":
            print("\n-----Book-----")
            print("ID: {}".format(attrs['id']))             #access dict key ID

    # send content of individual tags author, title, genre, to buffer
    def characters(self, content):
        if self.current:
            self.buffer += content

    # when you get to end of the element you want to print the data
    # and we strip the buffer holding content so no trailing whitespace
    def endElement(self, name):
        if name == "author":
            print("Author:", self.buffer.strip())
        elif name == "title":
            print("Title:", self.buffer.strip())
        elif name == "genre":
            print("Genre:", self.buffer.strip())
        elif name == "price":
            print("Price:", self.buffer.strip())
        elif name == "publish_date":
            print("Published:", self.buffer.strip())
        elif name == "description":
            print("Description:", self.buffer.strip())

        # clears the element so it does repete description
        self.current = None



handler = CatalogHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('data.xml')

