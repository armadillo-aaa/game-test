import pygame
from objects import Player
from objects import Ball
from objects import Prize
from objects import Bullet
from random import randint

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)


pygame.mixer.music.load('sounds/bird.mp3')
pygame.mixer.music.play(-1)

s_catch = pygame.mixer.Sound('sounds/catch.ogg')

BLACK = (0, 0, 0)
W, H = 1000, 570

sc = pygame.display.set_mode((W, H))

bg = pygame.image.load('images/back1.jpg').convert()
score = pygame.image.load('images/score_fon.png').convert_alpha()

f = pygame.font.SysFont('arial', 30)

telega = pygame.image.load('images/telega.png').convert_alpha()
t_rect = telega.get_rect(centerx=W//2, bottom=H-5)

clock = pygame.time.Clock()
FPS = 60

balls_data = ({'path': 'ball_bear.png', 'score': 100, 'health': 100},
              {'path': 'ball_fox.png', 'score': 150, 'health': 150},
              {'path': 'ball_panda.png', 'score': 200, 'health': 200})

balls_surf = [pygame.image.load('images/'+data['path']).convert_alpha() for data in balls_data]

balls = pygame.sprite.Group()

prize_data = ({'path': 'ball_tiger.png', 'score': 10, 'value': 50},
              )

prize_surf = [pygame.image.load('images/'+data['path']).convert_alpha() for data in prize_data]

prizes = pygame.sprite.Group()

bullets_data = ({'path': 'ball_owl.png', 'damage': 50},
              )

bullets_surf = [pygame.image.load('images/'+data['path']).convert_alpha() for data in bullets_data]

bullets = pygame.sprite.Group()

def createBall(group):
    indx = randint(0, len(balls_surf)-1)
    x = randint(20, W-20)
    speedY = randint(1, 2)
    speedX = randint(-3, 3)

    return Ball(x, speedX, speedY, balls_surf[indx], balls_data[indx]['score'], balls_data[indx]['health'], group)

def createPrize(group, ball):
    indx = randint(0, len(prize_surf)-1)
    x = ball.rect.centerx
    y = ball.rect.centery
    speedX, speedY = ball.speedX, ball.speedY

    return Prize(x, y, speedX, speedY, prize_surf[indx], prize_data[indx]['score'], prize_data[indx]['value'], group)

bullet_speed = 1
def createBullet(group):
    indx = randint(0, len(bullets_surf)-1)
    x = t_rect.centerx
    y = t_rect.y
    global bullet_speed

    return Bullet(x+5, y, bullet_speed, bullets_surf[indx], bullets_data[indx]['damage'], group),\
           Bullet(x-5, y, bullet_speed, bullets_surf[indx], bullets_data[indx]['damage'], group)

game_score = 0

def collideBalls():
    global game_score
    for ball in balls:
        if t_rect.collidepoint(ball.rect.center):
            s_catch.play()
            game_score += ball.score
            ball.kill()

        for bullet in bullets:
            if ball.rect.collidepoint(bullet.rect.center):
                ball.health -= bullet.damage
                bullet.kill()
                s_catch.play()
                if ball.health <= 0:
                    game_score += ball.score
                    chance = randint(0, 10)
                    if chance <= 1:
                        createPrize(prizes, ball)
                    ball.kill()

def collidePrizes():
    global game_score
    for prize in prizes:
        if t_rect.collidepoint(prize.rect.center):
            s_catch.play()
            game_score += prize.score
            global bullet_speed
            bullet_speed += 1
            prize.kill()

# createBall(balls)

# createBullet(bullets)

speed = 10
ready_to_fire = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createBall(balls)
        elif event.type == pygame.USEREVENT + 1:
            ready_to_fire = True

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        t_rect.x -= speed
        if t_rect.x < 0:
            t_rect.x = 0
    elif keys[pygame.K_RIGHT]:
        t_rect.x += speed
        if t_rect.x > W-t_rect.width:
            t_rect.x = W-t_rect.width
    elif keys[pygame.K_SPACE]:
        if ready_to_fire is True:
            createBullet(bullets)
            ready_to_fire = False
            pygame.time.set_timer(pygame.USEREVENT+1, 300)


    collideBalls()
    collidePrizes()

    sc.blit(bg, (0, 0))
    balls.draw(sc)
    prizes.draw(sc)
    bullets.draw(sc)
    sc.blit(score, (0, 0))
    sc_text = f.render(str(game_score), 1, (94, 138, 14))
    sc.blit(sc_text, (20, 10))
    sc.blit(telega, t_rect)
    pygame.display.update()

    clock.tick(FPS)

    balls.update(H,W)
    prizes.update(H, W)
    bullets.update(H)
