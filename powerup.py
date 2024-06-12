import pygame
import random

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, name):
        super().__init__()
        #wizaulizacja powerup
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.name = name

    def update(self, player):
        #Sprawdza nazwe powerupu i go aktywuje u gracza
        if self.rect.colliderect(player.rect):
            if self.name == 'SHIELD':
                player.bonus_shield = True
            elif self.name == 'SPEED':
                player.bonus_speed = True
            elif self.name == 'DOUBLE_DAMAGE':
                player.bonus_double_damage = True
            self.kill()  # Usuwa power-up po zebraniu