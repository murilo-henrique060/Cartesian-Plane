# Cartesian Plane
 Provides a cartesian plane canvas able to move and zooming in pygame.

## Key topics

- [Cartesian Plane](#cartesian-plane)
  - [Key topics](#key-topics)
  - [Overview](#overview)
- [Install](#install)
- [CartesianPlane](#cartesianplane)
  - [plane_to_screen()](#plane_to_screen)
  - [screen_to_plane()](#screen_to_plane)
  - [scale()](#scale)
  - [debug](#debug)
  - [event_handling()](#event_handling)
  - [update()](#update)
  - [Circle](#circle)
  - [Rectangle](#rectangle)
  - [Line](#line)
  - [Path](#path)
    - [add_points()](#add_points)
  - [draw](#draw)
    - [circle()](#circle-1)
    - [rect()](#rect)
    - [line()](#line-1)
- [Example codes](#example-codes)
  - [Objects.py](#objectspy)
  - [Senoid.py](#senoidpy)
- [Todo:](#todo)

## Overview

With this module you can use cartesian cordinates to draw forms and create objects in a cartesian plane. Which is useful for simple 2D graphics.

# Install

    pip install cartesian-plane

# CartesianPlane

    cartesian_plane = CartesianPlane(screen)


Creates a [CartesianPlane](#cartesianplane) canvas.

**Arguments:**

* screen: pygame screen - The screen where the canvas will be drawn.

Returns a [CartesianPlane](#cartesianplane) object.

## plane_to_screen()

    screen_pos = cartesian_plane.plane_to_screen(point)

Converts a cartesian point to a screen position.

**Arguments:**

* point: (x, y) | [x, y] - The cartesian point to convert.

Returns returns a screen position as a list [x, y].

## screen_to_plane()

    cartesian_point = cartesian_plane.screen_to_plane(screen_pos)

Converts a screen position to a cartesian point.

**Arguments:**

* screen_pos: (x, y) | [x, y] - The screen position to convert.

Returns a cartesian point as a list [x, y].

## scale()

    scaled_dimention = cartesian_plane.scale(dimension)

Scales a dimension to the current zoom level.

**Arguments:**

* dimension: int | float - The dimension to scale.

Returns a scaled dimension.

## debug

    cartesian_plane.debug(name1=value1, name2=value2, ...)

Add debug information to the Cartesian Plane. On each [update()](#update) call, the debug information will be drawn.

## event_handling()

    for event in pygame.event.get():
        # event handling
        ...

        cartesian_plane.event_handling(event)

This function is used on the event loop. It will handle the events of move and zooming the Cartesian Plane.

## update()

    cartesian_plane.update()

updates the Cartesian Plane and draws the objects.

## Circle

    circle = Circle(plane, color, center, radius, width)

Creates a [Circle](#circle) object. The circle is automated drawn on each call of the [update()](#update) function.

**Arguments:**

* plane: [CartesianPlane](#cartesianplane) - The Cartesian Plane where the circle will be drawn.
* color: (r, g, b) | (r, g, b, a) - The color of the circle.
* center: (x, y) | [x, y] - The center of the circle.
* radius: int | float - The radius of the circle.
* width: optional, int - The width of the circle. 0 to fill. default to 0.

## Rectangle

    rect = Rect(plane, color, rect, width)

Creates a [Rectangle](#rectangle) object. The rectangle is automated drawn on each call of the [update()](#update) function.

**Arguments:**

* plane: [CartesianPlane](#cartesianplane) - The Cartesian Plane where the rectangle will be drawn.
* color: (r, g, b) | (r, g, b, a) - The color of the rectangle.
* rect: (x, y, width, height) | [x, y, width, height] - The rectangle.
* width: optional, int - The width of the rectangle. 0 to fill. default to 0.

## Line

    line = Line(plane, color, start, end, width)

Creates a [Line](#line) object. The line is automated drawn on each call of the [update()](#update) function.

**Arguments:**

* plane: [CartesianPlane](#cartesianplane) - The Cartesian Plane where the line will be drawn.
* color: (r, g, b) | (r, g, b, a) - The color of the line.
* start: (x, y) | [x, y] - The start of the line.
* end: (x, y) | [x, y] - The end of the line.
* width: optional, int - The width of the line. default to 1.

## Path

    path = Path(plane, color, *points, length = 100)

Creates a [Path](#path) object. The path is automated drawn on each call of the [update()](#update) function.

**Arguments:**

* plane: [CartesianPlane](#cartesianplane) - The Cartesian Plane where the path will be drawn.
* color: (r, g, b) | (r, g, b, a) - The color of the path.
* points: (x, y) | [x, y] - The points of the path.
* length: optional, int - The max length of the path. 0 or less to unlimited lenght (not recommended). default to 1000.

### add_points()

    path.add_points(*points)

adds points to the path.

**Arguments:**

* points: (x, y) | [x, y] - The points to add.

## draw

This class is used to draw a shape on the screen.

### circle()

    draw.circle(plane, color, center, radius, width)

Draws a circle on the screen.

**Arguments:**

* plane: [CartesianPlane](#cartesianplane) - The Cartesian Plane where the circle will be drawn.
* color: (r, g, b) | (r, g, b, a) - The color of the circle.
* center: (x, y) | [x, y] - The center of the circle.
* width: optional, int - The width of the circle. 0 to fill. default to 0.

### rect()

    draw.rect(plane, color, rect, width)

Draws a rectangle on the screen.

**Arguments:**

* plane: [CartesianPlane](#cartesianplane) - The Cartesian Plane where the rectangle will be drawn.
* color: (r, g, b) | (r, g, b, a) - The color of the rectangle.
* rect: (x, y, width, height) | [x, y, width, height] - The rectangle.
* width: optional, int - The width of the rectangle. 0 to fill. default to 0.

### line()

    draw.line(plane, color, start, end, width)

Draws a line on the screen.

**Arguments:**

* plane: [CartesianPlane](#cartesianplane) - The Cartesian Plane where the line will be drawn.
* color: (r, g, b) | (r, g, b, a) - The color of the line.
* start: (x, y) | [x, y] - The start of the line.
* end: (x, y) | [x, y] - The end of the line.
* width: optional, int - The width of the line. default to 1.

# Example codes

## Objects.py

```python
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
```

## Senoid.py

```python
# Senoid.py
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
```

# Todo:

* add a layer system to the canvas