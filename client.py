import pygame
from os import path
from word import Word, WordLibrary, CurrentWordList

global DELAY
width = 1200
height = 800
vel = 0.02
BACKSPACE = 8
ALPHABETS = 97,98
RETURN = 13
SPACE = 32
TIMER = 20
TIMER_GEN_WORD = 21
MISSED_WORD = 22
DELAY = 2300
pygame.font.init()

# test words
words = open("src/words.txt", 'r').read().split(" ")[:-1]
#fonts_list = pygame.font.get_default_font()
font = pygame.font.SysFont("comicsansmsttf", 32)


win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Rainy Words")
##title = pygame.image.load("src/rainywords.png").convert_alpha()
frontpageImage = pygame.image.load("src/frontpage.jpg").convert_alpha()
gameImage = pygame.image.load("src/gamebg.jpg").convert_alpha()

class Player():
    def __init__(self, words, score, id = 1): # id comes from Agent object
        #track current words on screen.
        self.current_word_list = CurrentWordList()
        #track users scores
        self.score = 0
        #current word that typing
        self.pressed_word = ""
        #player id
        self.player_id = id



def redrawWindow(win, player, vel, DELAY):
    win.fill((255,255,255))
    win.blit(gameImage, (0,0))
    for word in player.current_word_list.current_word_list:
        text = font.render(word.word_to_string(), True, (255,255,255))
        word.vel += 0.006
        win.blit(text, (word.x, word.y))
        word.update_falling()
        if word.y > height:
            pygame.event.post(pygame.event.Event(22, {"word": word.word})) # send misword event
    vel += 0.4
    DELAY -= 50
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
        win.blit(frontpageImage, (0,0))
        #win.blit(title, (350,200))
        pygame.display.update()

def main():
    run = True
    menu()

    #GAME SETUP
    #clock = pygame.time.Clock()
    player = Player(words, score=0)
    #words list that can be generated.
    words_library = WordLibrary(words, vel)
    #timer for generate word
    pygame.time.set_timer(TIMER_GEN_WORD, DELAY)

    while run:
        #clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            #word genarating event
            elif event.type == TIMER_GEN_WORD:
                player.current_word_list.current_word_list.append(words_library.generate_words())
                print(player.current_word_list.word_to_string_list()) # for debugging
            elif event.type == pygame.KEYDOWN:
                #player press return to submit word
                if event.key == RETURN:
                    #if what player types match
                    if player.pressed_word in player.current_word_list.word_to_string_list():
                        #add correct sound
                        pygame.mixer.init(44100, -16,2,2048)
                        pygame.mixer.music.load("src/correctbgm.ogg")
                        pygame.mixer.music.play()
                        #remove correct word from the list and clear word from screen
                        player.current_word_list.remove(player.pressed_word)
                        player.score += len(player.pressed_word)
                        print(player.score)
                    else:
                        #add wrong sound
                        pygame.mixer.init(44100, -16,2,2048)
                        pygame.mixer.music.load("src/wrongbgm.ogg")
                        pygame.mixer.music.play()
                    player.pressed_word = "" 
                elif event.key == BACKSPACE:
                    #player press backspace
                    player.pressed_word = player.pressed_word[:-1]
                elif event.key == SPACE:
                    pass
                else:
                    player.pressed_word += pygame.key.name(event.key)
                print(player.pressed_word) # for debugging

            elif event.type == MISSED_WORD:
                player.current_word_list.remove(event.word)
                player.score -= len(event.word)
        redrawWindow(win, player, vel, DELAY)

main()