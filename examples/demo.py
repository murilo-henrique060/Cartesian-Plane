import pygame
import cartesianPlane

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Set up the window
pygame.init()
screen = pygame.display.set_mode()
pygame.display.set_caption('Cartesian Plane')

plane = cartesianPlane.cartesianPlane(screen)

circle = cartesianPlane.cartesianObject.Circle(plane, RED, [0, 0], 10)
rect = cartesianPlane.cartesianObject.Rect(plane, GREEN, [20, 10, 10, 10])
line = cartesianPlane.cartesianObject.Line(plane, BLUE, [40, 0], [10, 10])
path = cartesianPlane.cartesianObject.Path(plane, YELLOW, [0, 0], [10, 10], [20, 20])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            quit()

        plane.event_handling(event)

    circle.center = plane.screen_to_plane(pygame.mouse.get_pos())

    # Update the plane
    plane.update()

    # Update the screen
    pygame.display.update()