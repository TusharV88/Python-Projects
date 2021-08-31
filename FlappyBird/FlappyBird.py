# Flappy Bird Game

import random  # For generating random numbers
import sys  # We will use sys.exit to exit the program
import pygame
from pygame.locals import *  # Basic pygame imports
from time import sleep
from pathlib import Path  # for directory listing


# Global Variables for the game
FPS = 35
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = "gallery/sprites/bird8.png"
BACKGROUND = ["gallery/sprites/bg11.jpg", "gallery/sprites/bg12.jpg", "gallery/sprites/bg13.jpg", "gallery/sprites/bg14.jpg", "gallery/sprites/bg15.jpg", "gallery/sprites/bg16.jpg", "gallery/sprites/bg17.jpg", "gallery/sprites/bg18.jpg", "gallery/sprites/bg19.jpg", "gallery/sprites/bg20.jpg", "gallery/sprites/bg21.jpg", "gallery/sprites/bg22.jpg", "gallery/sprites/bg23.jpg", "gallery/sprites/bg24.jpg", "gallery/sprites/bg25.jpg",
              "gallery/sprites/bg26.jpg", "gallery/sprites/bg27.jpg", "gallery/sprites/bg28.jpg", "gallery/sprites/bg29.jpg", "gallery/sprites/bg30.jpg", "gallery/sprites/bg31.jpg", "gallery/sprites/bg32.jpg", "gallery/sprites/bg33.jpg", "gallery/sprites/bg34.jpg", "gallery/sprites/bg35.jpg", "gallery/sprites/bg36.jpg", "gallery/sprites/bg37.jpg", "gallery/sprites/bg38.jpg", "gallery/sprites/bg39.jpg", "gallery/sprites/bg40.jpg", "gallery/sprites/bg41.jpg"]
PIPE = "gallery/sprites/pipe.png"


BackgroundGameMusic = ["Game Music/GameMusic1.mp3", "Game Music/GameMusic2.mp3", "Game Music/GameMusic3.mp3", "Game Music/GameMusic4.mp3", "Game Music/GameMusic5.mp3",
                       "Game Music/GameMusic6.mp3", "Game Music/GameMusic7.mp3", "Game Music/GameMusic8.mp3", "Game Music/GameMusic9.mp3", "Game Music/GameMusic10.mp3", "Game Music/GameMusic11.mp3"]

IntroMusic = ['Game Music/IntroMusic.mp3']

DIRECTORY = Path("./Game Music") # Take the Song Folder

BACKGROUND1 = "gallery/sprites/welcome.jpg"


def welcomeScreen():
    """
    Shows welcome images on the screen
    """

    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
    messagey = int(SCREENHEIGHT*0.13)
    basex = 0
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['welcome'], (0, 0))
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey))
                SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
                pygame.display.update()
                FPSCLOCK.tick(FPS)


def mainGame():
    score = 0
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENWIDTH/2)
    basex = 0

    # Create 2 pipes for blitting on the screen
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # my List of upper pipes
    upperPipes = [
        {'x': SCREENWIDTH+200, 'y': newPipe1[0]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y': newPipe2[0]['y']},
    ]
    # my List of lower pipes
    lowerPipes = [
        {'x': SCREENWIDTH+200, 'y': newPipe1[1]['y']},
        {'x': SCREENWIDTH+200+(SCREENWIDTH/2), 'y': newPipe2[1]['y']},
    ]

    pipeVelX = -4

    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerFlapAccv = -8  # velocity while flapping
    playerFlapped = False  # It is true only when the bird is flapping

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUNDS['wing'].play()

        # This function will return true if the player is crashed
        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes)
        if crashTest:
            return

        # check for score
        playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                score += 1
                #print(f"Your score is {score}")
                GAME_SOUNDS['point'].play()
            if score == 0:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[0]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 50:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[1]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 100:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[2]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 150:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[3]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 200:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[4]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 250:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[5]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 300:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[6]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 350:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[7]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 400:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[8]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 450:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[9]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 500:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[10]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 550:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[11]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 600:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[12]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 650:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[13]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 700:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[14]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 850:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[15]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 900:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[16]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 950:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[17]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 1000:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[18]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 1050:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[19]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 1100:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[20]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 1150:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[21]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 1200:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[22]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 1250:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[23]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 1300:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[24]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 1350:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[25]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 1400:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[26]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 1450:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[27]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 1500:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[28]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 1550:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[29]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
            elif score == 1600:
                GAME_SPRITES['background'] = pygame.image.load(
                    BACKGROUND[30]).convert()
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))

        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False
        playerHeight = GAME_SPRITES['player'].get_height()
        playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

        # move pipes to the left
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

        # Add a new pipe when the first is about to cross the leftmost part of the screen
        if 0 < upperPipes[0]['x'] < 5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        # if the pipe is out of the screen, remove it
        if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        # Lets blit our sprites now
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_SPRITES['pipe'][0],
                        (upperPipe['x'], upperPipe['y']))
            SCREEN.blit(GAME_SPRITES['pipe'][1],
                        (lowerPipe['x'], lowerPipe['y']))

        SCREEN.blit(GAME_SPRITES['base'], (basex, GROUNDY))
        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_SPRITES['numbers'][digit].get_width()
        Xoffset = (SCREENWIDTH - width)/2

        for digit in myDigits:
            SCREEN.blit(GAME_SPRITES['numbers'][digit],
                        (Xoffset, SCREENHEIGHT*0.12))
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery > GROUNDY - 25 or playery < 0:
        GAME_SOUNDS['hit'].play()
        pygame.mixer.music.stop()
        return True

    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
            GAME_SOUNDS['hit'].play()
            pygame.mixer.music.stop()
            return True

    for pipe in lowerPipes:
        if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
            GAME_SOUNDS['hit'].play()
            pygame.mixer.music.stop()
            return True

    return False


