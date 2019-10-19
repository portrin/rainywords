import pygame
from os import path
from word import Word, WordLibrary, CurrentWordList

width = 1200
height = 800
BACKSPACE = 8
RETURN = 13
SPACE = 32

# test words
words = ["hello", "int", "hi", "good", "read", "apple", "thanks", "tree", "sun", "moon"]

font = pygame.font.get_default_font()

win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Rainy Words")
title = pygame.image.load("src/rainywords.png").convert_alpha()

class Player():
    def __init__(self, words, score):
        #track current words on screen.
        self.current_word_list = CurrentWordList([Word("hi",1200,800)])
        #words list that can be generated.
        self.words_library = WordLibrary(words)
        #track users scores
        self.score = 0
        #current word that typing
        self.pressed_word = ""







def redrawWindow(win):
    win.fill((255,255,255))
    pygame.display.update()

def menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return
        win.fill((255,255,255))
        win.blit(title, (350,200))
        pygame.display.update()

def main():
    run = True
    menu()
    player = Player(words, score=0)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                #player press return to submit word
                if event.key == RETURN:
                    #if what player types match
                    if player.pressed_word in player.current_word_list.word_to_string_list():
                        #remove correct word from the list and clear word from screen
                        player.current_word_list.remove(player.pressed_word)
                        player.score += len(player.pressed_word)
                        player.pressed_word = ""
                        print(player.score)
                elif event.key == BACKSPACE:
                    #player press backspace
                    player.pressed_word = player.pressed_word[:-1]
                elif event.key == SPACE:
                    pass
                else:
                    player.pressed_word += pygame.key.name(event.key)
                print(player.pressed_word)
            
        redrawWindow(win)

main()