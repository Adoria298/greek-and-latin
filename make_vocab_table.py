from bs4 import BeautifulSoup, Tag

from pathlib import Path

def get_vocab_items(soup):
    "Takes in a BeautifulSoup and returns a dictionary of word (str): definition (str)"
    vocab_dict = {}
    for span in soup.find_all("span"):
        word, definition = span.get("title").split(" - ")
        vocab_dict[word] = definition
    return vocab_dict

def make_table_from_dict(dicti):
    """
    Takes in a dictionary of str:str (like one returned by get_vocab_items and returns an HTML table.
    The table returned is a tag object.
    """
    table = "<table>"
    for word in dicti.keys():
        table += "<tr>"
        table += "<td>" + word + "</td>"
        table += "<td>" + dicti[word] + "</td>"
        table += "</tr>"
    table += "</table>"
    return BeautifulSoup(table, "html.parser")


if __name__ == "__main__":
    src_path = Path(input("Please input the document you'd like to read. "))
    with src_path.open(mode='r', encoding='utf-8') as src: # trusting the user
        srcy_soup = BeautifulSoup(src.read(), "html.parser") # scry_soup: as in a soup that is saucy

    vocab = get_vocab_items(srcy_soup)
    print("Got the vocab. Let's go!")

    make_table_from_dict(vocab)

#    out_path = Path(input("Where do you want to put the final table? "))
 #   with out_path.open(mode='r', encoding='utf-8') as out: # if we shouldn't trust the user the program crashes
  #      out_soup = BeautifulSoup(out.read(), "html.parser")