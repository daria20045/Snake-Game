# Commentary done by Wardah Anwer

# Importing essential libraries
import pygame  # Pygame facilitates the import of all necessary modules for game development
import time  # The time module represents time in code using objects, numbers, and strings, offering various time-related functionalities
import random  # The random module is employed for generating and manipulating random integers

pygame.init()  # Initializing all the imported pygame modules

# Defining a palette of colors
# RGB (Red, Green, Blue) values in each line allow for a blend to produce a wide array of colors in the visible spectrum
# These color codes, represented as tuples ranging from 0 to 255, are used for computer display
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Setting the screen dimensions
screen_width = 600  # Width dimension
screen_height = 400  # Height dimension

# Initializing the game window with the specified screen size variables
screen = pygame.display.set_mode((screen_width, screen_height))
# The screen is automatically labeled as 'Snake Game' upon appearance
pygame.display.set_caption('Snake Game')

# Controlling frames per second (FPS)
clock = pygame.time.Clock()  # Creating a time-tracking object, measured in milliseconds

# Configuring frames for speed and movement; FPS regulates the animation's pace
snake_block = 10
snake_speed = 15

# Creating font objects with designated font style and size
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
# Function to visually represent the player's current score on the screen
def game_score(score):  
     # Render the player's score using a specific font, color, and value
     rendered_score = score_font.render("Score: " + str(score), True, blue)  
     # Display the rendered score at a designated position on the screen
     screen.blit(rendered_score, [0, 0]) 
 
 
# Function responsible for illustrating the snake's growth upon consuming the apple
def snake_growth(snake_block, snake_list): 
     # Iterate through each block in the snake's body
     for block_position in snake_list: 
         # Draw a white rectangle on the screen, representing each block in the snake
         pygame.draw.rect(screen, white, [block_position[0], block_position[1], snake_block, snake_block]) 
 
# Function to visually convey a message on the screen
def message(text, color): 
     # Render the message using a specified font, style, and color
     rendered_message = font_style.render(text, True, color) 
     # Display the rendered message at a defined position on the screen
     screen.blit(rendered_message, [screen_width / 6, screen_height / 3]) 
 
# Function governing the main game loop, determining when the game continues or stops
def game_loop():
     # Variable indicating whether the game is currently over
     game_over = False 
     # Variable handling specific conditions during active gameplay
     close_game = False 
     
     # Initial horizontal position of the snake's head
     x1 = screen_width / 2 
     # Initial vertical position of the snake's head
     y1 = screen_height / 2 
     
     # Variables representing the snake's movement in the horizontal and vertical directions
     x1_movement = 0 
     y1_movement = 0 
     
     # List storing the positions of each block in the snake's body
     snake_List = [] 
     # Initial length of the snake (starting with one block)
     snake_length = 1 
     
     # Randomly generated position for the apple along the x-axis
     x_food = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0 
     # Randomly generated position for the apple along the y-axis
     y_food = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0 

# Continue processing as long as the game is still in progress
while not game_over:
    # Execute this block when the game-over condition is true
    while close_game == True: 
        # Fill the screen with a black color to provide a clean slate
        screen.fill(black) 
        # Display a message informing the player of their loss and prompting them to press 'C' to play again or 'Q' to quit
        message("You Lost! Press C-Play Again or Q-Quit", blue)
        # Update the score display, subtracting 1 from the current snake length
        game_score(snake_length - 1)
        # Refresh the display to reflect the latest changes
        pygame.display.update()

        # Handle key events to respond to user input during the game-over state
        for event in pygame.event.get(): 
            # Check if a key has been pressed
            if event.type == pygame.KEYDOWN:
                # If the pressed key is 'Q', terminate the game
                if event.key == pygame.K_q: 
                    game_over = True 
                    close_game = False
                # If the pressed key is 'C', restart the game
                if event.key == pygame.K_c: 
                    game_loop()

    # Handle key events during the main game loop                
    for event in pygame.event.get(): 
        # If the user closes the game window, end the game
        if event.type == pygame.QUIT: 
            game_over = True  
        # If a key is pressed
        if event.type == pygame.KEYDOWN: 
            # If the left arrow key is pressed
            if event.key == pygame.K_LEFT: 
                # Move the snake to the left (negative direction) and maintain its vertical position
                x1_movement = -snake_block 
                y1_movement = 0 
            # If the right arrow key is pressed
            elif event.key == pygame.K_RIGHT: 
                # Move the snake to the right and maintain its vertical position
                x1_movement = snake_block 
                y1_movement = 0 
            # If the up arrow key is pressed
            elif event.key == pygame.K_UP: 
                # Move the snake upwards (negative direction) and maintain its horizontal position
                y1_movement = -snake_block 
                x1_movement = 0 
            # If the down arrow key is pressed
            elif event.key == pygame.K_DOWN: 
                # Move the snake downwards and maintain its horizontal position
                y1_movement = snake_block 
                x1_movement = 0 

if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
    # Set the flag to close the game when the snake hits the border
    close_game = True 

# Update the snake's position in the x direction    
x1 += x1_movement 
# Update the snake's position in the y direction 
y1 += y1_movement 
# Fill the screen with a black color
screen.fill(black) 
# Draw a rectangle to represent the food [location, color, [x_coordinate, y_coordinate, width, height]]
pygame.draw.rect(screen, red, [x_food, y_food, snake_block, snake_block]) 
# Create a new snake head
snake_head = [] 
# Add the new snake head's coordinates to the list
snake_head.append(x1) 
snake_head.append(y1)
# Add the new snake head to the snake_List for growth
snake_List.append(snake_head) 
# If the snake_List is longer than the snake's length, remove the oldest block
if len(snake_List) > snake_length: 
    del snake_List[0]

# Check for collisions with the snake's body
for x in snake_List[:-1]:
    # If the snake collides with itself, set the flag to close the game
    if x == snake_head:
        close_game = True

# Execute the snake growth function
snake_growth(snake_block, snake_List)
# Display the current score on the screen
game_score(snake_length - 1)
# Update the display screen
pygame.display.update()

# Check if the snake's head coordinates match the food coordinates
if x1 == x_food and y1 == y_food: 
    # Generate new random coordinates for the food
    x_food = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0 
    y_food = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
    # Increase the snake's length when it eats the food
    snake_length += 1 

# Control the game's speed by setting the number of frames per second
clock.tick(snake_speed)

# Close Pygame to stop running after the game ends
pygame.quit()
# Terminate the program
quit()

# Call the game_loop function to start or restart the game
game_loop()
