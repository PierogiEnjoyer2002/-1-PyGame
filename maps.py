import pygame
from utils import load_image


def load_image_scaled(image_path, scale_factor):
    image = load_image(image_path)
    width = int(image.get_width() * scale_factor)
    height = int(image.get_height() * scale_factor)
    return pygame.transform.scale(image, (width, height))


class Maps:
    def __init__(self):
        self.maps = [
            {
                "name": "Space Battle",
                "background": "space-background.png",
                "platforms": [
                    {"type": "hard-space-platform", "pos": (0.2, 0.85)},
                    {"type": "hard-space-platform", "pos": (0.3, 0.7)},
                    {"type": "hard-space-platform", "pos": (0.4, 0.55)},
                    {"type": "hard-space-platform", "pos": (0.8, 0.4)},
                    {"type": "hard-space-platform", "pos": (0.8, 0.85)},
                    {"type": "hard-space-platform", "pos": (0.7, 0.7)},
                    {"type": "hard-space-platform", "pos": (0.6, 0.55)},
                    {"type": "hard-space-platform", "pos": (0.2, 0.4)},
                    {"type": "hard-space-platform", "pos": (0.1, 0.25)},
                    {"type": "hard-space-platform", "pos": (0.9, 0.25)},
                ]
            },
            {
                "name": "Space Arena",
                "background": "space-background.png",
                "platforms": [
                    {"type": "hard-space-platform", "pos": (0.25, 0.85)},
                    {"type": "hard-space-platform", "pos": (0.75, 0.85)},
                    {"type": "hard-space-platform", "pos": (0.35, 0.7)},
                    {"type": "hard-space-platform", "pos": (0.65, 0.7)},
                    {"type": "hard-space-platform", "pos": (0.45, 0.55)},
                    {"type": "hard-space-platform", "pos": (0.55, 0.55)},
                    {"type": "hard-space-platform", "pos": (0.55, 0.4)},
                    {"type": "hard-space-platform", "pos": (0.45, 0.4)},
                    {"type": "hard-space-platform", "pos": (0.1, 0.25)},
                    {"type": "hard-space-platform", "pos": (0.9, 0.25)},
                ]
            },
            {
                "name": "Vulcanic Clash",
                "background": "vulcanic-background.png",
                "platforms": [
                    {"type": "hard-vulcanic-platform", "pos": (0.2, 0.9)},
                    {"type": "hard-vulcanic-platform", "pos": (0.8, 0.9)},
                    {"type": "hard-vulcanic-platform", "pos": (0.4, 0.8)},
                    {"type": "hard-vulcanic-platform", "pos": (0.6, 0.8)},
                    {"type": "hard-vulcanic-platform", "pos": (0.3, 0.7)},
                    {"type": "hard-vulcanic-platform", "pos": (0.7, 0.7)},
                    {"type": "hard-vulcanic-platform", "pos": (0.5, 0.6)},
                    {"type": "hard-vulcanic-platform", "pos": (0.5, 0.4)},
                    {"type": "hard-vulcanic-platform", "pos": (0.1, 0.25)},
                    {"type": "hard-vulcanic-platform", "pos": (0.9, 0.25)},
                ]
            },
            {
                "name": "Vulcanic Field",
                "background": "vulcanic-background.png",
                "platforms": [
                    {"type": "hard-vulcanic-platform", "pos": (0.2, 0.85)},
                    {"type": "hard-vulcanic-platform", "pos": (0.8, 0.85)},
                    {"type": "hard-vulcanic-platform", "pos": (0.3, 0.75)},
                    {"type": "hard-vulcanic-platform", "pos": (0.7, 0.75)},
                    {"type": "hard-vulcanic-platform", "pos": (0.4, 0.65)},
                    {"type": "hard-vulcanic-platform", "pos": (0.6, 0.65)},
                    {"type": "hard-vulcanic-platform", "pos": (0.5, 0.55)},
                    {"type": "hard-vulcanic-platform", "pos": (0.5, 0.45)},
                    {"type": "hard-vulcanic-platform", "pos": (0.1, 0.25)},
                    {"type": "hard-vulcanic-platform", "pos": (0.9, 0.25)},
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

        # Pobierz aktualne wymiary okna
        window_width, window_height = pygame.display.get_surface().get_size()
        center_x = window_width / 2

        for platform in selected_map["platforms"]:
            # Załadowanie i przeskalowanie obrazu platformy
            platform_image = load_image_scaled(f'{platform["type"]}.png', 0.2)  # Przykładowy współczynnik skalowania
            platform_rect = platform_image.get_rect()

            # Przeskaluj współrzędne platformy do rozmiaru okna, uwzględniając symetrię względem środka
            platform_pos = (center_x + (platform["pos"][0] - 0.5) * window_width - platform_rect.width / 2,
                            platform["pos"][1] * window_height - platform_rect.height / 2)

            # Sprawdź, czy platforma mieści się w oknie i dostosuj pozycję, jeśli to konieczne
            if platform_pos[0] < 0:
                platform_pos = (0, platform_pos[1])
            elif platform_pos[0] + platform_rect.width > window_width:
                platform_pos = (window_width - platform_rect.width, platform_pos[1])

            if platform_pos[1] < 0:
                platform_pos = (platform_pos[0], 0)
            elif platform_pos[1] + platform_rect.height > window_height:
                platform_pos = (platform_pos[0], window_height - platform_rect.height)

            platform_rect.topleft = platform_pos
            screen.blit(platform_image, platform_rect)