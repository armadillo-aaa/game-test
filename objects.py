import pygame

class Player(pygame.sprite.Sprite): #только начал переписывать. еще не подключил. надо разобраться с Git
    def __init__(self, x, y, speedX, speedY, surf, f_ratio, health):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, y))
        self.speedY = speedY
        self.speedX = speedX
        self.f_ratio = f_ratio
        self.health = health

    def update(self, *args):
        if self.rect.y < args[0] - 20:
            self.rect.y += self.speedY
            self.rect.x += self.speedX

        else:
            self.kill()

        if 0 < self.rect.x < args[1] - 40:
            pass
        else:
            self.speedX = -self.speedX



class Ball(pygame.sprite.Sprite):
    def __init__(self, x, speedX, speedY, surf, score, health, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 0))
        self.speedY = speedY
        self.speedX = speedX
        self.score = score
        self.health = health
        self.add(group)

    def update(self, *args):
        if self.rect.y < args[0] - 20:
            self.rect.y += self.speedY
            self.rect.x += self.speedX

        else:
            self.kill()

        if 0 < self.rect.x < args[1] - 40:
            pass
        else:
            self.speedX = -self.speedX

class Prize(pygame.sprite.Sprite):
    def __init__(self, x, y, speedX, speedY, surf, score, value, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, y))
        self.speedY = speedY
        self.speedX = speedX
        self.score = score
        self.value = value
        self.add(group)

    def update(self, *args):
        if self.rect.y < args[0] - 20:
            self.rect.y += self.speedY
            self.rect.x += self.speedX

        else:
            self.kill()

        if 0 < self.rect.x < args[1] - 40:
            pass
        else:
            self.speedX = -self.speedX

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, surf, damage, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.damage = damage
        self.add(group)

    def update(self, *args):
        if self.rect.y > 0:
            self.rect.y -= self.speed
        else:
            self.kill()
