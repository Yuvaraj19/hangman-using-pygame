import pygame
import math
import random

# Set up display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# Load images
images = []
for i in range(7):
    image = pygame.image.load("hangman"+str(i)+".png")
    images.append(image)

# Button variables
RADIUS = 20
GAP = 15
A = 65
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# Fonts
LETTER_FONT = pygame.font.SysFont('lato', 40)
WORD_FONT = pygame.font.SysFont('lato', 60)
TITLE_FONT = pygame.font.SysFont('lato', 70)

# Game variable
hangman_status = 0
words = ['PYTHON', 'PYGAME', 'DEVELOPER',
         'PROGRAMMER', 'COMPUTER', 'IDE', 'CODING']
word = random.choice(words)
guessed = []

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up loop
FPS = 60
clock = pygame.time.Clock()
run = True


def draw():
    win.fill(WHITE)
    # Draw title
    text = TITLE_FONT.render("Yuvaraj's HANGMAN!", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # Draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # Draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 2)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width() /
                            2, y - text.get_height() / 2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(msg):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(msg, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width() /
                    2, HEIGHT/2 - text.get_height()/2))
    pygame.time.delay(2000)
    pygame.display.update()


while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1

    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break

    if won:
        display_message("YOU WON :)")
        break

    if hangman_status == 6:
        display_message("YOU LOST :(")
        break

pygame.quit()
