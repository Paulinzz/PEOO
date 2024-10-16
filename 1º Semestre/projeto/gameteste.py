import pygame
from game_logic import Game
from graphics import Renderer

def main():
    # Inicializa o Pygame
    pygame.init()

    # Configurações da tela
    screen_width, screen_height = 1800,800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Mystic Quest")

    # Inicializa o jogo e o renderizador
    game = Game(screen_width, screen_height)
    renderer = Renderer(screen, game)

    clock = pygame.time.Clock()
    running = True

    # Loop principal do jogo
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Passa eventos para o jogo
            game.handle_event(event)

        # Atualiza o estado do jogo
        game.update()

        # Renderiza a tela
        renderer.render()

        # Controla a taxa de quadros
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
