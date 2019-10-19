import pygame
from os import path
from word import Word

width = 1200
height = 800

# test words
words = ["hello", "int", "hi", "good", "read", "apple", "thanks", "tree", "sun", "moon"]

font = pygame.font.get_default_font()

win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Rainy Words")
title = pygame.image.load("src/rainywords.png").convert_alpha()

class Player():
    def __init__(self, words, score):
        #track current words on screen.
        self.current_word_list = [] 
        #words list that can be generated.
        self.words_library = Word(words)
        #track users scores
        self.score = 0






def redrawWindow(win):
    win.fill((255,230,230))
    pygame.display.update()

def menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return
        win.fill((255,230,230))
        win.blit(title, (350,200))
        pygame.display.update()

def main():
    run = True
    menu()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        redrawWindow(win)

main()