import pygame

class Renderer:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.player_color = (255, 255, 255)  # Cor do jogador

    def render(self):
        # Limpa a tela
        self.screen.fill((0, 0, 0))  # Fundo preto

        # Desenha o jogador
        player_pos = self.game.get_player_position()
        pygame.draw.rect(self.screen, self.player_color, (*player_pos, 50, 50))

        # Atualiza a tela
        pygame.display.flip()
