import pygame
import cartesianPlane
from math import sin

RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Senoid')
clock = pygame.time.Clock()

plane = cartesianPlane.CartesianPlane(screen)

senoid = cartesianPlane.Path(plane, RED, [0, 0], length=0)

x = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            quit()

        plane.event_handling(event)

    plane.debug(
        fps=f'{clock.get_fps():.1f}',
        points=len(senoid.path)
    )

    # Update the plane
    plane.update()

    clock.tick(60)

    senoid.add_points([x * 100, sin(x) * 100])

    x += 0.01

    # Update the screen
    pygame.display.update()