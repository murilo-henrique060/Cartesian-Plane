import pygame

# setup screen
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mouse Wheel")

# main loop
while True:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEWHEEL:
            print("Mouse wheel")
            print(f'{event.y:<10}')
    # draw
    screen.fill((0, 0, 0))
    pygame.display.update()
    # clock
    pygame.time.Clock().tick(60)