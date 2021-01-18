from bs4 import BeautifulSoup

from pathlib import Path

src_path = Path(input("Please input the document you'd like to read. "))
with src_path.open(mode='r', encoding='utf-8') as src: # trusting the user
    srcy_soup = BeautifulSoup(src.read(), "html.parser")

def get_vocab_items(soup):
    "Takes in a BeautifulSoup and returns a dictionary of word (str): definition (str)"
    vocab_dict = {}
    for span in soup.find_all("span"):
        word, definition = span.get("title").split(" - ")
        vocab_dict[word] = definition
    return vocab_dict