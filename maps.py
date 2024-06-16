import pygame
from utils import load_image

class Maps:
    def __init__(self):
        self.maps = [
            {
                "name": "Space Battle",
                "background": "space-background.png",
                "platforms": [
                    {"type": "hard-space-platform", "pos": (100, 400)},
                    {"type": "soft-space-platform", "pos": (300, 300)},
                    {"type": "hard-space-platform", "pos": (500, 200)},
                    {"type": "soft-space-platform", "pos": (700, 100)},
                    {"type": "hard-space-platform", "pos": (200, 500)},
                    {"type": "hard-space-platform", "pos": (400, 400)},
                    {"type": "soft-space-platform", "pos": (600, 300)},
                    {"type": "hard-space-platform", "pos": (800, 400)},
                    {"type": "soft-space-platform", "pos": (1000, 300)},
                    {"type": "hard-space-platform", "pos": (1200, 200)}
                ]
            },
            {
                "name": "Space Arena",
                "background": "space-background.png",
                "platforms": [
                    {"type": "hard-space-platform", "pos": (150, 450)},
                    {"type": "soft-space-platform", "pos": (350, 350)},
                    {"type": "hard-space-platform", "pos": (550, 450)},
                    {"type": "soft-space-platform", "pos": (750, 350)},
                    {"type": "hard-space-platform", "pos": (200, 550)},
                    {"type": "soft-space-platform", "pos": (400, 450)},
                    {"type": "hard-space-platform", "pos": (600, 350)},
                    {"type": "soft-space-platform", "pos": (800, 250)},
                    {"type": "hard-space-platform", "pos": (1000, 350)},
                    {"type": "soft-space-platform", "pos": (1200, 450)}
                ]
            },
            {
                "name": "Vulcanic Clash",
                "background": "vulcanic-background.png",
                "platforms": [
                    {"type": "hard-vulcanic-platform", "pos": (100, 400)},
                    {"type": "soft-vulcanic-platform", "pos": (300, 300)},
                    {"type": "hard-vulcanic-platform", "pos": (500, 200)},
                    {"type": "soft-vulcanic-platform", "pos": (700, 100)},
                    {"type": "hard-vulcanic-platform", "pos": (200, 500)},
                    {"type": "hard-vulcanic-platform", "pos": (400, 400)},
                    {"type": "soft-vulcanic-platform", "pos": (600, 300)},
                    {"type": "hard-vulcanic-platform", "pos": (800, 400)},
                    {"type": "soft-vulcanic-platform", "pos": (1000, 300)},
                    {"type": "hard-vulcanic-platform", "pos": (1200, 200)}
                ]
            },
            {
                "name": "Vulcanic Field",
                "background": "vulcanic-background.png",
                "platforms": [
                    {"type": "hard-vulcanic-platform", "pos": (150, 450)},
                    {"type": "soft-vulcanic-platform", "pos": (350, 350)},
                    {"type": "hard-vulcanic-platform", "pos": (550, 450)},
                    {"type": "soft-vulcanic-platform", "pos": (750, 350)},
                    {"type": "hard-vulcanic-platform", "pos": (200, 550)},
                    {"type": "soft-vulcanic-platform", "pos": (400, 450)},
                    {"type": "hard-vulcanic-platform", "pos": (600, 350)},
                    {"type": "soft-vulcanic-platform", "pos": (800, 250)},
                    {"type": "hard-vulcanic-platform", "pos": (1000, 350)},
                    {"type": "soft-vulcanic-platform", "pos": (1200, 450)}
                ]
            }
        ]
        self.selected_map_index = 0

    def select_map(self, index):
        if 0 <= index < len(self.maps):
            self.selected_map_index = index

    def draw(self, screen):
        selected_map = self.maps[self.selected_map_index]
        background = load_image(selected_map["background"])
        screen.blit(background, (0, 0))
        for platform in selected_map["platforms"]:
            platform_image = load_image(f'{platform["type"]}.png')
            screen.blit(platform_image, platform["pos"])
