from abc import ABC, abstractmethod

"""
Open Close Principle(OCP)

Class should be open for extension and close for modification
"""

class Translator(ABC):
    def __init__(self):
        self.words_mapping = {}

    @abstractmethod
    def translate(self):
        pass


class EnglishHindiTranslator(Translator):
    def __init__(self):
        self.words_mapping = {
            "school": "विद्यालय",
            "college": "कॉलेज"
        }

    def translate(self, word):
        hindi_word = self.words_mapping.get(word)
        print('{} in Hindi {}'.format(word, hindi_word))


class EnglishChineseTranslator(Translator):
    def __init__(self):
        self.words_mapping = {
            "school": "學校",
            "college": "大學"
        }

    def translate(self, word):
        hindi_word = self.words_mapping.get(word)
        print('{} in Chinese {}'.format(word, hindi_word))


class Main:
    def main(word):
        for translator in Translator.__subclasses__():
            translator().translate(word)


Main.main("school")