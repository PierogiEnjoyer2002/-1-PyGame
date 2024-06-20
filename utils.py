import pygame

def load_image(name):
    return pygame.image.load(f"assets/images/{name}").convert_alpha()

def load_image_scaled(image_path, scale_factor):
    image = load_image(image_path)
    width = int(image.get_width() * scale_factor)
    height = int(image.get_height() * scale_factor)
    return pygame.transform.scale(image, (width, height))