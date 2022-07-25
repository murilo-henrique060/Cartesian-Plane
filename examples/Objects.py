# Objects.py

import pygame
import cartesianPlane

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Set up the window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Cartesian Plane')
clock = pygame.time.Clock()

plane = cartesianPlane.CartesianPlane(screen)

circle = cartesianPlane.Circle(plane, RED, (0, 0), 10)
rect = cartesianPlane.Rect(plane, GREEN, [20, 10, 10, 10])
line = cartesianPlane.Line(plane, BLUE, [40, 0], [10, 10])
path = cartesianPlane.Path(plane, YELLOW, [0, 0], [10, 10], [20, 20])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            quit()

        plane.event_handling(event)

    plane.debug(
        fps=f'{clock.get_fps():.1f}'
    )

    # Update the plane
    plane.update()

    cartesianPlane.draw.circle(plane, GREEN, (15, 15), 1)
    cartesianPlane.draw.rect(plane, BLUE, (25, 25, 10, 10), 1)
    cartesianPlane.draw.line(plane, YELLOW, (35, 35), (45, 45))

    clock.tick()

    # Update the screen
    pygame.display.update()