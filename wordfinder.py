"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Machine for finding random words in a dictionary
    
    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """

    def __init__(self, path):
        """read dictionary and reports x number of items read"""
        dict_file =open(path)
        self.words= self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def parse(self,dict_file):
        """Parse dict_file into list of words"""
        return [w.strip() for w in dict_file]
    
    def random(self):
        """Return random word"""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines and comments"""

    def parse(self,dict_file):
        """Parse dict_file to make list of words, skipping blanks and comments"""

        return[w.strip() for w in dict_file
            if w.strip() and not w.startswith('#')]