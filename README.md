# game-of-life-python
An implementation of John Conway's famous "Game of Life", written in Python and visualized with MatPlotLib.

Although this project is largely functional, I would like to revisit it at some point and make a few tweaks.

1. I want to explore and try out more efficient ways of computing the Game of Life. My current implementation, while functional, leaves some room for desire in the performance department. I would love it if I could find a more efficient way of computing cell updates so that I could scale up the game more, or have it compute faster.
2. I want to look into other visual interfaces for displaying the game. I am currently using Matplotlib, which I recognize as not the most efficient method to print matrix data to a screen. I would like to try out something else like Pygame or any visual library for Python with better performance.
3. I want to add a few more features to the simulation. One feature that's still currently a work-in-progress with the code is the ability to add specific cell formations to the matrix through a set of functions. I think it would be interesting if I were to extend this feature further by adding more formations as well as adding some way for users to add them in bulk (as opposed to manually changing the Python code each time).
