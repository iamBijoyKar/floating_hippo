import pygame
import pymunk
import pymunk.pygame_util

class Simulation:
    def __init__(self,width=800,height=600,gravity=(0,100),fps=60.0,caption="Pymunk Test"):
        pygame.init()
        self.width = width
        self.height = height
        self.is_running = True
        self.clock = pygame.time.Clock()
        self.fps = 60.0
        self.dt = 1.0/self.fps
        self.window = pygame.display.set_mode((self.width, self.height))

        self.space = pymunk.Space()
        self.space.gravity = gravity
        self.draw_options = pymunk.pygame_util.DrawOptions(self.window)
        pygame.display.set_caption(caption)

    def create_ball(self,pos,radius=30,mass=1,moment=100,body_type=pymunk.Body.DYNAMIC,elasticity=0.5,friction=0.5):
        body = pymunk.Body(mass=mass,moment=moment,body_type=body_type)
        body.position = pos
        shape = pymunk.Circle(body,radius)
        shape.elasticity = elasticity
        shape.friction = friction
        self.space.add(body,shape)
        return shape
    
    
    def create_segment(self,pos1,pos2,elasticity=0.5,friction=0.5):
        segment = pymunk.Segment(self.space.static_body,pos1,pos2,1)
        segment.elasticity = elasticity
        segment.friction = friction
        self.space.add(segment)
        return segment

    def draw(self):
        self.window.fill((255,255,255))
        self.space.debug_draw(self.draw_options)
        pygame.display.update()

    def run(self):
        while self.is_running:
            self.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())

            self.space.step(self.dt)
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.fps)
            pygame.display.update()

        pygame.quit()