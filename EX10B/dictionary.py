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



if __name__ == '__main__':
    small_dict_data = "\n".join(["(a)beautiful - very pleasing or satisfying",
                                 "(a)wise - possessed of or characterized by scholarly knowledge or learning",
                                 "(a)kind -",
                                 "(a)Warm - conserving or maintaining warmth or heat",
                                 "(v)Claim - to assert or maintain as a fact",
                                 "(n)ph one - a portable electronic telephone device",
                                 "(a)wise - having the power to judge what is true or right",
                                 "[n]place - a particular portion of space, whether of definite or indefinite exten",
                                 "(a)well-known - clearly or fully known",
                                 "(v)-create - to cause to come into being",
                                 "(n)law - the principles and regulations established in a community by some authority",
                                 "(n)injury - harm or damage that is done or sustained",
                                 "",
                                 "choice - an act or instance of selection",
                                 "(n)fire - a burning mass of material, as on a hearth or in a furnace",
                                 "(b)consume - to destroy or expend by use",
                                 "(v)consume - to eat or drink up; devour",
                                 "(v)fire - to expose to the action of fire; subject to heat",
                                 "(v)fire - to inspire"])

    small_dictionary = Dictionary(small_dict_data)

    assert len(small_dictionary.get_definitions("kind")) == 0
    assert len(small_dictionary.get_definitions("phone")) == 0
    assert len(small_dictionary.get_definitions("ph one")) == 0
    assert len(small_dictionary.get_definitions("choice")) == 0
    assert len(small_dictionary.get_definitions("-create")) == 0
    assert len(small_dictionary.get_definitions("create")) == 0
    assert len(small_dictionary.get_definitions("beautiful")) == 1
    assert len(small_dictionary.get_definitions("fire")) == 3
    assert len(small_dictionary.get_definitions("Consume")) == 1
    assert len(small_dictionary.get_definitions("wise")) == 2
    assert small_dictionary.is_word_noun("fire") is True
    assert small_dictionary.is_word_verb("fire") is True
    assert small_dictionary.is_word_adjective('warm') is True
    assert small_dictionary.is_word_noun("place") is False

    all_nouns = small_dictionary.get_all_nouns()
    assert isinstance(all_nouns, list)

    assert len(all_nouns) == 3
    assert "law" in all_nouns
    assert "injury" in all_nouns
    assert "fire" in all_nouns

    all_verbs = small_dictionary.get_all_verbs()
    assert isinstance(all_verbs, list)

    assert len(all_verbs) == 3
    assert "consume" in all_verbs
    assert "claim" in all_verbs
    assert "fire" in all_verbs

    all_adjectives = small_dictionary.get_all_adjectives()
    assert isinstance(all_adjectives, list)

    assert len(all_adjectives) == 4
    assert "wise" in all_adjectives
    assert "warm" in all_adjectives
    assert "beautiful" in all_adjectives
    assert "well-known" in all_adjectives

    search_result = small_dictionary.search("N", min_len=5, max_len=8)
    assert len(search_result) == 2
    assert 'consume' in search_result
    assert 'injury' in search_result

    print("Ready for submission!")

