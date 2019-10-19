import random

class Word():
    def __init__(self, words):
        # collection of random words from server to client
        self.words = words

    def generate_words(self):
        try:
            word = random.choice(self.words)
        except random.error as error:
            print(str(error))
        return word