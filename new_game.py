import pygame
import random

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Tanks')

# icon = pygame.image.load('apple.png')
# pygame.display.set_icon(icon)

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (200, 200, 0)
green = (0, 155, 0)
blue = (0, 0, 255)

clock = pygame.time.Clock()

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)


# img = pygame.image.load('snakehead.png')
# appleimg = pygame.image.load('apple.png')

def score(score):
    text = smallfont.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, [0, 0])


def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)


def pause():
    paused = True

    message_to_screen("Paused",
                      black,
                      -100,
                      size="large")
    message_to_screen("Press C to continue or Q to quit",
                      black,
                      25)
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        clock.tick(5)


def game_intro():
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    intro = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(white)
        message_to_screen("Welcome to Tanks!", green, -100, "large")
        message_to_screen("The objective is to shoot and destroy", black, -30)
        message_to_screen("the enemy tank before they destroy you.", black, 10)
        message_to_screen("The more enemies you destroy, the harder they get.", black, 50)
        # message_to_screen("Press E to play, C to pause, or Q to quit", black, 180)

        pygame.draw.rect(gameDisplay, green, (150, 500, 100, 50))
        pygame.draw.rect(gameDisplay, yellow, (350, 500, 100, 50))
        pygame.draw.rect(gameDisplay, red, (550, 500, 100, 50))

        pygame.display.update()

        clock.tick(15)


game_intro()


def gameLoop():
    gameExit = False
    gameOver = False
    FPS = 20

    while not gameExit:

        if gameOver:
            message_to_screen("Game over",
                              red,
                              y_displace=-50,
                              size="large")
            message_to_screen("Press R to play again, Q to quit",
                              black,
                              50,
                              size="medium")
            pygame.display.update()

        while gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_r:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    pass
                elif event.key == pygame.K_d:
                    pass
                elif event.key == pygame.K_w:
                    pass
                elif event.key == pygame.K_s:
                    pass
                elif event.key == pygame.K_c:
                    pause()

        gameDisplay.fill(white)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()


gameLoop()
