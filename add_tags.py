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
    title = input("Please enter its title (press enter to ignore): \n")
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
            if child.string in (" ", ". ", ", "): # avoid punctuation or spaces
                print("I don't think this needs splitting or a span tag!")
                continue
            while True:
                needs_splitting = input("Does this text need splitting first [Y/N]? ").upper()
                if needs_splitting in ("Y", "N"):
                    break
            while True:
                needs_span = input("Does this text need a span tag [Y/N]? ").upper()
                if needs_span in ("Y", "N"):
                    break
            if needs_span == "Y":
                new_spans = []
                if needs_splitting == "Y":
                    for word in child.string.split(" "):
                        new_span = soup.new_tag("span")
                        new_span["title"] = get_title(word)
                        new_span.string = word
                        new_spans.append(new_span)
                for new_span in new_spans[::-1]: child.insert_after(new_span)
                child.extract() # it's been replaced, it's not needed anymore

print(soup.prettify())

# write code 
while True:
    needs_writing = input("Should I write this to a file [Y/N]? ").upper()
    if needs_writing in ("Y", "N"):
        break
if needs_writing == "Y":
    with open("docs/the_ethiopians_ext.html", "w", encoding="utf-8") as f:
        f.write(str(soup))
    print("Succesfully written!") # if we haven't got any errors, it was successful.
else:
    print("I won't write it then.")

input("Press enter to exit. ")