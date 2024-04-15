<div align="center">
    <img src="https://github.com/iamBijoyKar/floating_hippo/assets/85790967/ba8de7a3-e766-404a-9a24-ff413036a411" width="300" alt="logo" />
    <h1> Floating Hippo </h1>
    <p> Floating Hippo is a simple, abstracted, and easy to use library for 2D simulations using Pymunk and Pygames. This is designed to make it easier to create simulations without worrying about the complexity of Pymunk and Pygames. Is is a good starting point for beginners who want to learn about physics simulations. 
    </p>
</div>

> **Note:** This library is still in development and is not ready for use. We are looking for contributors to help us finish this project 🙂

## Features 🚀
- **Simple:** Floating Hippo is designed to be simple and easy to use.
- **Abstracted:** Floating Hippo abstracts the complexity of Pymunk and Pygames to make it easier to create simulations.
- **Customizable:** Floating Hippo allows you to customize the simulation as per your needs.
- **Event Handling:** Floating Hippo provides an event handling system to handle events like mouse clicks, key presses, etc.
- **Built-in Shapes:** Floating Hippo provides built-in shapes like circle, segment, and polygon to create the simulation.


## Installation 🪄
```bash
pip install floating-hippo
```

## Usage 📖

Simple example of a simulation dropping balls on a |_| shaped platform on mouse click using Floating Hippo.

### Code 👇

```python
from floating_hippo import Simulation

# Create a simulation
simulation = Simulation(800,600,caption="Test",gravity=(0,1000))

# Create a segment shape like |_|
simulation.create_segment((100,100),(100,500))
simulation.create_segment((100,500),(600,500))
simulation.create_segment((600,500),(600,100))

@simulation.events.add_event("mousebuttondown")
def on_click(event,*args,**kwargs):
    simulation.create_ball(event.pos)

```
![falling_balls_floating_hippo - Made with Clipchamp](https://github.com/iamBijoyKar/floating_hippo/assets/85790967/17dcbfbb-4874-4124-8be4-cf22722edea3)

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing 🤝

Contributions, issues and feature requests are welcome! Feel free to check [issues page](https://github.com/iamBijoyKar/floating_hippo/issues).


## Show your support ⭐️

Give a ⭐️ if this project helped you!
