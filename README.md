# greek-and-latin

## Overview

Resources for Classical Greek and Latin, aimed at the OCR GCSE June 2020 exams, including the Greek set text from Farnell & Goff's adaptation of Herodotus, which do not exist anywhere I can find on the web, apart from here. Includes resources made by other people from elsewhere on the web.
See [adoria298.github.io/greek-and-latin](https://adoria298.github.io/greek-and-latin) for rendered text.
All texts are stored in the `docs` folder and analysis tools are stored in the root folder.

## Analysis Tools

These tools are command line tools designed to allow machines to analyse the text easily. They work based on span tags around each word in every paragraph, such as `<span title="βουλευομαι - to plan">ἐβουλευσατο</span>` - the title element is used so that the text is provided for the human reader. They require [Python 3.6+](https://www.python.org), so that f-strings can be used and [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/), which can be installed with `pip install beautifulsoup4`.

The ultimate aim is to make all the texts stored here compatible with the Perseus Digital Library, so that its myriad of wonderful tools can all be used.

### `analysis.py`

- counts words and their many forms.
- could be used to prioritize flashcards, etc.
- results of which will eventually be linked into the main text.
- only works with `docs/greek/set_texts/the_ethiopians.html`

### `add_tags.py`

- used to add properly formed span tags, as required by `analyis.py`, to paragraphs of text.
- can be used with any HTML file.
- writes directly to the original file.
