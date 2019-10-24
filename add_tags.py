from bs4 import BeautifulSoup
from pprint import pprint

# add spans and titles to words without them
for para in soup.find_all("p"):
	for child in para.children:
		if child.name == "span":
			if "title" in child.attrs:
				print(f"{child.string} has a title!")
			else:
				child["title"] = get_title(child)
		elif child.name == None:
			print(f"Text: {child.string}")
			while True:
				needs_splitting = input("Does this text need splitting first [Y/N]?")
				if needs_splitting not in ("Y", "N"):
					break
			while True:
				needs_span = input("Does this text need a span tag [Y/N]? ").upper()
				if needs_span not in ("Y", "N"):
					break
			if needs_span == "Y":
				if needs_splitting == "Y":
					new_spans = []
					for word in child.string.split(" "):
						new_span = soup.new_tag("span")
						new_span["title"] = get_title(word)
						new_span.string = word
						new_spans.append(new_span)
				child.replace_with