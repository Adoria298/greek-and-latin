# Texts

Please do expand the amount of texts! Please do correct errors whereever they are found! Below is the process of adding texts - NB that steps 4 & 5 can be replaced by the use of `add_tags.py`:

1. Open the HTML file in the text editor of your choice (on github.com, I recommend using soft wrap word wrapping).
2. Type up, with correct breathings, the text from Farnell & Goff. Every new paragraph, end the last one with the text `</p>`, create a new line, the create the new one with the text `<p>`.
3. Once typed up, proof read the text, then commit it, mentioning which lines you have typed, and this issue (typing `issue #1` in the commit message works.
4. At every word, you nned to add a `<span>` tag in front. This `<span>` tag should have a `title` equal to the dictionary definition, with a space, dash, space between the Greek and the English. This serves two functions:
    - annotating the word with what to expect in a dictionary for the reader;
    -  showing the computer what the Greek word is, so it can analyse the text more easily.
5. Then, once you have added the definition, go to the end of the word and add `</span>` before the space and the next word. If your word was `ἐβουλευσατο`, it should now look like this: `<span title="βουλευομαι - to plan">ἐβουλευσατο</span>`.
6. Once you finish annotating a paragraph, ensuring you annotate every word correctly, commit it. Again, mention which lines and this issue in your commit message.
