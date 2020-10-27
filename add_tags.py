# external imports
from bs4 import BeautifulSoup, NavigableString

# stdlib imports
from pprint import pprint
from pathlib import Path
import sys

class Tagifier:
    def __init__(self, path=""):
        self.path = self.get_path(path)
        self.soup = self.get_soup()
        try:
            self.add_tags()
        except Exception as e:
            print("Error! Error:", e)
        finally:
            self.save()

    def is_valid_path(self, path: str) -> bool:
        try:
            test_Path = Path(path)
        except:
            return False
        if test_Path.exists() and test_Path.is_file() and "htm" in test_Path.suffix:
            return True
        else:
            return False

    def get_path(self, path: str = "") -> Path:
        """
        Validates the path provided. If invalid, calls input to get a new path.
        If that is invalid, uses docs/greek/set_texts/the_ethiopians.html.
        In all cases, makes self.path a Path object which points to an existing HTML file.
        """
        if path and self.is_valid_path(path):
            return Path(path)
        path = input("Please input the document you'd like to add tags to: ")
        if not self.is_valid_path(path):
            path = "docs/greek/set_texts/the_ethiopians.html"
        return Path(path)
        
    def get_soup(self) -> BeautifulSoup:
        """
        Makes a BeautifulSoup out of self.path.
        Returns the soup.
        """
        # actual reading code
        print(f"Reading {self.path.name}") # to give an impression of progress
        with self.path.open(mode="r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
        return soup

    def get_title(self, string: str) -> str:
        """
        Finds the title for the string, by asking the user.
        Params:
            - string: a string-like object
        Returns a string for the title.
        """
        print("Text:", string)
        lemma = input("Please enter the \"dictionary form\" of this word (press enter to ignore): \n ")
        defin = input("Please enter the definition of this word (press enter to ignore): \n")
        return lemma + " - " + defin

    def y_or_n_input(self, prompt: str) -> str:
        """
        Calls input(prompt) until the response is Y or N.
        Returns Y or N.
        """
        ans = ""
        while not ans in ("Y", "N"):
            ans = input(prompt).upper()
        return ans

    def add_tags(self):
        print("Instructions:")
        print("Press Ctrl+C to end the loop and save your work. Note work in the current paragraph will not be saved, so ensure that you are at the end of the paragraph.")

        # main loop - try/except so the loop can be easily broken
        try: 
            # add spans and titles to words without them
            for para in self.soup.find_all("p"):
                for child in para.children:
                    if child.name == "span":
                        if "title" in child.attrs:
                            print(f"'{child.string}' has a title!")
                        else:
                            child["title"] = self.get_title(child.string)
                    elif child.name == None:
                        print(f"Text: {child.string}")
                        if child.string in (" ", ". ", ", ", "\n", "\t", ""): # avoid punctuation or whitespace
                            print("I don't think this needs splitting or a span tag!")
                            continue
                        needs_splitting = self.y_or_n_input("Does this text need splitting first [Y/N]? ")
                        needs_span = self.y_or_n_input("Does this same text need a span tag [Y/N]? ")
                        if needs_span == "Y":
                            new_spans = []
                            if needs_splitting == "Y":
                                for word in child.string.split(" "):
                                    new_span = self.soup.new_tag("span")
                                    new_span["title"] = self.get_title(word)
                                    new_span.string = word
                                    new_spans.append(new_span)
                            for new_span in new_spans[::-1]:
                                new_space = NavigableString(" ")
                                child.insert_after(new_space) # insert a space between spans
                                new_space.insert_after(new_span)
                            child.extract() # it's been replaced, it's not needed anymore
        except KeyboardInterrupt:
            print("Breaking loop.")

    def save(self):
        print("\nNew HTML for this file:\n")
        print(self.soup.prettify())

        # write code 
        needs_writing = self.y_or_n_input("Should I write this to a file [Y/N]? ")
        if needs_writing == "Y":
            try:
                with self.path.open("w", encoding="utf-8") as f:
                    f.write(str(self.soup))
                print("Succesfully written!") # file closed with no errors, so it was successful.
            except Exception as e:
                print("File unsuccessfuly written! Sorry!")
                print("Error:", e)
        else:
            print("I won't write it then.")

        input("Press enter to exit. ")

if __name__ == "__main__":
    t = Tagifier()