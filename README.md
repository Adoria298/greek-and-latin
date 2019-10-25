# greek-and-latin

Github pages for Herodotus.
See [adoria298.github.io/greek-and-latin](https://adoria298.github.io/greek-and-latin) for rendered text.
All texts are stored in the docs folder, so analysis tools can be stored in the root folder.

## `analysis.py`

- requires [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/), which can be installed with `pip install beautifulsoup4`.
- counts words and their many forms.
- could be used to prioritize flashcards, etc.
- results of which will eventually be linked into the main text.

## `add_tags.py`

- also requires [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/), as above.
- used to add properly formed span tags to paragraphs of text.
- as with `analysis.py`, currently works on `docs/the_ethiopians.html` only.
- removes spaces between words when outputting, so doesn't rewrite `docs/the_ethiopians.html`, instead writes to `docs/the_ethiopians_ext.html`.
