import pygame
import random
import os

################################################################
# all_files
game_icon = 'pp.jpg'
background_image = "trump.jpg"
platform_icon = "platform.jfif"
player_image = "serega.gif" 
bot_image = "haha.jpg"
two_ebatan = "brus_li.jpg"
# Music
pygame.mixer.init()
pygame.mixer.music.load('kachok.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play()
# Name
def generate_arabic_characters(length=200):
    arabic_characters = [chr(i) for i in range(0x0600, 0x06FF)]
    return ''.join(random.choice(arabic_characters) for _ in range(length))

arabic_string = generate_arabic_characters()
###############################################################

sound_jump = pygame.mixer.Sound('cum_cut.mp3')
screen_width = 1920
screen_height = 1080
FPS = 70
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(arabic_string)
my_icon = pygame.image.load(game_icon)
pygame.display.set_icon(my_icon)
pygame.init()
pygame.mixer.init()

# Colors
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 255, 255)

# Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(player_image).convert_alpha()  
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = screen_height - 150  
        self.velocity_y = 0
        self.on_ground = False
        self.speed = 5
        self.health = 100

    def update(self):
        self.rect.y += self.velocity_y

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > screen_width - self.rect.width:
            self.rect.x = screen_width - self.rect.width

        if not self.on_ground:
            self.velocity_y += 1

    def jump(self):
        if self.on_ground:
            self.velocity_y = -20

    def reset(self):
        self.rect.x = 100
        self.rect.y = screen_height - 100

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(two_ebatan).convert_alpha()  
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = screen_height - 150  
        self.velocity_y = 0
        self.on_ground = False
        self.speed = 5
        self.health = 50

    def update(self):
        self.rect.y += self.velocity_y

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > screen_width - self.rect.width:
            self.rect.x = screen_width - self.rect.width

        if not self.on_ground:
            self.velocity_y += 1

    def jump(self):
        if self.on_ground:
            self.velocity_y = -20

    def reset(self):
        self.rect.x = 100
        self.rect.y = screen_height - 100

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load(platform_icon).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Bot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(bot_image).convert_alpha()  
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(0, screen_height - 100)
        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > screen_width or self.rect.x < 0:
            self.speed = -self.speed

try:
    background = pygame.image.load(background_image).convert()
except pygame.error as e:
    print(f"Failed to load background:  {e}")
    pygame.quit()
    exit()
background = pygame.transform.scale(background, (screen_width, screen_height))

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
bots = pygame.sprite.Group()

player = Player()
player2 = Player2()
all_sprites.add(player, player2)

ground = Platform(0, screen_height - 50, screen_width, 50)
platforms.add(ground)
all_sprites.add(ground)

for _ in range(10):
    p_width = random.randint(50, 150)
    p_height = 20
    p_x = random.randint(0, screen_width - p_width)
    p_y = random.randint(0, screen_height - 100)
    platform = Platform(p_x, p_y, p_width, p_height)
    platforms.add(platform)
    all_sprites.add(platform)

for _ in range(9):  
    bot = Bot()
    bots.add(bot)
    all_sprites.add(bot)

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
                sound_jump.set_volume(1)
                sound_jump.play()
            if event.key == pygame.K_UP:
                player2.jump()
                
    all_sprites.update()

    player.on_ground = False
    for platform in platforms:
        if player.rect.colliderect(platform.rect) and player.velocity_y >= 0:
            player.rect.bottom = platform.rect.top
            player.velocity_y = 0
            player.on_ground = True
    player2.on_ground = False
    for platform in platforms:
        if player2.rect.colliderect(platform.rect) and player2.velocity_y >= 0:
            player2.rect.bottom = platform.rect.top
            player2.velocity_y = 0
            player2.on_ground = True

    for bot in bots:
        if player.rect.colliderect(bot.rect):
            player.health -= 10
            player.rect.x -= 20  
        if player2.rect.colliderect(bot.rect):
            player2.health -= 10
            player2.rect.x += 20  

    screen.blit(background, (0, 0))
    all_sprites.draw(screen)

    font = pygame.font.Font(None, 36)
    health_text = font.render(f'Player 1 Health: {player.health}', True, WHITE)
    screen.blit(health_text, (10, 10))
    health_text2 = font.render(f'Player 2 Health: {player2.health}', True, WHITE)
    screen.blit(health_text2, (10, 50))

    pygame.display.update()
pygame.quit()