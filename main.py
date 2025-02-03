import pygame 
import random 
import time 

pygame.init()

WIDTH = 900 
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH,HEIGHT))

def losers():
    bg = pygame.image.load("bground.png")
    bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))
    screen.blit(bg,(0,0))

class Bin(pygame.sprite.Sprite):
    def __init__ (self):
        super().__init__()
        self.image = pygame.image.load("bin.png")
        self.image = pygame.transform.scale(self.image,(40,60))
        self.rect = self.image.get_rect()

class Recycle(pygame.sprite.Sprite):
    def __init__(self,img):
        super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect= self.image.get_rect()

class Non_recyclabe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("plastic.png")
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()

item_list = pygame.sprite.Group()
plastic_list = pygame.sprite.Group()
allsprites = pygame.sprite.Group()

bin = Bin()
allsprites.add(bin)

images = ["item1.png","item2.png","item3.png"]

for i in range(50):
    item = Recycle(random.choice(images))

    item.rect.x = random.randrange(WIDTH)
    item.rect.y = random.randrange(HEIGHT)

    item_list.add(item)
    allsprites.add(item)

for i in range(20):
    plastic = Non_recyclabe()

    plastic.rect.x = random.randrange(WIDTH)
    plastic.rect.y = random.randrange(HEIGHT)

    plastic_list.add(plastic)
    allsprites.add(plastic)

WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)
playing= True
score = 0

clock = pygame.time.Clock()
start_time = time.time()

myFont = pygame.font.SysFont("times New Roman",22)
text= myFont.render("Score =" + str(0), True, BLACK)


while playing:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    time_elapsed = time.time()-start_time
    if time_elapsed >= 60:
        if score >= 20:
            screen.fill('green')
            text = myFont.render("bin loot successful", True,RED)
        else:
            screen.fill('red')
            text = myFont.render("bin loot unsuccessful",True, "green")
        screen.blit(text,(250,50))
    else:
        losers() 
        countDown = myFont.render("time Left:" + str(60 - int(time_elapsed)),True, WHITE)
        screen.blit(countDown,(20,10))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if bin.rect.y >0:
                bin.rect.y -= 5
        if keys[pygame.K_DOWN]:
            if bin.rect.y <700:
                bin.rect.y +=5 
        if keys[pygame.K_LEFT]:
            if bin.rect.y>0:
                bin.rect.x -=5 
        if keys[pygame.K_RIGHT]:
            if bin.rect.y <900:
                bin.rect.x +=5
        item_hit_list = pygame.sprite.spritecollide(bin, item_list,True)
        plastic_hit_list = pygame.sprite.spritecollide(bin, plastic_list,True)
        for item in item_hit_list:
            score += 1 
            text = myFont.render("score = "+ str(score),True, WHITE)
        for plastic in plastic_hit_list:
            score -= 5 
            text = myFont.render("score = "+ str(score),True,WHITE)
    screen.blit(text,(20,50))
    allsprites.draw(screen)
    pygame.display.update()

pygame.quit()


while playing:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
