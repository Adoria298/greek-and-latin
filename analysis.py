from bs4 import BeautifulSoup
from pprint import pprint

with open("docs/greek/set_texts/the_ethiopians.html", mode="r", encoding="utf-8") as f:
	soup = BeautifulSoup(f.read(), "html.parser")

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
		
pprint(words)
