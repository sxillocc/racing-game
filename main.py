import pygame
import random

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
p1_turn = True
winner = False
win = ""

# dice button
d_width = 192
d_height = 48
d_x = screen_width - d_width - padding
d_y = screen_height - padding - d_height
dice = (d_x, d_y, d_width, d_height)
dice_disable = False

# track init
t_width = 50
t_height = screen_height - (2*padding)

# dice init
rolled = 0
first_roll = True

#helper init
target = 0
increment = 0

# players positions
px1 = (screen_width/2) - imgWidth - 100
px2 = (screen_width/2) + 100
p1 = 0
p2 = 0

# players images
playerImg = pygame.image.load("ca.png")
player2Img = pygame.image.load("ironman.png")

#steps init
step = 3
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
def dice_button(color,fontcolor=white):
    pygame.draw.rect(screen, color, dice)
    font = pygame.font.SysFont("Raleway", 20)
    text = font.render("Throw Dice", True, fontcolor, None)
    text_rect = text.get_rect(center=(d_x + d_width / 2, d_y + d_height / 2))
    screen.blit(text, text_rect)


# dice helper
def helper_label(msg):
    font = pygame.font.SysFont("Raleway", 32)
    text = font.render(msg, True, white, blueGrey300)
    label_width = text.get_width()
    label_height = text.get_height()
    pos_x = screen_width - label_width/2 - padding
    pos_y = d_y - label_height/2 - 12
    text_rect = text.get_rect(center=(pos_x, pos_y))
    screen.blit(text, text_rect)

#Winner Label
def winner_label(msg):
    font = pygame.font.SysFont("Raleway", 128)
    text = font.render(msg, True, blueGrey700, white)
    text_rect = text.get_rect(center=(screen_width/2, screen_height/2))
    screen.blit(text, text_rect)


# dice result
def dice_result(msg,firstroll):
    m = ""
    label_height = 0
    p_x = 0
    if firstroll:
        m = "You have not yet Rolled"
    else:
        m = "You have Rolled"
        bigfont = pygame.font.SysFont("Raleway", 256)
        text = bigfont.render(msg, True, white, blueGrey300)
        label_width = text.get_width()
        label_height = text.get_height()
        pos_x = screen_width - label_width / 2 - 2 * padding
        pos_y = screen_height / 2
        text_rect = text.get_rect   (center=(pos_x, pos_y))
        screen.blit(text, text_rect)
        p_x = pos_x

    font = pygame.font.SysFont("Raleway", 32)
    t = font.render(m, True, white, blueGrey300)
    tw = t.get_width()
    if first_roll:
        p_x = screen_width - tw / 2 - padding
    p_y = screen_height / 2 - label_height/2 - 20
    t_rect = t.get_rect(center=(p_x, p_y))
    screen.blit(t, t_rect)


# Game Loop
mainLoop = True
while mainLoop:
    clock = pygame.time.Clock()
    screen.fill(blueGrey300)
    # show dice result
    dice_result(str(rolled), first_roll)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 1 left, 2 middle, 3 right
            if event.button == 1:
                e_width = event.pos[0]
                e_height = event.pos[1]
                if ((d_x + d_width) > e_width > d_x) and (d_y < e_height < d_y + d_height):
                    if dice_disable:
                        break
                    else:
                        first_roll = False
                        temp = random.randrange(1,7)
                        while temp == rolled:
                            temp = random.randrange(1, 7)
                        rolled = temp
                        if p1_turn:
                            target = p1 + rolled
                            dice_disable = True
                            if target > step:
                                target = 0
                                p1_turn = False
                                dice_disable = False
                        else:
                            target = p2 + rolled
                            dice_disable = True
                            if target > step:
                                target = 0
                                p1_turn = True
                                dice_disable = False

    if target != 0:
        increment = 0.1
    else:
        increment = 0

    if dice_disable and not winner:
        if p1_turn:
            if p1 + increment >= target:
                p1 = target
                target = 0
                increment = 0
                dice_disable = False
                if p1 == step:
                    p1_turn = False
                    dice_disable = True
                    winner = True
                    win = "Player 1"
                    print("Captain America Winner")
            else:
                p1 = p1 + increment
        else:
            if p2 + increment >= target:
                p2 = target
                target = 0
                increment = 0
                dice_disable = False
                if p2 == step:
                    p1_turn = True
                    dice_disable = True
                    winner = True
                    win = "Player 2"
                    print("Ironman Winner")
            else:
                p2 = p2 + increment

    mouse = pygame.mouse.get_pos()

    # disable_dice
    if dice_disable:
        dice_button(white, black)

    # dice button
    if ((d_x + d_width) > mouse[0] > d_x) and (d_y < mouse[1] < d_y + d_height) and not dice_disable:
        dice_button(blueGrey700d)
    elif not dice_disable:
        dice_button(blueGrey700)

    # Shows whose turn it is
    if p1_turn:
        helper_label("PLAYER 1 TURN")
    else:
        helper_label("PLAYER 2 TURN")
    #track
    track()
    #player1
    player(p1)
    #player2
    player2(p2)

    if winner:
        winner_label("  Winner is "+win+"  ")

    pygame.display.update()
    clock.tick(30)

pygame.quit()