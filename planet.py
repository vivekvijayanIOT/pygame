import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((700, 700))
earth = pygame.transform.scale(pygame.image.load('earth.png'), (30,30))
sun = pygame.transform.scale(pygame.image.load('sun.png'), (80,80))
moon = pygame.transform.scale(pygame.image.load('moon.png'), (10,10))

white = (255, 255, 255)
blue = (0, 0, 255)
yellow = (255, 255, 0)
grey = (200, 200, 200)
black = (0, 0, 0)
sun_radius = 50
center = (350, 350)
earth_x = 50
earth_y = 330
earth_orbit = 0
moon_orbit = 0
clock = pygame.time.Clock()
running = True
stars = [(random.randint(0, 699), random.randint(0, 699)) for x in range(140)]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    earth_x = math.cos(earth_orbit) * 300 + 350
    earth_y = -math.sin(earth_orbit) * 300 + 350
    moon_x = math.cos(moon_orbit) * 50 + earth_x
    moon_y = -math.sin(moon_orbit) * 50 + earth_y
    earth_orbit += .002
    moon_orbit += .01
    screen.fill(black)
    for star in stars:
        x, y = star[0], star[1]
        pygame.draw.line(screen, white, (x, y), (x, y))   
    screen.blit(earth,(int(earth_x), int(earth_y)))
    screen.blit(sun,center)
    screen.blit(moon,((int(moon_x), int(moon_y))))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
