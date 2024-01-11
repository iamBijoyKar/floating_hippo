from .sim import Simulation

# Window size
WIDTH,HEIGHT = 800,600

balls = Simulation(WIDTH,HEIGHT,caption="Test",gravity=(0,1000))

balls.create_segment((100,100),(100,500))
balls.create_segment((100,500),(600,500))
balls.create_segment((600,500),(600,100))

@balls.events.add_event("mousebuttondown")
def print_pos(event,*args,**kwargs):
    balls.create_ball(event.pos)

