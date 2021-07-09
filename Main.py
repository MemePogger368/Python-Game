import math
import random
import pygame
import ctypes  # An included library with Python install.
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
Mbox('WARNING!', 'You are about to see the best code ever Give me Excellence or this happy face will turn upside down :D and i will steal all your bitcoin', 2)


RED = pygame.Color('red')
pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()
screen = pygame.display.set_mode((1280, 800))
rect = screen.get_rect()
clock = pygame.time.Clock()
pygame.display.set_caption("Broken ass Project")
width = 1280
height = 800

#background
BACKGROUND = pygame.Surface((5120, 4000))
BACKGROUND.fill((127, 69, 2))
BACKGROUND = pygame.image.load("child_eat_game/sprites/track.png").convert()
screen.blit(BACKGROUND,(0,0))
pygame.display.update()


#music
pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('child_eat_game\Wice.wav')
pygame.mixer.music.play(-1)

# Initialising and definitions
WHITE = pygame.Color('white')
VEHICLE1 = pygame.Surface((40, 70), pygame.SRCALPHA)
VEHICLE1.fill((130, 180, 20))
#blitting car onto 'rectangle car'
VEHICLE1 = pygame.image.load("child_eat_game/sprites/bulk_idle.png")
screen.blit(VEHICLE1,(0,0))
pygame.display.update()
eBall = []


pygame.display.update()
white = (255,255,255)
blue = (0,0,255)

size = 10
x_change = 0
accel_x = 0
max_speed = 6

BLACK = 0,0,0




class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)



class Lawsuit(Entity):
    
    
    def __init__(self, image, position):
        pass
        
        
        


class Barrier(object):
    pass


class Background(pygame.sprite.Sprite):

    def __init__(self, image, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(topleft=location)

class Player(Entity):

    def __init__(self):
        red = (255, 0, 0)
        move_x = 300
        move_y = 400
        self.rect = pygame.draw.rect(screen,red, (move_x, move_y, 10, 10))
        self.dist = 10



class VehicleSprite(Entity):
    MAX_FORWARD_SPEED = 15
    MAX_REVERSE_SPEED = 0
    ACCELERATION = 0.05
    TURN_SPEED = 0.000000000001

    def __init__(self, image, position):
        Entity.__init__(self)
        self.src_image = image
        self.image = image
        self.rect = self.image.get_rect(center=position)
        self.position = pygame.math.Vector2(position)
        self.velocity = pygame.math.Vector2(0, 0)
        self.speed = self.direction = 0
        self.k_left = self.k_right = self.k_down = self.k_up = 0

    def update(self, time):
        # SIMULATION
        self.speed += self.k_up + self.k_down
        # To clamp the speed.
        self.speed = max(-self.MAX_REVERSE_SPEED,min(self.speed, self.MAX_FORWARD_SPEED))
        # clamps to screen
        
        
        #slow down
        

        # Degrees sprite is facing (direction)
        self.direction += (self.k_right + self.k_left)
        rad = math.radians(self.direction)
        self.velocity.x = -self.speed*math.sin(rad)
        self.velocity.y = -self.speed*math.cos(rad)
        self.position += self.velocity
        self.image = pygame.transform.rotate(self.src_image, self.direction)
        self.rect = self.image.get_rect(center=self.position)





def game_loop():

    background = Background(BACKGROUND, [0, 0])
    bike = VehicleSprite(VEHICLE1, rect.center)

    bike_group = pygame.sprite.Group(bike)

    all_sprites = pygame.sprite.Group(bike_group)

    camera = pygame.math.Vector2(0, 0)
    done = False
    
    sides = ['top', 'bottom', 'left', 'right']
    weights = [width, width, height, height]


    while not done:
        
        time = clock.tick(60)

        side = random.choices(sides, weights)[0]

        if side == 'top':
            y = random.randrange(width-4)
            x = random.randrange(width-4)
        elif side == 'bottom':
            y = random.randrange(width-4)
            x = random.randrange(width-4)
        elif side == 'left':
            y = random.randrange(width-4)
            x = random.randrange(width-4)
        elif side == 'right':
            y = random.randrange(width-4)
            x = random.randrange(width-4)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                # Bike Input (Player 1)
                if event.key == pygame.K_d:
                    bike.k_right = -3
                elif event.key == pygame.K_a:
                    bike.k_left = 3
                elif event.key == pygame.K_w:
                    bike.k_up = 0.1
                elif event.key == pygame.K_s:
                    bike.k_down = -0.1
                elif event.key == pygame.K_SPACE:
                    bike.k_down = -0.5

                elif event.key == pygame.K_ESCAPE:
                    done = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    bike.k_right = 0
                elif event.key == pygame.K_a:
                    bike.k_left = 0
                elif event.key == pygame.K_w:
                    bike.k_up = -0.1
                elif event.key == pygame.K_s:
                    bike.k_down = 0
                elif event.key == pygame.K_SPACE:
                    bike.k_down = 0

        for i in range(len(eBall)):

            ball_rect = pygame.draw.circle(screen, blue, eBall[i], size)

            if bike.rect.colliderect(ball_rect):
                print("hit")


        camera -= bike.velocity

        all_sprites.update(time)

        screen.fill(BLACK)
        screen.blit(background.image, background.rect.topleft+camera)

        for sprite in all_sprites:
            screen.blit(sprite.image, sprite.rect.topleft+camera)
        pygame.draw.rect(screen, RED, (x, y, 4, 4))

        pygame.display.flip()



game_loop()
pygame.quit()
