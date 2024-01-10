from sim import Simulation,Event
import pygame


# Window size
WIDTH,HEIGHT = 800,600

simulation = Simulation(WIDTH,HEIGHT,caption="Test",gravity=(0,1000))
simulation.create_ball((300,300))
simulation.create_ball((400,300))
simulation.create_segment((100,100),(100,500))
simulation.create_segment((100,500),(600,500))
simulation.create_segment((600,500),(600,100))

def print_hello():
    print("Hello")

simulation.events.add_event(Event(pygame.MOUSEBUTTONDOWN,print_hello))


if __name__ == "__main__":
    simulation.run()
