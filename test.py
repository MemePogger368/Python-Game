#simple platformer

#set up of our game


import pygame #Imports Pygame alowing us to make a game
from pygame.locals import *  #this gives the all the local varabials e.g. pygame.quit
import sys #imports the sys
import random #imports random alowing for randomnes to happen

pygame.init() #sets up the Pygame to be used for the game
vec = pygame.math.Vector2 #2 for two dimensional


def Game_Loop():
    HEIGHT = 450 #sets the size of the screen 
    WIDTH = 400 #sets the size of the screen
    ACC = 0.5  #sets the variable of  
    FRIC = -0.12 #sets the Friction as a variable
    FPS = 60 #sets the frames per second

    FramePerSec = pygame.time.Clock() #sets up the clock

    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT)) #sets up the surface that the game is played on
    pygame.display.set_caption("Platformer game") #sets up the name of the window the game is played on

    #----------------------------------------------------------------------------------#
    #class for player 1

    class Player1(pygame.sprite.Sprite): #this is the over all class for all of the player 1 things this also sets up the sprite of the player
        def __init__(self):
            super().__init__() #this starts up the spite
            #self.image = pygame.image.load("character.png")  #Im not useing this at the moment but i might
            self.surf = pygame.Surface((30, 30))#tells where on the surface it is
            self.surf.fill((8,126,139)) #changes the colour of the sptite
            self.rect = self.surf.get_rect() #makes it a rectangle
    
            self.pos = vec((390, 360)) #X and Y cords of the player at the start 
            self.vel = vec(0,0) #sets the velsoity of the player moving
            self.acc = vec(0.5,0) #sets the acceleration
            self.jumping = False #sets up the jumping
            self.score = 0       #Sets the score of zero at the start of the game

        def move(self):
            self.acc = vec(0,0.5) #sets how fast the player can move
    
            pressed_keys = pygame.key.get_pressed() #this checks if the keys are presed to move
                
            if pressed_keys[K_LEFT]: #this means if the left button is clicked it will do the code
                self.acc.x = -ACC
            if pressed_keys[K_RIGHT]: #This means if the Right button is cliked it will do the 
                self.acc.x = ACC
                    
            self.acc.x += self.vel.x * FRIC 
            self.vel += self.acc
            self.pos += self.vel + 0.5 * self.acc
            
            if self.pos.x > WIDTH:
                self.pos.x = 0
            if self.pos.x < 0:
                self.pos.x = WIDTH
                
            self.rect.midbottom = self.pos

        def jump(self): #sets up what a jump is
            hits = pygame.sprite.spritecollide(self, platforms, False)
            if hits and not self.jumping:
                self.jumping = True 
                self.vel.y = -17

        def cancel_jump(self): #sets up  cancel jump 
            if self.jumping:
                if self.vel.y < -3:
                    self.vel.y = -3

        def update(self): #sets up points system for player one
            hits = pygame.sprite.spritecollide(self ,platforms, False) #sets up what a collision is
            if self.vel.y > 0:        
                if hits:
                    if self.pos.y < hits[0].rect.bottom:
                        if hits[0].point == True:   ##
                            hits[0].point = False   ##
                            self.score += 1         ##                
                        self.pos.y = hits[0].rect.top +1
                        self.vel.y = 0
                        self.jumping = False



    #----------------------------------------------------------------------------------------------------------#

    #class for player 2

    class Player2(pygame.sprite.Sprite): #this is the over all class for all of the player 2 things this also sets up the sprite of the player
        def __init__(self):
            super().__init__() #this starts up the spite
            #self.image = pygame.image.load("character.png")  #Im not useing this at the moment but i might
            self.surf = pygame.Surface((30, 30))#tells where on the surface it is
            self.surf.fill((231,90,124)) #changes the colour of the sptite
            self.rect = self.surf.get_rect() #makes it a rectangle
    
            self.pos = vec((10, 360)) #X and Y cords of the player at the start 
            self.vel = vec(0,0) #sets the velsoity of the player moving
            self.acc = vec(0.5,0) #sets the acceleration
            self.jumping = False #sets up the jumping
            self.score = 0       #Sets the score of zero at the start of the game

        def move(self):
            self.acc = vec(0,0.5)
    
            pressed_keys = pygame.key.get_pressed() #this checks if the keys are presed to move
                
            if pressed_keys[K_a]: #this means if the left button is clicked it will do the code
                self.acc.x = -ACC
            if pressed_keys[K_d]: #This means if the Right button is cliked it will do the 
                self.acc.x = ACC
                    
            self.acc.x += self.vel.x * FRIC
            self.vel += self.acc
            self.pos += self.vel + 0.5 * self.acc
            
            if self.pos.x > WIDTH:
                self.pos.x = 0
            if self.pos.x < 0:
                self.pos.x = WIDTH
                
            self.rect.midbottom = self.pos

        def jump(self): 
            hits = pygame.sprite.spritecollide(self, platforms, False)
            if hits and not self.jumping:
                self.jumping = True 
                self.vel.y = -17

        def cancel_jump(self):
            if self.jumping:
                if self.vel.y < -3:
                    self.vel.y = -3

        def update(self): #sets up points system for player two
            hits = pygame.sprite.spritecollide(self ,platforms, False) #sets up what a collision is
            if self.vel.y > 0:        
                if hits:
                    if self.pos.y < hits[0].rect.bottom:
                        if hits[0].point == True:   ##
                            hits[0].point = False   ##
                            self.score += 1         ##                
                        self.pos.y = hits[0].rect.top +1
                        self.vel.y = 0
                        self.jumping = False
                        
    #-------------------------------------------------------------------------------#

    #class for the platforms

    class platform(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.surf = pygame.Surface((random.randint(50,100), 12))
            self.surf.fill((96,153,45)) #sets the colour of the main platform
            self.rect = self.surf.get_rect(center = (random.randint(0,WIDTH-10), random.randint(0, HEIGHT-30))) # sets how big the platforms can be
            self.point = True #alows platfoms to count for points
            self.speed = random.randint(-1, 3) #this sets the speed of the platforms to ramdom between -1 and 3
            self.moving = True #alows the platforms to move
    
        def move(self): #code for platform movment
            if self.moving == True:  
                self.rect.move_ip(self.speed,0)
                if self.speed > 0 and self.rect.left > WIDTH:
                    self.rect.right = 0
                if self.speed < 0 and self.rect.right < 0:
                    self.rect.left = WIDTH

    def check(platform, groupies):
        if pygame.sprite.spritecollideany(platform,groupies):
            return True
        else:
            for entity in groupies:
                if entity == platform:
                    continue
                if (abs(platform.rect.top - entity.rect.bottom) < 40) and (abs(platform.rect.bottom - entity.rect.top) < 40):
                    return True
            C = False

    def plat_gen():
        while len(platforms) < 6:
            width = random.randrange(50,100)
            p  = platform()      
            C = True
            
            while C:
                p = platform()
                p.rect.center = (random.randrange(0, WIDTH - width),
                                random.randrange(-50, 0))
                C = check(p, platforms)
            platforms.add(p)
            all_sprites.add(p)


    #------------------------------------------------------------------------------------#
    #sets up the varibles that are used in the games

    #PT1 is the main platform that the player spawns on
        
    PT1 = platform() #sets PT1 as a platform class 
    PT1.point = False #stops the main platform from giving you points 
    P1 = Player1() #sets player 1 as the player class
    P2 = Player2() # sets up player 2 as the player 2 class

    #-------------------------------------------------------------------------------#
    #sets up the main platform that the players spawn on
    PT1.surf = pygame.Surface((WIDTH, 20))
    PT1.surf.fill((251,176,45)) #this sets the colour of the main platform
    PT1.rect = PT1.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))
    PT1.moving = False #this stops the main bottom platfor form moving

    #-----------------------------------------------------------------------------#


    #sets up
    all_sprites = pygame.sprite.Group()
    all_sprites.add(PT1)
    all_sprites.add(P1)
    all_sprites.add(P2)

    platforms = pygame.sprite.Group()
    platforms.add(PT1)

    #------------------------------------------------------------------------------#
    #Sets up platform genration

    for x in range(random.randint(4,19)):
        C = True
        pl = platform()
        while C:
            pl = platform()
            C = check(pl, platforms)
        platforms.add(pl)
        all_sprites.add(pl)


    #-------------------------------------------------------------------------------#
    #text based code
    def text_objects(text, font):
        textSurface = font.render(text, True, (0,0,0))
        return textSurface, textSurface.get_rect()

    def message_display(text):
        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((WIDTH/2),(HEIGHT/2))
        displaysurface.blit(TextSurf, TextRect) 


    #---------------------------------------------------------------------------------#
    #game loop



    while True:
        P1.update() #updates the player class for player one that we defined before
        P2.update() #updates the player class for player two that we defined before

        for event in pygame.event.get(): #gets all the events of the python game e.g. If a button is clicked
            if event.type == QUIT: #sets up the quit feature
                pygame.quit() #ends the pygame task
                sys.exit() #ends the window
    #------------------------------------------------------------------------------------------#
    #sets up the jump and cancel jump for both of the players
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_ESCAPE:
                    pygame.quit() #ends the pygame task
                    sys.exit() #ends the window
                if event.key == pygame.K_UP:
                    P1.jump()
                if event.key == pygame.K_w:
                    P2.jump()

            if event.type == pygame.KEYUP:    
                if event.key == pygame.K_UP: #if the up key is presed
                    P1.cancel_jump()  #runs the cancel jump feature that was defined before
                if event.key == pygame.K_w: #if the w key is presed
                    P2.cancel_jump()  #runs the cancel jump feature that was defined before

    #----------------------------------------------------------------------------------------#
    #sets up for the players to die and what happens for both players

            if P1.rect.top > HEIGHT: #Sets it up for if player one dies
                for entity in all_sprites: #gets all the sprites on the screen 
                    entity.kill() #kills all the sprites one the screenw
                    pygame.time.delay(5) #how long it waits before doing anything
                    displaysurface.fill((8,126,139)) #Is the colour of the death screen
                    message_display('Blue has won')
                    pygame.display.update() #updates the display
                    #how long winner screen stays on screen 
                    Game_Loop()

            if P2.rect.top > HEIGHT: #sets it up for if player two dies
                for entity in all_sprites: #gets all the sprites on the screen 
                    entity.kill() #kills all the sprites one the screenw
                    pygame.time.delay(5) #how long it waits before doing anything
                    displaysurface.fill((8,126,139)) #Is the colour of the death screen
                    message_display('Blue has won')
                    pygame.display.update() #updates the display
                    #how long winner screen stays on screen 
                    Game_Loop()
            
    #--------------------------------------------------------------------------------#

    #sets up the platform being getting rid of its self

        if P1.rect.top <= HEIGHT / 3: 
            P1.pos.y += abs(P1.vel.y)
            for plat in platforms:
                plat.rect.y += abs(P1.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()

        if P2.rect.top <= HEIGHT / 3:
            P2.pos.y += abs(P2.vel.y)
            for plat in platforms:
                plat.rect.y += abs(P2.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()
    #--------------------------------------------------------------------------------#
        plat_gen() #runs the platform gen code
        displaysurface.fill((39,39,39)) #the colour of the main surface that the game is played on

        #sets up the points system for player 1
        f = pygame.font.SysFont("Verdana", 20)     #sets the font and size
        g  = f.render(str(P1.score), True, (8,126,139))   #Sets up the points system that can go u
        displaysurface.blit(g, (WIDTH/1.25, 10))   #sets up the placement of the text

        #sets up the points system for player 2
        f = pygame.font.SysFont("Verdana", 20)     #sets the font and size
        j  = f.render(str(P2.score), True, (231,90,124))   #Sets up the points system that can go u
        displaysurface.blit(j, (WIDTH/5, 10))   #sets up the placement of the text
        
        for entity in all_sprites:
            displaysurface.blit(entity.surf, entity.rect)
            entity.move()


        pygame.display.update()
        FramePerSec.tick(FPS)


Game_Loop()





