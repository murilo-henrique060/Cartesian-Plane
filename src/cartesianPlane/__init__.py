import pygame
from pygame.locals import *
from cartesianPlane.cartesianObjects import *
from cartesianPlane.colors import *

# Version of the Cartesian Plane package
__version__ = "1.0.0"

class CartesianPlane:
    def __init__(self, screen):
        """Initialize the Cartesian Plane

        Args:
            screen (pygame.display): The screen to draw on
        """
        self.screen = screen
        self.size = screen.get_size()
        self.rect = self.screen.get_rect()
        self.offset = list(self.rect.center)

        self.objects = []

        # track mouse position
        self.last_pos = None
        self.move_plane = False

        self.scale_factor = 1

        # Load Fonts
        pygame.font.init()
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 20)

        # Debug Info
        self.debug_info = {}


    def plane_to_screen(self, point : list | tuple) -> list:
        """Convert Cartesian Coordinates to Screen Coordinates

        Args:
            point (list | tuple): The Cartesian Coordinates

        Returns:
            list: The Screen Coordinates
        """
        screen_x = round((point[0] + self.offset[0]) * self.scale_factor) # Screen_X = (Cartesian_X + Offset_X) * Scale factor
        screen_y = round((self.offset[1] - point[1]) * self.scale_factor) # Screen_Y = (Offset_Y - Cartesian_Y) * Scale factor
        return [screen_x, screen_y]

    def screen_to_plane(self, point: list | tuple) -> list:
        """Convert Screen Coordinates to Cartesian Coordinates

        Args:
            point (list | tuple): The Screen Coordinates

        Returns:
            list: The Cartesian Coordinates
        """
        plane_x = (point[0] / self.scale_factor) - self.offset[0] # Cartesian x = (Screen_X / Scale_Factor) - Offset_X
        plane_y = self.offset[1] - (point[1] / self.scale_factor) # Cartesian y = Offset_Y - (Screen_Y / Scale_Factor)
        return [plane_x, plane_y]

    def scale(self, dimention : int | float) -> int:
        """Scale a dimention to the screen size

        Args:
            dimention (int | float): Dimension in plane size

        Returns:
            int: Dimension in screen size
        """
        return round(dimention * self.scale_factor)

    def move_axis(self) -> None:
        """Move the axis of the Cartesian Plane
        """
        current_pos = pygame.mouse.get_pos()
        if self.last_pos:
            self.offset[0] += (current_pos[0] - self.last_pos[0]) / self.scale_factor
            self.offset[1] += (current_pos[1] - self.last_pos[1]) / self.scale_factor

        self.last_pos = current_pos

    def zooming(self, wheel : int) -> None:
        """Zoom the Cartesian Plane

        Args:
            wheel (int): The amount of wheel movement
        """
        before_zooming = self.screen_to_plane(pygame.mouse.get_pos())
        if wheel > 0 and self.scale_factor < 100:
            self.scale_factor *= 1.1

        elif wheel < 0 and self.scale_factor > 0.1:
            self.scale_factor *= 0.9

        after_zooming = self.screen_to_plane(pygame.mouse.get_pos())
        self.offset[0] -= before_zooming[0] - after_zooming[0]
        self.offset[1] += before_zooming[1] - after_zooming[1]

    def debug(self, **kwargs) -> None:
        """Add debug information to the Cartesian Plane
        """
        for key, value in kwargs.items():
            self.debug_info[key] = value

        offset = 5
        for key, value in self.debug_info.items():
            text = self.font.render(f'{key}: {value}', True, WHITE)
            self.screen.blit(text, (10, offset))
            offset += text.get_height()

    def event_handling(self, event) -> None:
        """Handle events

        Args:
            event (pygame.locals): The event to handle
        """
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            self.move_plane = True

        if event.type == MOUSEBUTTONUP and event.button == 1:
            self.move_plane = False
            self.last_pos = None

        if event.type == MOUSEWHEEL:
            self.zooming(event.y)


    def update(self):
        """Update the Cartesian Plane
        """
        if self.move_plane:
            self.move_axis()

        # Clear the screen
        self.screen.fill(BLACK)

        # Draw the axis of Cartesian Plane
        origin = self.plane_to_screen((0, 0))
        pygame.draw.line(self.screen, WHITE, (0, origin[1]), (self.size[0], origin[1]), 1) # X-Axis = (0, origin_y) to (screen_width, origin_y)
        pygame.draw.line(self.screen, WHITE, (origin[0], 0), (origin[0], self.size[1]), 1) # Y-Axis = (origin_x, 0) to (origin_x, screen_height)

        # Draw the objects
        for object in self.objects:
            object.draw()

        # Draw the debug info
        self.debug(
            # Offset=self.offset,
            # Origin=self.plane_to_screen((0, 0))
            # Scale_Factor=f'{self.scale_factor*100:.2f}%',
            # Mouse_Pos=pygame.mouse.get_pos(),
            # Plane_Pos=self.screen_to_plane(pygame.mouse.get_pos()),
            # Converted_Mouse_Pos=self.plane_to_screen(self.screen_to_plane(pygame.mouse.get_pos()))
        )