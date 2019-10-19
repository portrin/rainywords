import random

class Word():
    def __init__(self, word, win_width, win_height):
        # collection of random words from server to client
        self.word = word
        self.x = random.randint(100, win_width - 100)
        self.y = 0
        self.vel = 0.005
    
    def clear_words(self):
        pass

    def string_compare(self, str, word):
        return str == self.word

    def word_to_string(self):
        return self.word

class WordLibrary():
    def __init__(self, words):
        self.word_library = words # words come from .csv file that was loaded in client.py

    def generate_words(self):
        try:
            word = Word(random.choice(self.word_library))
        except random.error as error:
            print(str(error))
        return word

class CurrentWordList():
    def __init__(self, wordList=[]):
        self.current_word_list = wordList

    def word_to_string_list(self):
        string_list = []
        for x in self.current_word_list:
            string_list.append(x.word_to_string())
        return string_list

    def remove(self, word):
        for x in self.current_word_list:
            if x.word == word:
                x.clear_words()
                self.current_word_list.remove(x)
        return
