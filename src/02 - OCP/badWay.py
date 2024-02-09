class EnglishHindiTranslator:
    def __init__(self):
        self.words_mapping = {
            "school": "विद्यालय",
            "college": "कॉलेज"
        }

    def translate_into_hindi(self, word):
        hindi_word = self.words_mapping.get(word)
        print('{} in hindi {}'.format(word, hindi_word))


translator = EnglishHindiTranslator()
translator.translate_into_hindi('school')