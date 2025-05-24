# prologue
import pygame
screen = pygame.display.set_mode((600,600))
running = True
x = 0
y = 0
px = 0
py = 0
ox = 0
oy = 0
oxvel = 0
oyvel = 0
yvel = 0
xvel = 0
mousedown = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #the important math stuff "main reason why you're here"
        if event.type == pygame.MOUSEMOTION:
            #calculates the mouses velocity.
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            xvel = (x - px)
            yvel = (y - py)
            px = pygame.mouse.get_pos()[0]
            py = pygame.mouse.get_pos()[1]
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            #this one should be obvious
            mousedown = True
            
        if event.type == pygame.MOUSEBUTTONUP:
            #sets it to know to add the velocity
            mousedown = False
            oxvel = xvel
            oyvel = yvel
    if mousedown:
        #this makes sure it doesn't go crazy
        ox = x
        oy = y
        oxvel = 0
        oyvel = 0
    #epilogue
    ox += oxvel
    oy += oyvel
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (255,255,255), [ox,oy], 5, 0)
    oyvel += 0.1
    oxvel *= 0.99
    if ox >= 595 or ox <= 5:
        oxvel *= -0.7
    if oy >= 595 or oy <= 5:
        oyvel *= -0.7
        if oy >= 595:
            oy = 596
        else:
            oy = 6
    ox = max(5, min(595, ox))
    oy = max(5, min(595, oy))
    pygame.display.update()
pygame.quit()