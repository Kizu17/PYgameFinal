import pygame
import sys
import imageio
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 500
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 80
PUCK_SIZE = 20
FPS = 60
FPS_GIF = 30
# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 146, 230)
BLACK = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2P Soccer Game")

# Load background GIF frames
background_gif_path = "img/soccer.gif"
background_gif = imageio.mimread(background_gif_path)
background_gif_path2 = "img/restartBG.gif"
background_gif2 = imageio.mimread(background_gif_path2)

background_image = pygame.image.load("img/hockeyField.png").convert()
background_rect = background_image.get_rect()

#just an image
image_path = "img/logo.png"
image = pygame.image.load(image_path)

image_path2 = "img/gameOver.png"
image2 = pygame.image.load(image_path2)

image_path3 = "img/Instruction.png"
image3 = pygame.image.load(image_path3)

image_path4 = "img/developers.png"
image4 = pygame.image.load(image_path4)

# Set the desired size
new_width, new_height = 450, 150
new_width2, new_height2 = 200, 50
new_width3, new_height3 = 800, 500
new_width4, new_height4 = 800, 500

# Resize the image
resized_image = pygame.transform.scale(image, (new_width, new_height))
resized_image2 = pygame.transform.scale(image2, (new_width2, new_height2))
resized_image3 = pygame.transform.scale(image3, (new_width3, new_height3))
resized_image4 = pygame.transform.scale(image4, (new_width4, new_height4))

#for Goal keeper design
goalkeeper_image_path = "img/player1.png"
goalkeeper_image = pygame.image.load(goalkeeper_image_path)

goalkeeper_image_path2 = "img/player2.png"
goalkeeper_image2 = pygame.image.load(goalkeeper_image_path2)

# Resize the goalkeeper image
resized_goalkeeper_image = pygame.transform.scale(goalkeeper_image, (PLAYER_WIDTH, PLAYER_HEIGHT))
resized_goalkeeper_image2 = pygame.transform.scale(goalkeeper_image2, (PLAYER_WIDTH, PLAYER_HEIGHT))

# Create a Pygame clock object to control the frame rate
clock = pygame.time.Clock()

MENU, GAME, RESTART_MENU, INSTRUCTION, DEVELOPER = 0, 1, 2, 3, 4
current_state = MENU

def draw_rounded_button(x, y, width, height, radius, color, text, text_color):
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, rect, border_radius=radius)

    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

    return rect  # Return the rect object for the button

