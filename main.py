import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    screen_middle = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]
    # spawn player in the middle of the screen
    player= Player(screen_middle[0], screen_middle[1], PLAYER_RADIUS)
    
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        
        pygame.display.flip()
        
        clock.tick(60)
        
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
