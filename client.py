import pygame
from os import path
from word import Word, WordLibrary, CurrentWordList
from networkutil import Agent

pygame.init()
global DELAY
#for networking
endpoint_addr = "0.0.0.0"
endpoint_port = 5000
#game parameter
width = 1200
height = 800
vel = 0.02
minute = 0
second = 0
minute_text = '0'
second_text = '00'
enemy_name = ''
enemy_score = 0
BACKSPACE = 8
RETURN = 13
SPACE = 32
COUNTDOWN = 180 # countdown per game 180 seconds
CLOCKTICK_EVENT = 20
TIMER_GEN_WORD = 21
MISSED_WORD = 22
DELAY = 2200
player_id = 0
score = 0
pygame.font.init()
pygame.display.init()
pygame.mixer.init(44100, -16,2,2048)
font = pygame.font.SysFont("comicsansmsttf", 32)
fontname = pygame.font.SysFont("comicsansmsttf", 40)
fontNameWelcome = pygame.font.SysFont("comicsansmsttf", 52)
user_text = font.render('', True, (0,0,0))

# test words
words = open("src/words.txt", 'r').read().split(" ")[:-1]
#setup game window
win = pygame.display.set_mode((width, height))

# load game materials
pygame.display.set_caption("Rainy Words")
frontpageImage = pygame.image.load("src/frontpage.jpg").convert_alpha()
gameImage = pygame.image.load("src/gamebg.jpg").convert_alpha()
welcomeImage = pygame.image.load("src/welcome.jpg").convert_alpha()
youwinImage = pygame.image.load("src/youwin.jpg").convert_alpha()
youloseImage = pygame.image.load("src/youlose.jpg").convert_alpha()
waitingImage = pygame.image.load("src/waiting.jpg").convert_alpha()


class Player():
    def __init__(self, words, score, agent, username='', id = 0): # id comes from Agent object
        #track current words on screen.
        self.current_word_list = CurrentWordList()
        #track users scores
        self.score = 0
        #current word that typing
        self.pressed_word = ""
        #player socket handler !!!
        self.agent = agent
        #each player username
        self.username = username
        #player id
        self.id = id



def redrawWindow(win, player, vel, DELAY, time_text, enemy_name, enemy_score):
    win.blit(gameImage, (0,0))
    win.blit(time_text, (555,35))
    username_text = font.render(player.username, True, (0,0,0))
    win.blit(username_text, (40,30)) # render username on screen
    score_text = font.render(str(player.score), True, (0,0,0))
    win.blit(score_text, (140,30))
    enemy_name_text = font.render(enemy_name, True, (0,0,0))
    win.blit(enemy_name_text, (890,30)) #render enemy name
    enemy_score_text = font.render(str(enemy_score), True, (0,0,0))
    win.blit(enemy_score_text, (990,30)) #render enemy score
    user_text = fontname.render(player.pressed_word, True, (0,0,0)) # render interactive typing
    win.blit(user_text, (530,730)) # interactive keypressed
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
    text = fontNameWelcome.render(name, True, (0,0,0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == RETURN:
                    return
        win.fill((255,255,255))
        win.blit(welcomeImage, (0,0))
        win.blit(text, (625,359))
        #win.blit(title, (350,200))
        pygame.display.update()

def frontpage(): #enter name page
    name = ""
    # pygame.mixer.music.load("src/bgm.ogg")
    pygame.mixer.Channel(0).set_volume(0.7)
    pygame.mixer.Channel(0).play(pygame.mixer.Sound("src/bgm.ogg"), -1)
    while True:
        text = fontname.render(name, True, (0,0,0))
        win.blit(frontpageImage, (0,0))
        win.blit(text, (360,675))
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
    welcome(name)
    #GAME SETUP
    number_of_player = 0
    enemy_name = ''
    time_text = font.render('3 : 00', True, (0,0,0))
    timeleft = COUNTDOWN # set variable to track timeleft
    clock = pygame.time.Clock()
    agent = Agent(endpoint_addr, endpoint_port) # initialize player network handler
    player = Player(words, 0, agent, name, 0)
    player.agent.connect() # connect player to the server
    ## waiting for another player
    while number_of_player < 2:
        win.blit(waitingImage, (0,0))
        pygame.display.update()
        message = player.agent.receive()
        player.agent.send({'player_id' : player.id,
                    'number_of_player' : number_of_player,
                    'score' : score,
                    'username' : player.username})
        print(message)
        try:
            player.id = message['player_id']
            number_of_player = message['number_of_player']
        except:
            pass
        print(player.id)
        print(number_of_player)
    #words list that can be generated.
    words_library = WordLibrary(words, vel)
    #timer for generate word
    pygame.time.set_timer(TIMER_GEN_WORD, DELAY)
    pygame.time.set_timer(CLOCKTICK_EVENT, 1000) # clock ticks every 1 second.

    while run:
        #clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            # clock tick event (timer)
            elif event.type == CLOCKTICK_EVENT:
                # do sth
                timeleft -= 1
                if timeleft == 0:
                    #go to play again screen (call play again method)
                    pass
                minute = timeleft // 60
                second = timeleft - (minute * 60)
                minute_text = str(minute)
                if second < 10:
                    second_text = '0' + str(second)
                else:
                    second_text = str(second)
                time_text = font.render(minute_text + ' : ' + second_text, True, (0,0,0)) # timer update (render)
                pass
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
                #add wrong sound
                pygame.mixer.music.load("src/wrongbgm.ogg")
                pygame.mixer.music.play()
                if player.score <= 0 or len(event.word) >= player.score:
                    player.score = 0
                else:
                    player.score -= len(event.word)
                print(player.score)
        player.agent.send({'player_id' : player.id,
                    'number_of_player' : number_of_player,
                    'score' : player.score,
                    'username' : player.username})
        message = player.agent.receive()
        if player.id == 1:
            enemy_name = message['username'][1]
            enemy_score = message['score'][1]
        elif player.id == 2:
            enemy_name = message['username'][0]
            enemy_score = message['score'][0]
        redrawWindow(win, player, vel, DELAY, time_text, enemy_name, enemy_score)

main()