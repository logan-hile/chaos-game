import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

def findArea(vertices):
    pA, pB, pC = vertices # p = Point (pointA, pointB, pointC)
    # Using Heron's formula
    x1, x2, x3 = pA[0], pB[0], pC[0]
    y1, y2, y3 = pA[1], pB[1], pC[1]

    # Using the distance formula to calculate length of each side
    ab = math.sqrt((x2-x1)**2 + (y2-y1)**2) # Between A and B
    bc = math.sqrt((x3-x2)**2 + (y3-y2)**2) # Between B and C
    ac = math.sqrt((x3-x1)**2 + (y3-y1)**2) # Between A and C

    sp = (ab + bc + ac) / 2 # sp = semi-perimeter

    area = math.sqrt(sp * ((sp-ab) * (sp-bc) * (sp-ac)))

    return area

def findMiddlePoint(pA, pB):
    x1, x2 = pA[0], pB[0]
    y1, y2 = pA[1], pB[1]
    
    xCoord = abs(x2-x1)
    yCoord = abs(y2-y1)

    print(xCoord, yCoord)
    
    return(xCoord, yCoord)

firstPointCoordinates = (random.randint(250, 750), random.randint(250, 500)) # Starts with random coordinates to start

basePoints = {"A":(250,500), "B":(500,250), "C":(750,500)} # Main three points creating the base trinagle
baseArea = findArea(basePoints.values())

lastPlottedCoordinates = (0,0)

def pointInTriangle(point, vertices):
    pA, pB, pC = vertices

    if findArea((point, pA, pB)) + findArea((point, pB, pC)) + findArea((point, pA, pC)) <= baseArea:
        return point
    
    return False

def pickRandomVertice():
    rand = random.randint(0, 2)

    if rand == 0:
        return("A")
    elif rand == 1:
        return("B")
    
    return("C")

while not pointInTriangle(firstPointCoordinates, basePoints.values()):
    firstPointCoordinates = (random.randint(250, 750), random.randint(250, 500)) # Get new random coordinates

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    for point in basePoints:
        pygame.draw.circle(screen, "black", basePoints[point], 5) # Visually plot each point

    pygame.draw.circle(screen, "deeppink2", firstPointCoordinates, 5)

    for i in range(0, 1000):
        baseVertice = pickRandomVertice()
        midPoint = findMiddlePoint(lastPlottedCoordinates, basePoints[baseVertice])

        pygame.draw.circle(screen, "green", midPoint, 5)


    pygame.display.flip() # Display to screen

pygame.quit()