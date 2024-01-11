from sim import Simulation
# todo: make it unnecessary to import pygame
import pygame 


# Window size
WIDTH,HEIGHT = 800,600

simulation = Simulation(WIDTH,HEIGHT,caption="Test",gravity=(0,1000))
simulation.create_ball((300,300))
simulation.create_ball((400,300))
simulation.create_segment((100,100),(100,500))
simulation.create_segment((100,500),(600,500))
simulation.create_segment((600,500),(600,100))
simulation.create_box((400,100),100,100)
simulation.create_poly((100,100),[(0,0),(0,100),(100,100),(150,0)])


@simulation.events.add_event("mousebuttondown")
def print_pos(event,*args,**kwargs):
    simulation.create_ball(event.pos)

@simulation.events.add_event("keydown")
def print_key(event,*args,**kwargs):
    print(event.key)

if __name__ == "__main__":
    simulation.run()
