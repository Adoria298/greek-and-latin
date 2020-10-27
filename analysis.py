from bs4 import BeautifulSoup
from pprint import pprint

def count_words(soup: BeautifulSoup) -> dict:
	"""
	`<span title="<lemma> - <definition>"><word></span>`
	Creates a dictionary in the following format from a soup containing spans in the preceding format:
	<lemma>: 
		- count: int
		- definitions: list of <definition>
		- <word>: int (count of that particular word)

	Relies on accurate markup.
	"""
	# count words used
	words = {}
	# find all spans, count the definition and the declension of each word
	for span in soup.find_all("span"):
		title = span.get("title")
		if not title == "" or span.string == "":
			lemma, definition = title.split(" - ")
		else:
			lemma = ""
			definiton = ""
		if lemma in words:
			words[lemma]['count'] += 1
			if not definition in words[lemma]["definitions"]:
				words[lemma]["definitions"].append(definition)
			if span.string in words[lemma]:
				words[lemma][span.string] += 1
			else:
				words[lemma][span.string] = 1
		else:
			words[lemma] = {
				"count": 1
			}
			words[lemma][span.string] = 1
			words[lemma]["definitions"] = [definition]
	return words

if __name__ == "__main__":
	with open("docs/greek/set_texts/the_ethiopians.html", mode="r", encoding="utf-8") as f:
		soup = BeautifulSoup(f.read(), "html.parser")
		words = count_words(soup)
	pprint(words)
