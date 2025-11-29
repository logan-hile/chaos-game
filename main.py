import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

baseIndices = [(250, 500), (500, 250), (750, 500)] # Main three points

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    for point in baseIndices:
        pygame.draw.circle(screen, "black", point, 5) # Visually plot each point

    pygame.display.flip() # Display to screen

pygame.quit()