import pygame
from sys import exit
from random import randint

pygame.init()
screen = pygame.display.set_mode((1000, 700))
clock = pygame.time.Clock()
screen.fill('black')

class Tiles(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((64,64))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x,y))

    def animation(self):
        if self.rect.y >= 0:
            self.rect.y -= 5
        else:
            self.kill()

    def update(self):
        self.animation()

class Dancer(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        mood = randint(0, 4)
        self.life = randint(1000,1800)
        self.x = x
        self.y = y
        balance1 = pygame.image.load('sprites/Balancing/balancing1.png').convert_alpha()
        balance1 = pygame.transform.scale(balance1, (200, 200))
        balance2 = pygame.image.load('sprites/Balancing/balancing2.png').convert_alpha()
        balance2 = pygame.transform.scale(balance2, (200, 200))
        balance3 = pygame.image.load('sprites/Balancing/balancing3.png').convert_alpha()
        balance3 = pygame.transform.scale(balance3, (200, 200))
        balance4 = pygame.image.load('sprites/Balancing/balancing4.png').convert_alpha()
        balance4 = pygame.transform.scale(balance4, (200, 200))
        balance5 = pygame.image.load('sprites/Balancing/balancing5.png').convert_alpha()
        balance5 = pygame.transform.scale(balance5, (200, 200))
        balance6 = pygame.image.load('sprites/Balancing/balancing6.png').convert_alpha()
        balance6 = pygame.transform.scale(balance6, (200, 200))
        balance7 = pygame.image.load('sprites/Balancing/balancing7.png').convert_alpha()
        balance7 = pygame.transform.scale(balance7, (200, 200))
        balance8 = pygame.image.load('sprites/Balancing/balancing8.png').convert_alpha()
        balance8 = pygame.transform.scale(balance8, (200, 200))
        self.balancing_frames = [balance1, balance2, balance3, balance4, balance5, balance6, balance7, balance8]
        hip1 = pygame.image.load('sprites/hips/hips1.png').convert_alpha()
        hip1 = pygame.transform.scale(hip1, (200, 200))
        hip2 = pygame.image.load('sprites/hips/hips2.png').convert_alpha()
        hip2 = pygame.transform.scale(hip2, (200, 200))
        hip3 = pygame.image.load('sprites/hips/hips3.png').convert_alpha()
        hip3 = pygame.transform.scale(hip3, (200, 200))
        hip4 = pygame.image.load('sprites/hips/hips4.png').convert_alpha()
        hip4 = pygame.transform.scale(hip4, (200, 200))
        hip5 = pygame.image.load('sprites/hips/hips5.png').convert_alpha()
        hip5 = pygame.transform.scale(hip5, (200, 200))
        hip6 = pygame.image.load('sprites/hips/hips6.png').convert_alpha()
        hip6 = pygame.transform.scale(hip6, (200, 200))
        hip7 = pygame.image.load('sprites/hips/hips7.png').convert_alpha()
        hip7 = pygame.transform.scale(hip7, (200, 200))
        hip8 = pygame.image.load('sprites/hips/hips8.png').convert_alpha()
        hip8 = pygame.transform.scale(hip8, (200, 200))
        self.hip_frames = [hip1, hip2, hip3, hip4, hip5, hip6, hip7, hip8]
        skip1 = pygame.image.load('sprites/Skip/skip1.png').convert_alpha()
        skip1 = pygame.transform.scale(skip1, (200, 200))
        skip2 = pygame.image.load('sprites/Skip/skip2.png').convert_alpha()
        skip2 = pygame.transform.scale(skip2, (200, 200))
        skip3 = pygame.image.load('sprites/Skip/skip3.png').convert_alpha()
        skip3 = pygame.transform.scale(skip3, (200, 200))
        skip4 = pygame.image.load('sprites/Skip/skip4.png').convert_alpha()
        skip4 = pygame.transform.scale(skip4, (200, 200))
        skip5 = pygame.image.load('sprites/Skip/skip5.png').convert_alpha()
        skip5 = pygame.transform.scale(skip5, (200, 200))
        skip6 = pygame.image.load('sprites/Skip/skip6.png').convert_alpha()
        skip6 = pygame.transform.scale(skip6, (200, 200))
        skip7 = pygame.image.load('sprites/Skip/skip7.png').convert_alpha()
        skip7 = pygame.transform.scale(skip7, (200, 200))
        skip8 = pygame.image.load('sprites/Skip/skip8.png').convert_alpha()
        skip8 = pygame.transform.scale(skip8, (200, 200))
        self.skip_frames = [skip1, skip2, skip3, skip4, skip5, skip6, skip7, skip8]
        slide1 = pygame.image.load('sprites/slide/slide1.png').convert_alpha()
        slide1 = pygame.transform.scale(slide1, (200, 200))
        slide2 = pygame.image.load('sprites/slide/slide2.png').convert_alpha()
        slide2 = pygame.transform.scale(slide2, (200, 200))
        slide3 = pygame.image.load('sprites/slide/slide3.png').convert_alpha()
        slide3 = pygame.transform.scale(slide3, (200, 200))
        slide4 = pygame.image.load('sprites/slide/slide4.png').convert_alpha()
        slide4 = pygame.transform.scale(slide4, (200, 200))
        slide5 = pygame.image.load('sprites/slide/slide5.png').convert_alpha()
        slide5 = pygame.transform.scale(slide5, (200, 200))
        slide6 = pygame.image.load('sprites/slide/slide6.png').convert_alpha()
        slide6 = pygame.transform.scale(slide6, (200, 200))
        slide7 = pygame.image.load('sprites/slide/slide7.png').convert_alpha()
        slide7 = pygame.transform.scale(slide7, (200, 200))
        slide8 = pygame.image.load('sprites/slide/slide8.png').convert_alpha()
        slide8 = pygame.transform.scale(slide8, (200, 200))
        self.slide_frames = [slide1, slide2, slide3, slide4, slide5, slide6, slide7, slide8]
        snap1 = pygame.image.load('sprites/snap/snap1.png').convert_alpha()
        snap1 = pygame.transform.scale(snap1, (200, 200))
        snap2 = pygame.image.load('sprites/snap/snap2.png').convert_alpha()
        snap2 = pygame.transform.scale(snap2, (200, 200))
        snap3 = pygame.image.load('sprites/snap/snap3.png').convert_alpha()
        snap3 = pygame.transform.scale(snap3, (200, 200))
        snap4 = pygame.image.load('sprites/snap/snap4.png').convert_alpha()
        snap4 = pygame.transform.scale(snap4, (200, 200))
        snap5 = pygame.image.load('sprites/snap/snap5.png').convert_alpha()
        snap5 = pygame.transform.scale(snap5, (200, 200))
        snap6 = pygame.image.load('sprites/snap/snap6.png').convert_alpha()
        snap6 = pygame.transform.scale(snap6, (200, 200))
        snap7 = pygame.image.load('sprites/snap/snap7.png').convert_alpha()
        snap7 = pygame.transform.scale(snap7, (200, 200))
        snap8 = pygame.image.load('sprites/snap/snap8.png').convert_alpha()
        snap8 = pygame.transform.scale(snap8, (200, 200))
        self.snap_frames = [snap1, snap2, snap3, snap4, snap5, snap6, snap7, snap8]
        self.frames = [snap1, snap2, snap3, snap4, snap5, snap6, snap7, snap8]
        self.animation_index = 0
        if mood == 0:
            self.frames = [balance1, balance2, balance3, balance4, balance5, balance6, balance7, balance8]
        elif mood == 1:
            self.frames = [hip1, hip2, hip3, hip4, hip5, hip6, hip7, hip8]
        elif mood == 2:
            self.frames = [skip1, skip2, skip3, skip4, skip5, skip6, skip7, skip8]
        elif mood == 3:
            self.frames = [slide1, slide2, slide3, slide4, slide5, slide6, slide7, slide8]
        elif mood == 4:
            self.frames = [snap1, snap2, snap3, snap4, snap5, snap6, snap7, snap8]
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def animation(self):
        if self.life >= 1:
            self.life -= 1
        else: self.kill()
        self.animation_index += .1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation()

dancer = pygame.sprite.Group()
tiles = pygame.sprite.Group()
dancer_go = 25
x = 150
tile_drop = pygame.USEREVENT + 1
pygame.time.set_timer(tile_drop, 900)
bg_music = pygame.mixer.Sound('dreams.mp3')
bg_music.play(loops=-1)

while True:

    if dancer_go == 0:
        y = 375
        if x <= 860:
            x += 150
        else:
            x -= 750
        dancer.add(Dancer(x,y))
        dancer_go = randint(600,1300)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == tile_drop:
            x = randint(0,1000)
            y = randint(400,700)
            colorize = randint(0,6)
            color = 'red'
            if colorize == 0:
                color = 'blue'
            elif colorize == 1:
                color = 'green'
            elif colorize == 2:
                color = 'red'
            elif colorize == 3:
                color = 'orange'
            elif colorize == 4:
                color = 'sky blue'
            elif colorize == 5:
                color = 'yellow'
            tiles.add(Tiles(color,x,y))

    screen.fill('black')
    dancer.draw(screen)
    dancer.update()
    tiles.draw(screen)
    tiles.update()
    dancer_go -= 1

    pygame.display.update()
    clock.tick(60)