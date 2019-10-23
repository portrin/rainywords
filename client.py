import pygame
from os import path
from word import Word, WordLibrary, CurrentWordList

global DELAY
width = 1200
height = 800
vel = 0.02
BACKSPACE = 8
RETURN = 13
SPACE = 32
TIMER = 20
TIMER_GEN_WORD = 21
MISSED_WORD = 22
DELAY = 2300
player_id = 0
pygame.font.init()
pygame.mixer.init(44100, -16,2,2048)
#fonts_list = pygame.font.get_default_font()
font = pygame.font.SysFont("comicsansmsttf", 32)
user_text = font.render('', True, (0,0,0))

# test words
words = open("src/words.txt", 'r').read().split(" ")[:-1]


win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Rainy Words")
##title = pygame.image.load("src/rainywords.png").convert_alpha()
frontpageImage = pygame.image.load("src/frontpage.jpg").convert_alpha()
gameImage = pygame.image.load("src/gamebg.jpg").convert_alpha()
welcomeImage = pygame.image.load("src/welcome.jpg").convert_alpha()


class Player():
    def __init__(self, words, score, username='', id = 0): # id comes from Agent object
        #track current words on screen.
        self.current_word_list = CurrentWordList()
        #track users scores
        self.score = 0
        #current word that typing
        self.pressed_word = ""
        #each player username
        self.username = username
        #player id
        self.player_id = id



def redrawWindow(win, player, vel, DELAY):
    win.fill((255,255,255))
    win.blit(gameImage, (0,0))
    user_text = font.render(player.pressed_word, True, (255,255,255)) # render interactive typing
    win.blit(user_text, (10,750)) # interactive keypressed
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

def welcome(name):
    text = font.render(name, True, (0,0,0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == RETURN:
                    return
        win.fill((255,255,255))
        win.blit(welcomeImage, (0,0))
        win.blit(text, (610,380))
        #win.blit(title, (350,200))
        pygame.display.update()

def frontpage(): #enter name page
    name = ""
    # pygame.mixer.music.load("src/bgm.ogg")
    pygame.mixer.Channel(0).set_volume(0.7)
    pygame.mixer.Channel(0).play(pygame.mixer.Sound("src/bgm.ogg"))
    while True:
        text = font.render(name, True, (0,0,0))
        win.blit(frontpageImage, (0,0))
        win.blit(text, (355,680))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            #when user type their name
            if event.type == pygame.KEYDOWN:
                if event.key == RETURN:
                    return name
                elif event.key == BACKSPACE:
                    name = name[:-1]
                else:
                    if len(name) < 30:
                        name += pygame.key.name(event.key)
        pygame.display.update()

def main():
    run = True
    name = frontpage()
    print(pygame.event.get())
    welcome(name)

    #GAME SETUP
    clock = pygame.time.Clock()
    player = Player(words, 0, player_id)
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
                        #remove correct word from the list and clear word from screen
                        player.current_word_list.remove(player.pressed_word)
                        #add correct sound
                        pygame.mixer.music.load("src/correctbgm.ogg")
                        pygame.mixer.music.play()
                        player.score += len(player.pressed_word)
                        print(player.score)
                    else:
                        #add wrong sound
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
                    #user_text = font.render(player.pressed_word, True, (255,255,255))
                print(player.pressed_word) # for debugging

            elif event.type == MISSED_WORD:
                player.current_word_list.remove(event.word)
                if player.score <= 0 or len(event.word) >= player.score:
                    player.score = 0
                else:
                    player.score -= len(event.word)
                print(player.score)
        redrawWindow(win, player, vel, DELAY)

main()