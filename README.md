# Simple Snake Game Project

### Overview

This project is a simple implementation of the classic **Snake** game using Python's **Turtle** library. The game features a moving snake, a food item, and a scoreboard. The goal is to eat as much food as possible while avoiding collisions with the walls or the snake's own body.

-----

### Features

  * **Snake Movement**: Control the snake's direction using the arrow keys (`↑`, `↓`, `←`, `→`).
  * **Scoreboard**: The score increases each time the snake eats a piece of food.
  * **Tail Extension**: The snake grows longer with every food item it consumes.
  * **Collision Detection**:
      * The game resets if the snake hits the wall.
      * The game also resets if the snake collides with its own body.

-----

### How to Install and Run

1.  Make sure you have Python installed on your computer.
2.  This project uses the **Turtle** library, which is part of the standard Python distribution, so you don't need to install any external packages.
3.  Ensure all the necessary files (`main.py`, `snake.py`, `food.py`, `scoreboard.py`) are in the same directory.
4.  Run the main file from your terminal or Command Prompt:
    ```bash
    python main.py
    ```

-----

### How to Play

  * Use the **up**, **down**, **left**, and **right** arrow keys to control the snake's direction.
  * Guide the snake's head to the food (the white circle) to eat it.
  * Each time you eat food, your score and the snake's length will increase.
  * Avoid hitting the walls around the screen or the snake's own body. If you hit either, the game will end, and your score will reset.

-----

### Dependencies

This project relies only on Python's built-in libraries, primarily `turtle` and `time`.

  * **`turtle`**: Used to create the graphics and movement on the screen.
  * **`time`**: Used to control the speed of the snake's movement.

-----

### Code Structure

  * `main.py`: The main file that runs the entire game logic.
  * `snake.py`: A class that defines the behavior and properties of the snake object.
  * `food.py`: A class that manages the food's position and appearance.
  * `scoreboard.py`: A class that handles the display and updates of the score.

-----

I hope this README is helpful\! Is there anything else you'd like to add or change?
