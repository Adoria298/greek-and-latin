# external imports
from bs4 import BeautifulSoup, NavigableString

# stdlib imports
from pprint import pprint
from pathlib import Path
import sys

# open file - default is docs/the_ethiopians.html
path = Path(input("Please input the document you'd like to be opened: "))
if not path.exists() or not path.is_file() or not "htm" in path.suffix: # must be an existing HTML file.
    print("The file given does not exist. Using docs/the_ethiopians.html instead.")
    path = Path("docs/the_ethiopians.html")
print(f"Opening {path.name}")
## actual reading code
with path.open(mode="r", encoding="utf-8") as f:
	soup = BeautifulSoup(f.read(), "html.parser")

# function definitions
def get_title(string):
    """
    Finds the title for the string, by asking the user.
    Params:
        - string: a string-like object
    Returns a string for the title.
    """
    print("Text:", string)
    title = input("Please enter its title (press enter to ignore): \n ")
    return title

print(f"Reading {path.name}") # not true, but good enough
print("Press Ctrl+C to end the loop and save your work. Note work in the current paragraph will not be saved, so ensure that you are at the end of the paragraph.")

# main loop - try/except so the loop can be easily broken
try: 
    # add spans and titles to words without them
    for para in soup.find_all("p"):
        for child in para.children:
            if child.name == "span":
                if "title" in child.attrs:
                    print(f"'{child.string}' has a title!")
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
                    needs_span = input("Does this same text need a span tag [Y/N]? ").upper()
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
                    for new_span in new_spans[::-1]:
                        new_space = NavigableString(" ")
                        child.insert_after(new_space) # insert a space between spans
                        new_space.insert_after(new_span)
                    child.extract() # it's been replaced, it's not needed anymore
except KeyboardInterrupt:
    print("Breaking loop.")
finally:
    print("\nNew HTML for this file:\n")
    print(soup.prettify())

    # write code 
    while True:
        needs_writing = input("Should I write this to a file [Y/N]? ").upper()
        if needs_writing in ("Y", "N"):
            break
    if needs_writing == "Y":
        try:
            with path.open("w", encoding="utf-8") as f:
                f.write(str(soup))
        except Exception as e:
            print("File unsuccessfuly written! Sorry!")
            print(e)
        print("Succesfully written!") # if we haven't got any errors, it was successful.
    else:
        print("I won't write it then.")

    input("Press enter to exit. ")