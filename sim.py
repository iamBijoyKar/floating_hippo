import pygame
import pymunk
import pymunk.pygame_util

class Simulation:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.run = True
        self.clock = pygame.time.Clock()
        self.fps = 60.0
        self.dt = 1.0/self.fps
        self.window = pygame.display.set_mode((self.width, self.height))

        self.space = pymunk.Space()
        self.space.gravity = (0,100)
        self.draw_options = pymunk.pygame_util.DrawOptions(self.window)

    def create_ball(self,space,pos,radius=30,mass=1,moment=100,body_type=pymunk.Body.DYNAMIC,elasticity=0.5,friction=0.5):
        body = pymunk.Body(mass=mass,moment=moment,body_type=body_type)
        body.position = pos
        shape = pymunk.Circle(body,radius)
        shape.elasticity = elasticity
        shape.friction = friction
        space.add(body,shape)
        return shape

    def draw(self):
        self.window.fill((255,255,255))
        self.space.debug_draw(self.draw_options)
        pygame.display.update()

    def run(self):
        while self.run:
            self.draw(self.window)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            self.space.step(self.dt)
            self.draw(self.window)
            pygame.display.flip()
            self.clock.tick(self.fps)
            pygame.display.update()

        pygame.quit()