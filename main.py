import pygame

# init pygame
pygame.init()

# init color
black = (0,0,0)
white = (255,255,255)
blueGrey300 = (144,164,174)
blueGrey900 = (38,50,56)
blueGrey700d = (28, 49, 58)#1c313a
blueGrey700 = (69, 90, 100)#455a64
grey900 = (33, 33, 33)
teal900 = (0,77,64)

# Screen Info
info = pygame.display.Info()
screen_width = info.current_w - 68
screen_height = info.current_h - 64

# Display Screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game of Life")
icon = pygame.image.load("running_blue.png")
pygame.display.set_icon(icon)
screen.fill(blueGrey300)

# Helper Functions

# players init
imgWidth = 64
imgHeight = 64
padding = 50

# dice button
d_width = 192
d_height = 48
d_x = screen_width - d_width - padding
d_y = screen_height - padding - d_height
dice = (d_x, d_y, d_width, d_height)

# track init
t_width = 50
t_height = screen_height - (2*padding)

# players positions
px1 = (screen_width/2) - imgWidth - 100
px2 = (screen_width/2) + 100
p1 = 0
p2 = 0

# players images
playerImg = pygame.image.load("ca.png")
player2Img = pygame.image.load("ironman.png")

#steps init
step = 50
stepSize = t_height / step

def player(pos):
    py1 = t_height + padding - (imgHeight / 2) - pos * stepSize
    font = pygame.font.SysFont("Raleway", 25)
    h = " " + str(pos) + " "
    text = font.render(h,True,blueGrey900, blueGrey300)
    tw = text.get_width()
    tx = px1 - tw / 2 - 8
    ty = py1 + imgHeight / 2
    text_rect = text.get_rect(center=(tx, ty))

    #print items
    screen.blit(playerImg, (px1, py1))
    screen.blit(text, text_rect)


def player2(pos):
    py2 = t_height + padding - (imgHeight / 2) - pos * stepSize
    font = pygame.font.SysFont("Raleway", 25)
    h = " " + str(pos) + " "
    text = font.render(h, True, blueGrey900, blueGrey300)
    tw = text.get_width()
    tx = px2 + imgWidth + tw / 2 + 8
    ty = py2 + imgHeight / 2
    text_rect = text.get_rect(center=(tx, ty))

    # print items
    screen.blit(player2Img, (px2, py2))
    screen.blit(text, text_rect)


# draw track
def track():
    tx = screen_width/2 - t_width/2
    ty = padding
    t = (tx,ty,t_width,t_height)
    pygame.draw.rect(screen,blueGrey900,t)

# draw dice
def dice_button(color):
    pygame.draw.rect(screen, color, dice)

# Game Loop
mainLoop = True
while mainLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False

    mouse = pygame.mouse.get_pos()
    if ((d_x + d_width) > mouse[0] > d_x) and (d_y < mouse[1] < d_y + d_height) :
        dice_button(blueGrey700d)
    else:
        dice_button(blueGrey700)

    track()
    player(p1)
    player2(p2)
    pygame.display.update()

pygame.quit()