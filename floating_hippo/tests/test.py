
import sys
sys.path.append("../floating_hippo")

from floating_hippo import Simulation


# Window size
WIDTH,HEIGHT = 800,600

simulation = Simulation(WIDTH,HEIGHT,caption="Test",gravity=(0,1000))

@simulation.events.add_event("mousebuttondown")
def print_pos(event,*args,**kwargs):
    simulation.create_ball(event.pos)

if __name__ == "__main__":
    simulation.run()
