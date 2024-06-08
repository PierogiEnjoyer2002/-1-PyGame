import pygame
import sys


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

        # Get screen dimensions
        self.screen_width, self.screen_height = self.screen.get_size()

        # Load images
        self.background = pygame.image.load("assets/menu-background.png")
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))
        self.screenshots = [pygame.image.load(f"assets/map{i}.png") for i in range(1, 4)]
        self.current_screenshot = 0

        self.start_img = pygame.image.load("assets/start-button.png")
        self.controls_img = pygame.image.load("assets/controls-button.png")
        self.controls_overlay = pygame.image.load("assets/rage-crate.png")
        self.close_button = pygame.image.load("assets/rage-crate.png")
        self.volume_button = pygame.image.load("assets/rage-crate.png")

        self.controls_visible = False

    def draw_menu(self):
        self.screen.blit(self.background, (0, 0))  # Draw background

        # Draw screenshot
        screenshot_x = (self.screen_width - self.screenshots[self.current_screenshot].get_width()) // 2
        self.screen.blit(self.screenshots[self.current_screenshot], (screenshot_x, int(self.screen_height * 0.1)))

        # Draw buttons
        start_button_x = (self.screen_width - self.start_img.get_width()) // 2
        self.screen.blit(self.start_img, (start_button_x, int(self.screen_height * 0.8)))
        self.screen.blit(self.controls_img, (start_button_x, int(self.screen_height * 0.9)))
        self.screen.blit(self.volume_button, (int(self.screen_width * 0.9), int(self.screen_height * 0.05)))

        if self.controls_visible:
            controls_overlay_x = (self.screen_width - self.controls_overlay.get_width()) // 2
            self.screen.blit(self.controls_overlay, (controls_overlay_x, int(self.screen_height * 0.1)))
            self.screen.blit(self.close_button, (int(self.screen_width * 0.9), int(self.screen_height * 0.1)))

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.controls_visible:
                    if self.is_over_close_button(event.pos):
                        self.controls_visible = False
                else:
                    if self.is_over_start_button(event.pos):
                        return 'start'
                    elif self.is_over_controls_button(event.pos):
                        self.controls_visible = True
                    elif self.is_over_volume_button(event.pos):
                        self.change_volume()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.current_screenshot = (self.current_screenshot - 1) % len(self.screenshots)
        elif keys[pygame.K_RIGHT]:
            self.current_screenshot = (self.current_screenshot + 1) % len(self.screenshots)

    def is_over_start_button(self, pos):
        x, y = pos
        start_button_x = (self.screen_width - self.start_img.get_width()) // 2
        return start_button_x <= x <= start_button_x + self.start_img.get_width() and int(
            self.screen_height * 0.8) <= y <= int(self.screen_height * 0.8) + self.start_img.get_height()

    def is_over_controls_button(self, pos):
        x, y = pos
        controls_button_x = (self.screen_width - self.controls_img.get_width()) // 2
        return controls_button_x <= x <= controls_button_x + self.controls_img.get_width() and int(
            self.screen_height * 0.9) <= y <= int(self.screen_height * 0.9) + self.controls_img.get_height()

    def is_over_close_button(self, pos):
        x, y = pos
        return int(self.screen_width * 0.9) <= x <= int(
            self.screen_width * 0.9) + self.close_button.get_width() and int(self.screen_height * 0.1) <= y <= int(
            self.screen_height * 0.1) + self.close_button.get_height()

    def is_over_volume_button(self, pos):
        x, y = pos
        return int(self.screen_width * 0.9) <= x <= int(
            self.screen_width * 0.9) + self.volume_button.get_width() and int(self.screen_height * 0.05) <= y <= int(
            self.screen_height * 0.05) + self.volume_button.get_height()

    def change_volume(self):
        # Placeholder for volume change logic
        print("Volume button clicked")

    def run(self):
        while True:
            result = self.handle_events()
            self.draw_menu()
            self.clock.tick(30)
            if result == 'start':
                return result