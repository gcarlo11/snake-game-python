# 🐍 Simple Snake Game

This project is a **classic Snake Game** implemented in **Python** using the built-in **Turtle** graphics library.
The goal is simple — guide the snake to eat as much food as possible while avoiding collisions with the walls or its own body.

---

## 🎮 Overview

The game creates a dynamic environment with:

* A **moving snake** controlled by arrow keys.
* A **food object** that randomly appears on the screen.
* A **scoreboard** that keeps track of how many food items have been eaten.

Each time the snake eats food, it grows longer — increasing the difficulty of avoiding collisions.

---

## ✨ Features

* **Snake Movement:**
  Control the snake using the arrow keys (↑, ↓, ←, →).

* **Scoreboard:**
  The score increases every time the snake eats a piece of food.

* **Tail Extension:**
  The snake’s body extends as it consumes food.

* **Collision Detection:**

  * If the snake hits a **wall**, the game resets.
  * If the snake hits its **own body**, the game also resets.

---

## 🧩 Code Structure

| File            | Description                                                                     |
| --------------- | ------------------------------------------------------------------------------- |
| `main.py`       | Contains the main game loop, event listeners, and collision logic.              |
| `snake.py`      | Defines the `Snake` class responsible for snake creation, movement, and growth. |
| `food.py`       | Defines the `Food` class that generates and refreshes the food position.        |
| `scoreboard.py` | Defines the `Scoreboard` class to track and display the score.                  |

---

## ⚙️ How to Install and Run

1. **Ensure Python is installed** (version 3.8 or newer is recommended).
   You can check by running:

   ```bash
   python --version
   ```

2. **Clone or download** this repository to your local machine.

3. Make sure all the following files are in the same directory:

   ```
   main.py
   snake.py
   food.py
   scoreboard.py
   ```

4. **Run the game** from your terminal or command prompt:

   ```bash
   python main.py
   ```

---

## 🕹️ How to Play

1. Use the **arrow keys** to control the snake’s movement:

   * ↑ Up
   * ↓ Down
   * ← Left
   * → Right

2. Eat the **food (white circle)** to gain points and grow longer.

3. Avoid hitting the **walls** or **your own tail** — doing so resets the game and your score.

4. Keep playing to beat your high score!

---

## 📦 Dependencies

This project uses **only Python’s built-in libraries**, no external packages are required.

* `turtle` — Handles the graphics, screen, and object drawing.
* `time` — Controls the refresh rate and speed of the snake’s movement.

---

## 🧠 Game Logic Summary

The main game loop continuously:

1. Updates the screen.
2. Moves the snake forward.
3. Detects collisions with:

   * **Food:** Adds points, extends the snake, and relocates food.
   * **Wall:** Resets the snake and scoreboard.
   * **Tail:** Resets the game if the snake runs into itself.

---

## 💡 Possible Improvements

* Add **sound effects** when eating food or hitting walls.
* Introduce **difficulty levels** (faster snake speed over time).
* Implement a **pause/restart button** using key bindings.
* Save and display the **highest score** using a local file.
* Add **themes** or color customizations for the snake and food.

