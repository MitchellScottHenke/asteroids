import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # dt = 0
    screen_middle = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]
    
    # Creating my groups
    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    
    # spawn player in the middle of the screen, add to groups
    Shot.containers = (shots_group, updatable_group, drawable_group)
    Player.containers = (updatable_group, drawable_group)
    player= Player(screen_middle[0], screen_middle[1], PLAYER_RADIUS)
   
    # Initializing the asteroidfield and asteroids
    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    asteroidfield = AsteroidField()
    
    while True:
        # calculate dt
        dt = clock.tick(60) / 1000.0
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
        screen.fill("black")
        updatable_group.update(dt)
        for asteroid in asteroid_group:
            if player.collision(asteroid) == True:
                print("Game over!")
                pygame.quit()
                exit()
            
            for shot in shots_group:
                if shot.collision(asteroid) == True:
                    new_asteroids = asteroid.split()
                    shot.kill()
                    
                    for x, y, radius, velocity in new_asteroids:
                        new_asteroid = Asteroid(x, y, radius)
                        new_asteroid.velocity = velocity
        
        for sprite in drawable_group:
            sprite.draw(screen)
        
        pygame.display.flip()
        
        clock.tick(60)


if __name__ == "__main__":
    main()
