import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen setup (1280x720)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Niki's Game - Player Demo")

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

# Sprite animation settings
ANIMATION_SPEED = 10  # Frames per second for idle animation
FRAME_DELAY = int(1000 / ANIMATION_SPEED)  # Delay between frames in ms

def main():
    running = True
    
    # Initialize player position at module level
    player_x = SCREEN_WIDTH // 2
    player_y = SCREEN_HEIGHT // 2
    
    # Track animation frame index
    current_frame = 0
    is_moving = False
    
    # Load player sprite images from asset folder
    try:
        # Try to load all 19 idle frames for animation
        player_images_idle = []
        for i in range(19):  # Using 19 frames as specified
            image_path = f"assets/BlueWizard/2BlueWizardIdle/Chara - BlueIdle{i:05d}.png"
            try:
                img = pygame.image.load(image_path)
                # player size (PLAYER_RADIUS * 4.68 instead of PLAYER_RADIUS * 3.12)
                img = pygame.transform.scale(img, (PLAYER_RADIUS * 4.68, PLAYER_RADIUS * 4.68))
                player_images_idle.append(img)
            except pygame.error:
                # If image fails to load, continue with next frame
                print(f"Warning: Could not load {image_path}, continuing...")
                continue
        
        if len(player_images_idle) == 0:
            print("No idle sprite images found, falling back to red circle")
            player_images_idle = [pygame.Surface((PLAYER_RADIUS * 4.68, PLAYER_RADIUS * 4.68))]
    
    except Exception as e:
        print(f"Error loading idle sprites: {e}")
        player_images_idle = [pygame.Surface((PLAYER_RADIUS * 4.68, PLAYER_RADIUS * 4.68))]
    
    # Try to load walking sprite images from asset folder
    try:
        player_images_walk = []
        for i in range(19):  # Using 19 frames as specified
            image_path = f"assets/BlueWizard/2BlueWizardWalk/Chara_BlueWalk{i:05d}.png"
            try:
                img = pygame.image.load(image_path)
                # player size (PLAYER_RADIUS * 4.68 instead of PLAYER_RADIUS * 3.12)
                img = pygame.transform.scale(img, (PLAYER_RADIUS * 4.68, PLAYER_RADIUS * 4.68))
                player_images_walk.append(img)
            except pygame.error:
                # If image fails to load, continue with next frame
                print(f"Warning: Could not load {image_path}, continuing...")
                continue
        
        if len(player_images_walk) == 0:
            print("No walking sprite images found, falling back to red circle")
            player_images_walk = [pygame.Surface((PLAYER_RADIUS * 4.68, PLAYER_RADIUS * 4.68))]
    
    except Exception as e:
        print(f"Error loading walking sprites: {e}")
        player_images_walk = [pygame.Surface((PLAYER_RADIUS * 4.68, PLAYER_RADIUS * 4.68))]
    
    # Track which animation set to use
    current_animation_set = "idle"
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Get key states
        keys = pygame.key.get_pressed()
        
        # Check if user is moving (any WASD key pressed)
        is_moving = keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]
        
        # Switch animation set based on movement state
        if is_moving:
            current_animation_set = "walk"
        else:
            current_animation_set = "idle"
        
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
        
        # Update animation frame based on time
        if len(player_images_idle) > 1 and current_animation_set == "idle":
            current_frame = (pygame.time.get_ticks() // FRAME_DELAY) % len(player_images_idle)
        elif len(player_images_walk) > 1 and current_animation_set == "walk":
            current_frame = (pygame.time.get_ticks() // FRAME_DELAY) % len(player_images_walk)
        
        # Draw everything
        screen.fill(WHITE)  # Clear screen
        
        # Draw player sprite instead of red circle
        if len(player_images_idle) > 0 and current_animation_set == "idle":
            try:
                img = player_images_idle[current_frame]
                rect = pygame.Rect(player_x - PLAYER_RADIUS * 2.34, player_y - PLAYER_RADIUS * 2.34, 
                                   PLAYER_RADIUS * 4.68, PLAYER_RADIUS * 4.68)
                screen.blit(img, rect)
            except Exception as e:
                print(f"Error drawing idle sprite: {e}")
        elif len(player_images_walk) > 0 and current_animation_set == "walk":
            try:
                img = player_images_walk[current_frame]
                rect = pygame.Rect(player_x - PLAYER_RADIUS * 2.34, player_y - PLAYER_RADIUS * 2.34, 
                                   PLAYER_RADIUS * 4.68, PLAYER_RADIUS * 4.68)
                screen.blit(img, rect)
            except Exception as e:
                print(f"Error drawing walking sprite: {e}")
        else:
            # Fallback to red circle if no sprites loaded
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
