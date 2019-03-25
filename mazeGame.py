import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# Setup
pygame.init()
 
# Set the width and height of the screen [width,height]
resolution = [420, 520]
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Hide the mouse cursor
pygame.mouse.set_visible(0)
 
#Speed
speed = 3

# Speed in pixels per frame
x_speed = 0
y_speed = 0
 
# Current position
x = 30
y = 30

#outer border
walls = [[0,0,10,520],[10,0,510,10],[10,510,520,520],[410,10,10,520]]
for i in [[60,10,50,250],[110,210,150,50],[210,260,50,200],[10,310,150,50],[60,410,200,50],[310,110,50,400],[160,60,200,100]]:
    walls.append(i)

class charachter():
    x = 15
    y = 15
    r = 10
    color = RED

    def __init__(self):
        pygame.draw.circle(screen, RED, [x,y], 10)

forrest = charachter()

def drawForrest(screen, x, y):
    pygame.draw.circle(screen, RED, [x,y], 10)

def drawMaze(walls):
        for wall in walls:
            pygame.draw.rect(screen,(0,0,0),(wall[0],wall[1],wall[2],wall[3]))
        
#Checks if forrest is touching a given rect
def checkCollision(rectCoords):
    x = rectCoords[0]
    y = rectCoords[1]
    width = rectCoords[2]
    height = rectCoords[3]
    if forrest.x > x and forrest.x < x+width and forrest.y > y and forrest.y < y+height: # in range(x1,x2) and forrest.y in range(y1,y2):
        return(True)
    else:
        return(False)

# -------- Main Program Loop -----------
while not done:
    # --- Event Processing

    x_speed = int(x_speed * .99)
    y_speed = int(y_speed * .99)

    lKey = False
    rKey = False
    uKey = False
    dKey = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

            # User pressed down a key
        elif (event.type == pygame.KEYDOWN and x_speed <= 10):
            # Figure out what key and react
            #print(event.key)
            if event.key == pygame.K_LEFT:
                lKey = True
                x_speed -= speed
            elif event.key == pygame.K_RIGHT:
                rKey = True
                x_speed += speed
            elif event.key == pygame.K_UP:
                uKey = True
                y_speed -= speed
            elif event.key == pygame.K_DOWN:
                dKey = True
                y_speed += speed

        if lKey and dKey:
            x_speed -= speed
            y_speed += speed
        elif lKey and uKey:
            x_speed -= speed
            y_speed -= speed
        elif rKey and uKey:
            x_speed += speed
            y_speed -= speed
        elif rKey and dKey:
            x_speed += speed
            y_speed += speed
        elif uKey:
            y_speed -= speed
        elif dKey:
            y_speed += speed
        elif lKey:
            x_speed -= speed
        elif rKey:
            x_speed += speed

    # --- Game Logic
 
    # Move the object according to the speed vector.
    x += x_speed
    y += y_speed
    forrest.x = x
    forrest.y = y

    for wall in walls:
            if checkCollision(wall):
                x = 30
                y = 30
                x_speed = 0
                y_speed = 0

    # --- Drawing Code

    screen.fill(WHITE)
    
    #Componets
    drawMaze(walls)
    drawForrest(screen, x, y)

    pygame.display.flip()
 
    # Limit frames per second
    clock.tick(120)
 
# Close the window and quit.
pygame.quit()


