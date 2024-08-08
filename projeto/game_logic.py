import pygame

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player_pos = [width // 2, height // 2]
        self.player_speed = 5

    def handle_event(self, event):
        # Lógica para manipular eventos
        pass

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_pos[0] -= self.player_speed
        if keys[pygame.K_RIGHT]:
            self.player_pos[0] += self.player_speed
        if keys[pygame.K_UP]:
            self.player_pos[1] -= self.player_speed
        if keys[pygame.K_DOWN]:
            self.player_pos[1] += self.player_speed

    def get_player_position(self):
        return self.player_pos
