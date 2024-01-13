
import sys
sys.path.append("../floating_hippo")

from floating_hippo import Simulation


# Window size
WIDTH,HEIGHT = 800,600

simulation = Simulation(WIDTH,HEIGHT,caption="Test",gravity=(0,1000))

simulation.create_segment((100,500),(600,490),friction=1)
simulation.create_segment((100,500),(100,100),friction=1)

(ball1_body,ball1_shape) = simulation.create_ball((300,300),friction=1)
(ball2_body,ball2_shape) = simulation.create_ball((400,300),friction=1)

(square1_body,square1_shape) = simulation.create_box((500,300),150,50,friction=1)

# spring1 = simulation.create_damped_spring(ball1_body,square1_body,(0,0),(0,0),stiffness=1000.0,damping=100.0,rest_length=100.0)
# spring2 = simulation.create_damped_spring(ball2_body,square1_body,(0,0),(0,0),stiffness=1000.0,damping=100.0,rest_length=100.0)

motor1 = simulation.create_simple_motor(ball1_body,square1_body,rate=-10.0)

@simulation.events.add_event("mousebuttondown")
def print_pos(event,*args,**kwargs):
    simulation.create_ball(event.pos)

if __name__ == "__main__":
    simulation.run()
