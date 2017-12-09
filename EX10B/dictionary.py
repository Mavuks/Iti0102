"""Simple dictionary."""
import string


class Dictionary:
    """fasdfsdf."""

    def __init__(self, initial_data):
        """fdsfdsf."""
        self.word_dict = {}
        self.verb = []
        self.noun = []
        self.adje = []


        list_of_words = initial_data.split("\n")

        for line in list_of_words:

            if len(line.split(" - ", 1)) == 2:
                word, definition = line.split(" - ", 1)
            else:
                continue

            if len(word) < 4:
                continue

            wordK = word[0] == "(" and word[2] == ")" and word[1] in "anv" and len(word[3:]) > 0
            wordK2 = all([char not in word[3:].lower() for char in "0123456789!\"#$%&'()*+,./:;<=>?@[\\]^_`{|}~"])
            wordK3 = len(word) - 1 !=word.find("-") == word.rfind("-") != 3

            wordK4 = len(definition) > 0 and any([char in string.ascii_letters for char in definition])

            if wordK and wordK2 and wordK3 and wordK4:
                if word[3:].lower() in self.word_dict:
                    self.word_dict[word[3:].lower()].append(definition)
                else:
                    self.word_dict[word[3:].lower()] = [definition]

                if word[1] == "n" and word[3:].lower() not in self.noun:
                    self.noun.append(word[3:].lower())
                if word[1] == "a" and word[3:].lower() not in self.adje:
                    self.adje.append(word[3:].lower())
                if word[1] == "v" and word[3:].lower() not in self.verb:
                    self.verb.append(word[3:].lower())


    def get_definitions(self, word):
        """gert."""


    def is_word_noun(self, word):
        """Is a word noun."""


    def is_word_verb(self, word):
        """Is a word verb."""


    def is_word_adjective(self, word):
        """Is a word adjective."""


    def get_all_nouns(self):
        """get all nouns."""


    def get_all_verbs(self):
        """Get all verbs."""


    def get_all_adjectives(self):
        """Get all adjectives."""


    def search(self, subword, min_len, max_len):
        """search."""

