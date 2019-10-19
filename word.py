import random

class Word():
    def __init__(self, word, resolution=(1200, 800)):
        # collection of random words from server to client
        self.word = word
        self.x = random.randint(100, resolution[1] - 100)
        self.y = 0
        self.vel = 10
    
    def clear_words(self):
        pass

    def string_compare(self, str, word):
        return str == self.word

    def word_to_string(self):
        return self.word

    def update_falling(self):
        self.y += self.vel

class WordLibrary():
    def __init__(self, words, resolution=(1200,800)):
        self.word_library = words # words come from .csv file that was loaded in client.py

    def generate_words(self):
        word = Word(random.choice(self.word_library), resolution=(1200,800))
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
