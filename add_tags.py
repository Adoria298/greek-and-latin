# Adds <span title=""> tags to a given HTML file.
from html.parser import HTMLParser
from pprint import pprint

class ParagraphProducer(HTMLParser):

    def __init__(self, convert_charrefs=True):
        super().__init__(convert_charrefs=convert_charrefs)
        self.in_p_tag = False

    def handle_starttag(self, tag, attrs):
        print("Encountered starting:", tag, "with the following attributes:")
        pprint(attrs)
        if tag == "p" and not self.in_p_tag:
            self.in_p_tag = True
        else:
           print("Not a paragraph!")
    
    def handle_endtag(self, tag):
        print("Encountered ending:", tag, "with the following attributes:")
        pprint(attrs)
        if tag == "p":
            self.in_p_tag = False

    def handle_data(self, data):
        print("Encountered data: ")
        if self.in_p_tag:
            yield dat

if __name__ == "__main__":
    file = open(input("What would you like to read? "), "r").read()
    pp = ParagraphProducer(True)
    pp.feed(file)

