import pygame
import math


# Bullet class
class Bullet:
    def __init__(self, x, y, direction, speed=10, damage=10):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = speed
        self.damage = damage
        self.radius = 5  # for collision detection

    def update(self):
        self.x += self.speed * math.cos(self.direction)
        self.y += self.speed * math.sin(self.direction)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius)


# Laser class
class Laser(Bullet):
    def __init__(self, x, y, direction, speed=20, damage=25):
        super().__init__(x, y, direction, speed, damage)
        self.radius = 3

    def draw(self, screen):
        pygame.draw.line(screen, (255, 0, 0), (self.x, self.y),
                         (self.x + self.radius * math.cos(self.direction),
                          self.y + self.radius * math.sin(self.direction)), 2)


# Rocket class
class Rocket(Bullet):
    def __init__(self, x, y, direction, speed=5, damage=50, explosion_radius=50):
        super().__init__(x, y, direction, speed, damage)
        self.explosion_radius = explosion_radius

    def explode(self):
        # Placeholder for explosion logic
        print("Rocket exploded")

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 165, 0), (self.x, self.y, 10, 5))


# Weapon base class
class Weapon:
    def __init__(self, cooldown, bullet_type):
        self.cooldown = cooldown
        self.last_shot = 0
        self.bullet_type = bullet_type

    def can_shoot(self, current_time):
        return current_time - self.last_shot >= self.cooldown

    def shoot(self, x, y, direction, bullets, current_time):
        if self.can_shoot(current_time):
            bullets.append(self.bullet_type(x, y, direction))
            self.last_shot = current_time


# Pistol class
class Pistol(Weapon):
    def __init__(self):
        super().__init__(cooldown=500, bullet_type=Bullet)


# Rifle class
class Rifle(Weapon):
    def __init__(self):
        super().__init__(cooldown=300, bullet_type=Bullet)


# LaserGun class
class LaserGun(Weapon):
    def __init__(self):
        super().__init__(cooldown=700, bullet_type=Laser)


# Bazooka class
class Bazooka(Weapon):
    def __init__(self):
        super().__init__(cooldown=1500, bullet_type=Rocket)

    def shoot(self, x, y, direction, bullets, current_time):
        if self.can_shoot(current_time):
            rocket = self.bullet_type(x, y, direction)
            bullets.append(rocket)
            self.last_shot = current_time
            rocket.explode()


# DroppedWeapon class
class DroppedWeapon:
    def __init__(self, weapon_type, x, y):
        self.weapon_type = weapon_type
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.fall_speed = 5

    def update(self):
        self.y += self.fall_speed

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.width, self.height))