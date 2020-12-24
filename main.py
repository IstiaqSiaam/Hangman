import pygame
import math
import random

#set window
pygame.init()
WIDTH, HEIGHT = 700, 500

window = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption(("HangMan"))

#loading images

images = []

for i in range(7):
  image = pygame.image.load(str(i) + ".png")
  images.append(image)

#Loading and processing the word dictionary
a_file = open("dictionary.txt", "r")
list_of_lists = []
for line in a_file:
  stripped_line = line.strip()
  line_list = stripped_line. split()
  line_up = [x.upper() for x in line_list]
  list_of_lists. append(line_up)
a_file. close()

wordlist = [''.join(i) for i in list_of_lists]
#words = str(wordlist)

#colors
Grey = (125,125,125)
BLACK = (0,0,0)
WHITE = (255,255,255)

#fonts
LETTER_FONT = pygame.font.SysFont('ariel', 40)
WORD_FONT = pygame.font.SysFont('ariel', 60)

# Game variables
Hangman_Status=0
#words = ['HELLO', 'DARKNESS', 'MY', 'OLD', 'FRIEND']
#print(words)
word = random.choice(wordlist)
guessed = []

FPS = 60
clock = pygame.time.Clock()

#buttons
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x,y, chr( A + i ), True])

#drawing

def draw():
  window.fill(Grey)

  #draw word
  display_word = ""
  for letter in word:
    if letter in guessed:
      display_word += letter + " "
    else:
      display_word +="_ "
  text = WORD_FONT.render(display_word,1,BLACK)
  window.blit(text, (180,310))

  #draw buttons
  for letter in letters:
    x,y,ltr,IsVisible =letter
    if IsVisible:
      pygame.draw.circle(window, BLACK, (x,y), RADIUS, 3)
      text = LETTER_FONT.render(ltr, 1, BLACK)
      window.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
  
  window.blit(images[Hangman_Status], (180,70))
  pygame.display.update()


run = True
#show message
def display_text(message):
  window.fill(WHITE)
  text = WORD_FONT.render(message,1,BLACK)
  window.blit(text,(WIDTH/2 - text.get_width()/2 , HEIGHT/2 - text.get_height()/2))
  pygame.display.update()
  pygame.time.delay(2000)

while run:
  clock.tick(FPS)
  draw()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_x,mouse_y = pygame.mouse.get_pos()
      for letter in letters:
        x,y,ltr,IsVisible = letter
        if IsVisible:
          distance = math.sqrt((x - mouse_x)**2 + (y - mouse_y)**2)
          if distance < RADIUS:
            letter[3] = False
            guessed.append(ltr)
            if ltr not in word:
              Hangman_Status += 1

  won = True

  for letter in word:
    if letter not in guessed:
      won = False
      break
  if won:
    display_text("YOU WON")
    break

  if Hangman_Status == 6:
    display_text("YOU LOST")
    break

pygame.quit()