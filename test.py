from sim import Simulation


# Window size
WIDTH,HEIGHT = 800,600

simulation = Simulation(WIDTH,HEIGHT,caption="Test",gravity=(0,1000))
simulation.create_ball((300,300))
simulation.create_ball((400,300))
simulation.create_segment((100,100),(100,500))
simulation.create_segment((100,500),(600,500))
simulation.create_segment((600,500),(600,100))


if __name__ == "__main__":
    simulation.run()
