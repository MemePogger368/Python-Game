import pygame
import random
import time 
pygame.init()



# ------------------------------------------------------------------------------------------VV window screen size
window = pygame.display.set_mode((500,500))
pygame.display.set_caption("I'M FAST AT THE CODING")
# ------------------------------------------------------------------------------------------
# --------------------------------------------VV coins class
class coins:
    def __init__(self,x,y,height,width,color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.rect = pygame.Rect(x,y,height,width)
    def draw(self):
        self.rect.topleft = (self.x,self.y)
        pygame.draw.rect(window, NiceOlive, self.rect)

# ------------------------------------------------------------------------------------------



# --------------------------------------VVV player class

# draw the player
class player:
    def __init__(self,x,y,height,width,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isJump = False
        self.JumpCount = 10
        self.speed = 5
        self.fall = 0
        self.color = color
        self.rect = pygame.Rect(x,y,height,width)
    def draw(self):
        self.rect.topleft = (self.x,self.y)
        pygame.draw.rect(window, self.color, self.rect)
# ------------------------------------------------------------------------------------------

# ------------------------------------------VV enemy class

class enemys:
    def __init__(self,x,y,height,width,color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
        self.rect = pygame.Rect(x,y,height,width)
    def draw(self):
        self.rect.topleft = (self.x,self.y)
        pygame.draw.rect(window, self.color, self.rect)
# ------------------------------------------------------------------------------------------

# --------------------------VV frames per sec
# FPS
FPS = 60
clock = pygame.time.Clock()
# ------------------------------------------------------------------------------------------
# ---------VV colors

# COLORS
NiceYellow = (255,255,0)
NiceOlive = (0, 255, 0)
# ------------------------------------------------------------------------------------------

# ----------------------------VV define enemy (enemy is platform) and players xx,y,height and colors
# define enemy and player class
playerman = player(40,390,30,30, NiceOlive)
enemy1 = enemys(150,390,100,10, NiceYellow)
enemy2 = enemys(300,300,100,10, NiceYellow)
enemy3 = enemys(80,250,100,10, NiceYellow)
enemy4 = enemys(-5000,490,100000,100, NiceYellow)

enemies = [enemy1,enemy2,enemy3,enemy4]
# ------------------------------------------------------------------------------------------


# --------------------------define coins colors and width,heights anD coins LIST
coin1 = coins(250,250,20,20,NiceOlive)
coin2 = coins(350,350,20,20,NiceOlive)
coin3  = coins(300,300,20,20,NiceOlive)
coin4 = coins(150,150,20,20,NiceOlive)
coin5  = coins(50,390,20,20,NiceOlive)
Coins_list = [coin1,coin2,coin3,coin4,coin5]   
# ------------------------------------------------------------------------------------------


# -----------VV scoring 
# display scoring
font = pygame.font.Font('freesansbold.ttf', 32)
score = 0
text = font.render('Score = ' + str(score), True, NiceOlive)
textRect = text.get_rect()  
textRect.center = (100, 40)
# ------------------------------------------------------------------------------------------
# main loop
runninggame = True
while runninggame:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runninggame = False
# -----------------------Draw the players and coins and enemys
    window.fill((0,0,0))
    window.blit(text,textRect)
    for coin in Coins_list:
        coin.draw()

    playerman.draw()
    for enemy in enemies:
        enemy.draw()

# ------------------------------------------------------------------------------------------

# --------------------------# VV screen movements
    if playerman.y < 250:
        playerman.y += 1
        for enemy in enemies:
            enemy.y += playerman.speed
        for coin in Coins_list:
            coin.y += playerman.speed

    if playerman.y > 450:
        playerman.y -= playerman.fall
        for enemy in enemies:
            enemy.y -= playerman.fall
        for coin in Coins_list:
            coin.y -= playerman.fall

# ------------------------------------------------------------------------------------------
# ----------------------------VV player keys and screen movements
    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT]:
        playerman.x -= playerman.speed
        if playerman.x < 100:
            playerman.x += playerman.speed
            for enemy in enemies:
                enemy.x += playerman.speed
            for coin in Coins_list:
                coin.x += playerman.speed



    if keys[pygame.K_RIGHT]:
        playerman.x += playerman.speed
        if playerman.x > 400:
            playerman.x -= playerman.speed
            for enemy in enemies:
                enemy.x -= playerman.speed
            for coin in Coins_list:
                coin.x -= playerman.speed
# ------------------------------------------------------------------------------------------

# ---------------------------collisions with player and enemy
    if not playerman.isJump:
        playerman.y += playerman.fall
        playerman.fall += 1
        collide = False
        for enemy in enemies:
            if playerman.rect.colliderect(enemy.rect):
                collide = True
                playerman.y = enemy.rect.top - playerman.height + 1
                if playerman.rect.right > enemy.rect.left and playerman.rect.left < enemy.rect.left - playerman.width:
                    playerman.x = enemy.rect.left - playerman.width
                if playerman.rect.left < enemy.rect.right and playerman.rect.right > enemy.rect.right + playerman.width:
                    playerman.x = enemy.rect.right
# ------------------------------------------------------------------------------------------
# ---------------------------------collision with coins and player     
        for i in range(len(Coins_list)-1,-1,-1):
            if playerman.rect.colliderect(Coins_list[i].rect):
                del Coins_list[i]
                score += 1
                text = font.render('Score = ' + str(score), True, NiceOlive)
                textRect = text.get_rect()  
                textRect.center = (100, 40)                
# ------------------------------- here is the problem I said if playerman.rect.colliderect coin1 it should then collide and delete the coin1 from coin list and then it should add it in to the score 1 point 


        if playerman.rect.bottom >= 500:
            collide = True
            playerman.isJump = False
            playerman.JumpCount = 10
            playerman.y = 500 - playerman.height
        if collide:
            if keys[pygame.K_SPACE]:
                playerman.isJump = True
            playerman.fall = 0

    else:
        if playerman.JumpCount > 0:
            playerman.y -= (playerman.JumpCount*abs(playerman.JumpCount))*0.3
            playerman.JumpCount -= 1
        else:
            playerman.isJump = False
            playerman.JumpCount = 10


    pygame.display.update()
pygame.quit()