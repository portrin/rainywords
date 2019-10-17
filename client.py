import pygame
from word import Word

width = 1200
height = 800

# test words
words = ["hello", "int", "hi", "good", "read", "apple", "thanks", "tree", "sun", "moon"]
#word = Word(words)

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rainy Words")

def redrawWindow(win):
    win.fill((255,230,230))
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        redrawWindow(win)

main()