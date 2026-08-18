import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup (1280x720)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Vampire Survivors - Player Demo")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player settings
PLAYER_RADIUS = 30
PLAYER_SPEED = 5

# Game clock for frame rate control
clock = pygame.time.Clock()
FPS = 60

def main():
    running = True
    
    # Initialize player position at module level
    player_x = SCREEN_WIDTH // 2
    player_y = SCREEN_HEIGHT // 2
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Get key states
        keys = pygame.key.get_pressed()
        
        # Update player position based on WASD input
        # Use independent if statements to handle multiple keys
        if keys[pygame.K_w]:
            player_y -= PLAYER_SPEED
        if keys[pygame.K_s]:
            player_y += PLAYER_SPEED
        if keys[pygame.K_a]:
            player_x -= PLAYER_SPEED
        if keys[pygame.K_d]:
            player_x += PLAYER_SPEED
        
        # Keep player within screen bounds
        player_x = max(PLAYER_RADIUS, min(SCREEN_WIDTH - PLAYER_RADIUS, player_x))
        player_y = max(PLAYER_RADIUS, min(SCREEN_HEIGHT - PLAYER_RADIUS, player_y))
        
        # Draw everything
        screen.fill(BLACK)  # Clear screen
        
        # Draw player (red circle)
        pygame.draw.circle(screen, RED, (player_x, player_y), PLAYER_RADIUS)
        
        # Update display
        pygame.display.flip()
        
        # Maintain frame rate
        clock.tick(FPS)
    
    # Quit Pygame
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
