import pygame

class Circle:
    def __init__(self, plane, color: tuple | list, center : tuple | list, radius : int | float, width : int = 0):
        """Create a Circle Object on the Cartesian Plane

        Args:
            plane (Cartesian Plane): The Cartesian Plane
            color (tuple | list): The color of the circle
            center (tuple | list): The position of the center of the circle
            radius (int | float): The radius of the circle
            width (int, optional): Width of the border of the circle. 0 to fill the object. Defaults to 0.
        """
        self.plane = plane
        self.center = [*center]
        self.radius = radius
        self.color = color
        self.width = width

        self.plane.objects.append(self)

    def draw(self):
        """Draw the circle
        """
        # Convert Cartesian to Screen Coordinates
        center = self.plane.plane_to_screen(self.center)
        radius = self.plane.scale(self.radius)

        # Draw the circle
        pygame.draw.circle(self.plane.screen, self.color, center, radius, self.width)

class Rect:
    def __init__(self, plane, color : tuple | list, rect : tuple | list, width : int = 0):
        """Create a Rectangle Object on the Cartesian Plane

        Args:
            plane (Cartesian Plane): The Cartesian Plane
            color (tuple | list): The color of the rectangle
            rect (tuple | list): The rectangle dimentions. [x, y, width, height]
            width (int, optional): Width of the border of the rectangle. 0 to fill the object. Defaults to 0.
        """
        self.plane = plane
        self.rect = [rect[0], rect[1]]
        self.width = rect[2]
        self.height = rect[3]
        self.color = color
        self.line_width = width

        self.plane.objects.append(self)

    def draw(self):
        """Draw the rectangle
        """
        # Convert Cartesian to Screen Coordinates
        rect = self.plane.plane_to_screen(self.rect)
        width = self.plane.scale(self.width)
        height = self.plane.scale(self.height)

        # Draw the rectangle
        pygame.draw.rect(self.plane.screen, self.color, [*rect, width, height], self.line_width)

class Line:
    def __init__(self, plane, color : tuple | list, start : tuple | list, end : tuple | list, width : int = 1):
        """Create a Line Object on the Cartesian Plane

        Args:
            plane (Cartesian Plane): The Cartesian Plane
            color (tuple | list): The color of the line
            start (tuple | list): The start position of the line
            end (tuple | list): The end position of the line
            width (int, optional): Width of the line. Defaults to 1.
        """
        self.plane = plane
        self.start = [*start]
        self.end = [*end]
        self.color = color
        self.width = width

        self.plane.objects.append(self)

    def draw(self):
        """Draw the line
        """
        # Convert Cartesian to Screen Coordinates
        start = self.plane.plane_to_screen(self.start)
        end = self.plane.plane_to_screen(self.end)

        # Draw the line
        pygame.draw.line(self.plane.screen, self.color, start, end, self.width)

class Path:
    def __init__(self, plane, color : tuple | list, *points : tuple | list, length : int=1000):
        """Create a Path Object on the Cartesian Plane

        Args:
            plane (Cartesian Plane): The Cartesian Plane
            color (tuple | list): The color of the path
            length (int, optional): Numbers of points. Defaults to 100.
        """
        self.plane = plane
        self.color = color
        self.path = [*points]
        self.length = length

        self.plane.objects.append(self)

    def add_points(self, *points : tuple|list):
        """Add a point to the path

        Args:
            point (tuple | list): The points to add
        """
        self.path.extend(points)

        if len(self.path) > self.length and self.length > 0:
            self.path = self.path[len(self.path) - self.length:]

    # A more efficient way to check if a point is in the screen, but don't work with rectangles and the points needs to be in the screen cordinates
    def _is_in_screen(self, point : tuple|list):
        return point[0] >= 0 and point[0] < self.plane.size[0] and point[1] >= 0 and point[1] < self.plane.size[1]

    def draw(self):
        """Draw the path
        """
        for point in self.path:
            # Convert Cartesian to Screen Coordinates
            point = self.plane.plane_to_screen(point)

            # Removing duplicate and out of screen points
            if self._is_in_screen(point):
                self.plane.screen.set_at(point, self.color)

class draw:
    def circle(surface, color : tuple | list, center : list, radius : int | float, width : int = 0):
        """Draw a circle on the Cartesian Plane

        Args:
            surface (Cartesian Plane): The Cartesian Plane
            color (tuple | list): The color of the circle
            center (list): The position of the center of the circle
            radius (int | float): The radius of the circle
            width (int, optional): Width of the border of the circle. 0 to fill. Defaults to 0.
        """
        pygame.draw.circle(surface.screen, color, surface.plane_to_screen(center), surface.scale(radius), width=width)

    def rect(surface, color : tuple | list, rect : list, width : int = 0):
        """Draw a rectangle on the Cartesian Plane

        Args:
            surface (Cartesian Plane): The Cartesian Plane
            color (tuple | list): The color of the rectangle
            rect (list): The rectangle dimentions. [x, y, width, height]
            width (int, optional): Width of the border of the rectangle. 0 to fill. Defaults to 0.
        """
        pygame.draw.rect(surface.screen, color, [*surface.plane_to_screen((rect[0], rect[1])), surface.scale(rect[2]), surface.scale(rect[3])], width=width)

    def line(surface, color : tuple | list, start_pos : list, end_pos : list, width : int = 1):
        """Draw a line on the Cartesian Plane

        Args:
            surface (Cartesian Plane): The Cartesian Plane
            color (tuple | list): The color of the line
            start_pos (list): The start position of the line
            end_pos (list): The end position of the line
            width (int, optional): Width of the line. Defaults to 1.
        """
        pygame.draw.line(surface.screen, color, surface.plane_to_screen(start_pos), surface.plane_to_screen(end_pos), width=width)