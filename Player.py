import pygame, os, random

pygame.init()

class Player(pygame.sprite.Sprite):
    # konstruktor klasy
    def __init__(self, image, cx, cy, weapon_list):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = cx, cy
        self.level = None
        self.weapon_list = weapon_list
        self.weapon = self.weapon_list[0]
        self.lives = 7
        self.points = 0
        self.bonus_speed = False
        self.bonus_shield = False
        self.bonus_double_demage = False
        self.player_speed = 8
        self.bullet_speed = 12

    #rysowanie gracza i jego stanu na ekranie
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.weapon, [self.rect.centerx-self.weapon.get_rect().width//2, self.rect.centery+40])

    #poruszanie się za pomocą klawiszy
    def update(self, key_pressed):
            self.get_event(key_pressed)
            self._move(self.weapon_list, 3)

        # blokujmy wyjście poza ekran gry
        if self.rect.bottom > HEIGHT:
                self.rect.bottom = HEIGHT
        if self.rect.top < 0:
                self.rect.top = 0
        if self.rect.centerx < 0:
                self.rect.centerx = 0
        if self.rect.centerx > WIDTH:
                self.rect.centerx = WIDTH

        #sprawdzamy kolizje z bonusami
        for b in pygame.sprite.spritecollide(self, self.level.set_of_bonus, True):
            if b.name == 'SHIELD':
                self.bonus_shield = True
            elif b.name == 'SPEED':
                self.bonus_speed = True
            elif b.name == "2DMG"
                self.bonus_double_demage = True
            bonus.play()

        # sprawdzamy kolizję z pociskami
        if pygame.sprite.spritecollideany(self, self.level.set_of_bullets):
            if self.bonus_speed:
                self.bonus_speed = False
            else:
                self.lives -= 1
            lose.play()
            pygame.time.delay(200)
            self.level.set_of_meteors.empty()
            self.level.set_of_bonus.empty()