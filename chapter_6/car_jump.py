import pygame
import pymunk
import pymunk.pygame_util
import math

pygame.init()

# Screen settings
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Jump Demo")
clock = pygame.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(screen)

# Physics settings
space = pymunk.Space()
space.gravity = (0, 90)  # gravity in x and y directions

# Ground
ground = pymunk.Segment(space.static_body, (0, height-100), (800, height-100), 5)
ground.friction = 0.7
space.add(ground)

# Ramp
ramp_angle = 10  # in degrees
ramp_length = 300
ramp_shape = pymunk.Segment(space.static_body, (300, height-100), (300 + int(ramp_length * math.cos(math.radians(ramp_angle))), height-100 - int(ramp_length * math.sin(math.radians(ramp_angle)))), 5)
ramp_shape.friction = 0.7
space.add(ramp_shape)

# Car setup
car_body = pymunk.Body(100, pymunk.moment_for_box(100, (50, 20)))
car_body.position = 100, height - 150
car_shape = pymunk.Poly.create_box(car_body, (50, 20))
car_shape.friction = 0.7

# Wheels
wheel1 = pymunk.Body(20, pymunk.moment_for_circle(20, 0, 10))
wheel1.position = car_body.position.x - 15, car_body.position.y + 10
wheel_shape1 = pymunk.Circle(wheel1, 10)
wheel_shape1.friction = 0.7

wheel2 = pymunk.Body(20, pymunk.moment_for_circle(20, 0, 10))
wheel2.position = car_body.position.x + 15, car_body.position.y + 10
wheel_shape2 = pymunk.Circle(wheel2, 10)
wheel_shape2.friction = 0.7

# Joints (connect wheels to body)
joint1 = pymunk.constraints.PivotJoint(car_body, wheel1, (0, 10), (0, 0))
joint2 = pymunk.constraints.PivotJoint(car_body, wheel2, (0, 10), (0, 0))

# Add car, wheels, joints to space
space.add(car_body, car_shape, wheel1, wheel_shape1, wheel2, wheel_shape2, joint1, joint2)

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Move car
    if keys[pygame.K_SPACE]:
        force = 3000
        angle = car_body.angle
        fx, fy = math.cos(angle) * force, math.sin(angle) * force
        car_body.apply_force_at_world_point((fx, fy), car_body.position)

    # Update physics
    space.step(1/60.0)

    # Draw everything
    screen.fill((255, 255, 255))  # Fill screen with white
    space.debug_draw(draw_options)

    # Draw vectors
    p = car_body.position
    v = car_body.velocity
    pygame.draw.line(screen, (255, 0, 0), (p[0], height - p[1]), (p[0] + v[0]/10, height - (p[1] + v[1]/10)), 3)  # Red line for velocity

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
