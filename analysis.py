from bs4 import BeautifulSoup
from pprint import pprint

with open("docs/the_ethiopians.html", mode="r", encoding="utf-8") as f:
	soup = BeautifulSoup(f.read(), "html.parser")

# count words used
words = {}
# find all spans, count the definition and the declension of each word
for span in soup.find_all("span"):
	title = span.get("title")
	if title in words:
		words[title]['count'] += 1
		if span.string in words[title]:
			words[title][span.string] += 1
		else:
			words[title][span.string] = 1
	else:
		words[title] = {
			"count": 1
		}
		words[title][span.string] = 1
		
pprint(words)
