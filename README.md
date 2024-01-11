<div align="center">
    <h1> Floating Hippo </h1>
    <p> Floating Hippo is a simple, abstracted, and easy to use library for 2D simulations using Pymunk and Pygames. 
    </p>
</div>

> **Note:** This library is still in development and is not ready for use. We are looking for contributors to help us finish this project 🙂

## Installation 🪄
```bash
pip install floating-hippo
```

## Usage 📖

Simple example of a simulation dropping balls on a |_| shaped platform on mouse click using Floating Hippo.

### Code 👇

```python
from floating_hippo import Simulation

# Width and Height of the window
WIDTH,HEIGHT = 800,600

# Create a simulation
simulation = Simulation(WIDTH,HEIGHT,caption="Test",gravity=(0,1000))

# Create a segment shape like |_|
simulation.create_segment((100,100),(100,500))
simulation.create_segment((100,500),(600,500))
simulation.create_segment((600,500),(600,100))

@simulation.events.add_event("mousebuttondown")
def on_click(event,*args,**kwargs):
    simulation.create_ball(event.pos)

if __name__ == "__main__":
    simulation.run()
```

## Contributing 🤝

Contributions, issues and feature requests are welcome! 


## Show your support ⭐️

Give a ⭐️ if this project helped you!
