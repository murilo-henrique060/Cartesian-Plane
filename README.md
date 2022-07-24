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
  - [is_in_screen()](#is_in_screen)
  - [debug](#debug)
  - [event_handling()](#event_handling)
  - [update()](#update)
- [Cartesian Objects](#cartesian-objects)
- [Example codes](#example-codes)
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

## is_in_screen()

    is_in_screen = cartesian_plane.is_in_screen(point, whidth, height)

Checks if a point or a rectangle is in the screen.

**Arguments:**

* point: (x, y) | [x, y] - The cartesian point to check.
* width: optional, int - The width of the rectangle. default to 0.
* height: optional, int - The height of the rectangle. default to 0.

Returns a boolean indicating if the point or rectangle is in the screen.

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

# Cartesian Objects


# Example codes

# Todo:

* add a layer system to the canvas