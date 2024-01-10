import pygame
import pymunk
import pymunk.pygame_util
import math

WIDTH, HEIGHT = 800, 600
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pymunk.pygame_util.positive_y_is_up = False
pygame.display.set_caption("Pymunk Test")

def draw(window,space,draw_options):
    window.fill((255,255,255))
    space.debug_draw(draw_options)
    pygame.display.update()

def create_ball(space,pos,radius=30,mass=1,moment=100,body_type=pymunk.Body.DYNAMIC,elasticity=0.5,friction=0.5):
    body = pymunk.Body(mass=mass,moment=moment,body_type=body_type)
    body.position = pos
    shape = pymunk.Circle(body,radius)
    shape.elasticity = elasticity
    shape.friction = friction
    space.add(body,shape)
    return shape

def run(window,width,height):
    run = True
    clock = pygame.time.Clock()
    fps = 60.0
    dt = 1.0/fps

    space = pymunk.Space()
    space.gravity = (0,100)
    draw_options = pymunk.pygame_util.DrawOptions(window)

    ball = create_ball(space,(300,300))
    segment = pymunk.Segment(space.static_body, (200,500), (500, 300), 1)
    segment.elasticity = 0.5
    segment.friction = 0.5
    space.add(segment)

    while run:
        window.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        
        space.step(dt)
        draw(window,space,draw_options)
        pygame.display.flip()
        clock.tick(fps)
        pygame.display.update()


    pygame.quit()


if __name__ == "__main__":
    run(window,WIDTH,HEIGHT)
