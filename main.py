import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

def findArea(pointA, pointB, pointC):
    # Using Heron's formula
    x1, x2, x3 = pointA[0], pointB[0], pointC[0]
    y1, y2, y3 = pointA[1], pointB[1], pointC[1]

    # Using the distance formula to calculate length of each side
    ab = math.sqrt((x2-x1)**2 + (y2-y1)**2) # Between A and B
    bc = math.sqrt((x3-x2)**2 + (y3-y2)**2) # Between B and C
    ac = math.sqrt((x3-x1)**2 + (y3-y1)**2) # Between A and C

    sp = (ab + bc + ac) / 2 # sp = semi-perimeter

    area = math.sqrt(sp * ((sp-ab) * (sp-bc) * (sp-ac)))

    return area

def pointInTriangle(point, triangleVertices):
    a, b, c = triangleVertices

    if findArea(point, a, b) + findArea(point, b, c) + findArea(point, a, c) <= findArea(a, b, c):
        return point
    
    return False

pointCoordinates = (random.randint(250, 750), random.randint(250, 500)) # Starts with random coordinates to start

basePoints = {"A":(250,500), "B":(500,250), "C":(750,500)} # Main three points creating the base trinagle
baseArea = findArea(basePoints["A"], basePoints["B"], basePoints["C"])

while pointInTriangle(pointCoordinates, (basePoints["A"], basePoints["B"], basePoints["C"])) == False:
    pointCoordinates = (random.randint(250, 750), random.randint(250, 500))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    for point in basePoints:
        pygame.draw.circle(screen, "black", basePoints[point], 5) # Visually plot each point

    pygame.draw.circle(screen, "deeppink2", pointCoordinates, 5) # Visually plot each point

    pygame.display.flip() # Display to screen

pygame.quit()