def getRandomPipe():
    """
    Generate positions of two pipes(one bottom straight and one top rotated ) for blitting on the screen
    """
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    offset = SCREENHEIGHT/3
    y2 = offset + random.randrange(0, int(SCREENHEIGHT -
                                          GAME_SPRITES['base'].get_height() - 1.2 * offset))
    pipeX = SCREENWIDTH + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1},  # upper Pipe
        {'x': pipeX, 'y': y2}  # lower Pipe
    ]
    return pipe


if __name__ == "__main__":
    # This will be the main point from where our game will start
    pygame.mixer.init()
    pygame.init()  # Initialize all pygame's modules
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird by TusharVerma')
    pygame.display.set_icon(pygame.image.load("gallery/sprites/bird_icon.ico"))
    GAME_SPRITES['numbers'] = (
        pygame.image.load("gallery/sprites/Final0.png").convert_alpha(),
        pygame.image.load("gallery/sprites/Final1.png").convert_alpha(),
        pygame.image.load("gallery/sprites/Final2.png").convert_alpha(),
        pygame.image.load("gallery/sprites/Final3.png").convert_alpha(),
        pygame.image.load("gallery/sprites/Final4.png").convert_alpha(),
        pygame.image.load("gallery/sprites/Final5.png").convert_alpha(),
        pygame.image.load("gallery/sprites/Final6.png").convert_alpha(),
        pygame.image.load("gallery/sprites/Final7.png").convert_alpha(),
        pygame.image.load("gallery/sprites/Final8.png").convert_alpha(),
        pygame.image.load("gallery/sprites/Final9.png").convert_alpha(),
    )

    GAME_SPRITES['message'] = pygame.image.load(
        "gallery/sprites/message5.png").convert_alpha()
    GAME_SPRITES['base'] = pygame.image.load(
        "gallery/sprites/base.png").convert_alpha()
    GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
                            pygame.image.load(PIPE).convert_alpha()
                            )

    # Game sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound("gallery/audio/die.wav")
    GAME_SOUNDS['hit'] = pygame.mixer.Sound("gallery/audio/hit.wav")
    GAME_SOUNDS['point'] = pygame.mixer.Sound("gallery/audio/point.wav")
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound("gallery/audio/swoosh.wav")
    GAME_SOUNDS['wing'] = pygame.mixer.Sound("gallery/audio/wing.wav")

    #GAME_SPRITES['background'] = pygame.image.load(BACKGROUND[0]).convert()
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()
    GAME_SPRITES['welcome'] = pygame.image.load(BACKGROUND1).convert()

    while True:
        welcomeScreen()  # Shows welcome screen to the user until he presses a button
        for fp in DIRECTORY.glob('*.mp3'):
            # add each file to the queue
            pygame.mixer.music.load(str(fp))
            pygame.mixer.music.play()

            # now wait until the song is over
            while pygame.mixer.music.get_busy():
                sleep(0)  # wait 1 second.
                mainGame()  # This is the main game function
