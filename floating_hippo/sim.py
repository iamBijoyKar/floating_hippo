import pygame
import pymunk
import pymunk.pygame_util
from pymunk import Vec2d
from typing import Sequence,List,Tuple
from .utils import str_to_pygame_event
class Event:
    def __init__(self,type:pygame.event.EventType,event_str,func) -> None:
        self.type = type
        self.func = func
        self.event_str = event_str

class Events:
    def __init__(self) -> None:
        self.events:List[Event] = []

    def add_event(self,type:str):
        def decorator(func):
            pygame_event = str_to_pygame_event(type)
            print(pygame_event)
            self.events.append(Event(pygame_event,type,func))
        return decorator

    def run_events(self,event:pygame.event.Event):
        for event_ in self.events:
            if event_.type == event.type:
                try:
                    event_.func(event)
                except Exception as e:
                    print(e)

            


class Simulation:
    def __init__(self,width=800,height=600,gravity=(0,100),fps=60.0,caption="Pymunk Test"):
        pygame.init()
        pymunk.pygame_util.positive_y_is_up = False
        pygame.display.set_caption(caption)
        self.width = width
        self.height = height
        self.is_running = True
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.dt = 1.0/self.fps
        self.window = pygame.display.set_mode((self.width, self.height))
        self.space = pymunk.Space()
        self.space.gravity = gravity
        self.draw_options = pymunk.pygame_util.DrawOptions(self.window)
        self.events = Events()

    def create_ball(self,pos:Vec2d | Tuple[int,int],radius=30.0,mass=1.0,moment=100.0,body_type=pymunk.Body.DYNAMIC,elasticity=0.5,friction=0.5)-> Tuple[pymunk.Body,pymunk.Circle]:
        body = pymunk.Body(mass=mass,moment=moment,body_type=body_type)
        body.position = pos
        shape = pymunk.Circle(body,radius)
        shape.elasticity = elasticity
        shape.friction = friction
        self.space.add(body,shape)
        return (body,shape)
    
    def create_box(self,pos:Vec2d | Tuple[int,int],width,height,mass=1.0,moment=100.0,body_type=pymunk.Body.DYNAMIC,elasticity=0.5,friction=0.5)-> Tuple[pymunk.Body,pymunk.Poly]:
        body = pymunk.Body(mass=mass,moment=moment,body_type=body_type)
        body.position = pos
        shape = pymunk.Poly.create_box(body,(width,height))
        shape.elasticity = elasticity
        shape.friction = friction
        self.space.add(body,shape)
        return (body,shape)
    
    def create_poly(self,pos:Vec2d | Tuple[int,int],vertices:Sequence[Tuple[float,float]],mass=1.0,moment=100.0,body_type=pymunk.Body.DYNAMIC,elasticity=0.5,friction=0.5)-> Tuple[pymunk.Body,pymunk.Poly]:
        body = pymunk.Body(mass=mass,moment=moment,body_type=body_type)
        body.position = pos
        shape = pymunk.Poly(body,vertices)
        shape.elasticity = elasticity
        shape.friction = friction
        self.space.add(body,shape)
        return (body,shape)
    
    
    def create_segment(self,pos1:Vec2d | Tuple[int,int],pos2:Vec2d | Tuple[int,int],elasticity=0.5,friction=0.5):
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
                self.events.run_events(event)                    

            self.space.step(self.dt)
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.fps)
            pygame.display.update()

        pygame.quit()