def draw_instruction_menu():
    frame_index = 0
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Check for mouse click on the back button
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Draw the current frame of the GIF as the background
        frame_data = np.array(background_gif[frame_index])
        frame_surface = pygame.surfarray.make_surface(frame_data.swapaxes(0, 1))
        screen.blit(frame_surface, (0, 0))
        screen.blit(resized_image3, (0, 0))

        # Use the draw_rounded_button function for the back button
        back_button_rect = draw_rounded_button(WIDTH // 2 - 80, HEIGHT // 2 + 160, 150, 40, 10, BLUE, "Back", WHITE)

        if back_button_rect.collidepoint(mouse_x, mouse_y):
            keys = pygame.mouse.get_pressed()
            if keys[0]:  # Check for left mouse button click
                return MENU  # Return to the main menu

        pygame.display.flip()
        frame_index = (frame_index + 1) % len(background_gif)

        # Cap the frame rate of the GIF
        clock.tick(FPS_GIF)

def draw_developer_menu():
    frame_index = 0
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Check for mouse click on the back button
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Draw the current frame of the GIF as the background
        frame_data = np.array(background_gif[frame_index])
        frame_surface = pygame.surfarray.make_surface(frame_data.swapaxes(0, 1))
        screen.blit(frame_surface, (0, 0))
        screen.blit(resized_image4, (0, 0))

        # Use the draw_rounded_button function for the back button
        back_button_rect = draw_rounded_button(WIDTH // 2 - 80, HEIGHT // 2 + 160, 150, 40, 10, BLUE, "Back", WHITE)

        if back_button_rect.collidepoint(mouse_x, mouse_y):
            keys = pygame.mouse.get_pressed()
            if keys[0]:  # Check for left mouse button click
                return MENU  # Return to the main menu

        pygame.display.flip()
        frame_index = (frame_index + 1) % len(background_gif)

        # Cap the frame rate of the GIF
        clock.tick(FPS_GIF)

def draw_menu():
    frame_index = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        frame_data = np.array(background_gif[frame_index])
        frame_surface = pygame.surfarray.make_surface(frame_data.swapaxes(0, 1))
        screen.blit(frame_surface, (0, 0))

        screen.blit(resized_image, (330, 15))
        # Use the returned rect object for collision detection
        button_rect = draw_rounded_button(WIDTH // 2 + 65, HEIGHT // 2 - 30, 150, 40, 10, BLUE, "Start Game", WHITE)

        instruction_rect = draw_rounded_button(WIDTH // 2 + 65, HEIGHT // 2 + 20, 150, 40, 10, BLUE, "Instruction", WHITE)

        dev_rect = draw_rounded_button(WIDTH // 2 + 65, HEIGHT // 2 + 70, 150, 40, 10, BLUE, "Developers", WHITE)

        quit_rect = draw_rounded_button(WIDTH // 2 + 65, HEIGHT // 2 + 120, 150, 40, 10, BLUE, "Quit", WHITE)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Check for button clicks
        if button_rect.collidepoint(mouse_x, mouse_y):
            keys = pygame.mouse.get_pressed()
            if keys[0]:
                return True
        elif instruction_rect.collidepoint(mouse_x, mouse_y):
            keys = pygame.mouse.get_pressed()
            if keys[0]:
                return INSTRUCTION
        elif dev_rect.collidepoint(mouse_x, mouse_y):
            keys = pygame.mouse.get_pressed()
            if keys[0]:
                return DEVELOPER
        elif quit_rect.collidepoint(mouse_x, mouse_y):
            keys = pygame.mouse.get_pressed()
            if keys[0]:
                pygame.quit()
                sys.exit()

        pygame.display.flip()

        frame_index = (frame_index + 1) % len(background_gif)
        clock.tick(FPS_GIF)

# Function to reset positions
def reset_positions(player1, player2, puck):
    player1[0], player1[1] = 50, HEIGHT // 2 - PLAYER_HEIGHT // 2
    player2[0], player2[1] = WIDTH - 50 - PLAYER_WIDTH, HEIGHT // 2 - PLAYER_HEIGHT // 2
    puck[0], puck[1] = WIDTH // 2 - PUCK_SIZE // 2, HEIGHT // 2 - PUCK_SIZE // 2

# Function to draw the restart menu
def draw_restart_menu():
    frame_index = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        frame_data = np.array(background_gif2[frame_index])
        frame_surface = pygame.surfarray.make_surface(frame_data.swapaxes(0, 1))
        screen.blit(frame_surface, (0, 0))

        screen.blit(resized_image, (190, 10))
        screen.blit(resized_image2, (300, 170))


        button_rect_menu = draw_rounded_button(WIDTH // 2 - 75, HEIGHT // 2 + 10, 150, 40, 10, BLUE, "Main Menu", WHITE)

        button_rect = draw_rounded_button(WIDTH // 2 - 75, HEIGHT // 2 + 65, 150, 40, 10, BLUE, "Restart", WHITE)

        quit_rect = draw_rounded_button(WIDTH // 2 - 75, HEIGHT // 2 + 115, 150, 40, 10, BLUE, "Quit", WHITE)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Check for button clicks

        if button_rect_menu.collidepoint(mouse_x, mouse_y):
            keys = pygame.mouse.get_pressed()
            if keys[0]:
                return MENU
        elif button_rect.collidepoint(mouse_x, mouse_y):
            keys = pygame.mouse.get_pressed()
            if keys[0]:
                return True
        elif quit_rect.collidepoint(mouse_x, mouse_y):
            keys = pygame.mouse.get_pressed()
            if keys[0]:
                pygame.quit()
                sys.exit()

        pygame.display.flip()

        frame_index = (frame_index + 1) % len(background_gif2)
        clock.tick(FPS_GIF)

# Function for the game loop
def game_loop():
    clock = pygame.time.Clock()

    # Player positions
    player1_pos = [50, HEIGHT // 2 - PLAYER_HEIGHT // 2]
    player2_pos = [WIDTH - 50 - PLAYER_WIDTH, HEIGHT // 2 - PLAYER_HEIGHT // 2]

    # Puck position and speed
    puck_pos = [WIDTH // 2 - PUCK_SIZE // 2, HEIGHT // 2 - PUCK_SIZE // 2]
    puck_speed = [4, 4]

    # Scores
    score_player1 = 0
    score_player2 = 0

    # Font for displaying scores
    font = pygame.font.Font(None, 48)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1_pos[1] > 0:
            player1_pos[1] -= 7
        if keys[pygame.K_s] and player1_pos[1] < HEIGHT - PLAYER_HEIGHT:
            player1_pos[1] += 7

        if keys[pygame.K_UP] and player2_pos[1] > 0:
            player2_pos[1] -= 7
        if keys[pygame.K_DOWN] and player2_pos[1] < HEIGHT - PLAYER_HEIGHT:
            player2_pos[1] += 7

        # Update puck position
        puck_pos[0] += puck_speed[0]
        puck_pos[1] += puck_speed[1]

        # Check for collisions with walls
        if puck_pos[1] <= 0 or puck_pos[1] >= HEIGHT - PUCK_SIZE:
            puck_speed[1] = -puck_speed[1]

        # Check for collisions with players
        if (
            player1_pos[0] < puck_pos[0] + PUCK_SIZE
            and player1_pos[0] + PLAYER_WIDTH > puck_pos[0]
            and player1_pos[1] < puck_pos[1] + PUCK_SIZE
            and player1_pos[1] + PLAYER_HEIGHT > puck_pos[1]
        ) or (
            player2_pos[0] < puck_pos[0] + PUCK_SIZE
            and player2_pos[0] + PLAYER_WIDTH > puck_pos[0]
            and player2_pos[1] < puck_pos[1] + PUCK_SIZE
            and player2_pos[1] + PLAYER_HEIGHT > puck_pos[1]
        ):
            puck_speed[0] = -puck_speed[0]

        if puck_pos[0] < 0:
            score_player2 += 1
            reset_positions(player1_pos, player2_pos, puck_pos)


        elif puck_pos[0] > WIDTH:
            score_player1 += 1
            reset_positions(player1_pos, player2_pos, puck_pos)

        # Check for winning condition
        if score_player1 >= 5 or score_player2 >= 5:
            return RESTART_MENU  # Return to RESTART_MENU
        
        # Draw everything
        screen.blit(background_image, background_rect)
        
        # Draw the goalkeeper images instead of rectangles
        screen.blit(resized_goalkeeper_image, (player1_pos[0], player1_pos[1]))
        screen.blit(resized_goalkeeper_image2, (player2_pos[0], player2_pos[1]))

        pygame.draw.ellipse(screen, WHITE, (puck_pos[0], puck_pos[1], PUCK_SIZE, PUCK_SIZE))

        # Display scores
        score_text = font.render(f"{score_player1} - {score_player2}", True, WHITE)
        screen.blit(score_text, (WIDTH // 2 - 32, 30))
        
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if current_state == MENU:
        result = draw_menu()
        if result == GAME:
            current_state = GAME
        elif result == INSTRUCTION:
            current_state = INSTRUCTION
        elif result == DEVELOPER:
            current_state = DEVELOPER
    elif current_state == GAME:
        result = game_loop()
        if result == RESTART_MENU:
            current_state = RESTART_MENU
    elif current_state == RESTART_MENU:
        result = draw_restart_menu()
        if result == GAME:
            current_state = GAME
        elif result == MENU:
            current_state = MENU  # Reset positions when restarting
    elif current_state == INSTRUCTION:
        current_state = draw_instruction_menu()
    elif current_state == DEVELOPER:
        current_state = draw_developer_menu()



