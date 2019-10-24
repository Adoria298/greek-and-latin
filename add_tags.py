from bs4 import BeautifulSoup
from pprint import pprint

with open("docs/the_ethiopians.html", mode="r", encoding="utf-8") as f:
	soup = BeautifulSoup(f.read(), "html.parser")

def get_title(string):
    """
    Finds the title for the string, by asking the user.
    Params:
        - string: a string-like object
    Returns a string for the title.
    """
    print("Text:", string)
    while True:
        needs_title = input("Does this text need a title [Y/N]? ").upper()
        if needs_title in ("Y", "N"):
            break
    if needs_title == "Y":
        title = input("Please enter it's title: \n")
    else: # has to be N
        title = ""
    return title

# add spans and titles to words without them
for para in soup.find_all("p"):
    for child in para.children:
        if child.name == "span":
            if "title" in child.attrs:
                print(f"{child.string} has a title!")
            else:
                child["title"] = get_title(child.string)
        elif child.name == None:
            print(f"Text: {child.string}")
            while True:
                needs_splitting = input("Does this text need splitting first [Y/N]?").upper()
                if needs_splitting in ("Y", "N"):
                    break
            while True:
                needs_span = input("Does this text need a span tag [Y/N]? ").upper()
                if needs_span in ("Y", "N"):
                    break
            if needs_span == "Y":Y
                new_spans = []
                if needs_splitting == "Y":
                    for word in child.string.split(" "):
                        new_span = soup.new_tag("span")
                        new_span["title"] = get_title(word)
                        new_span.string = word
                        new_spans.append(new_span)
                for new_span in new_spans: child.insert_after(new_span)
        child.decompose() # it's been replaced, it's not needed anymore
