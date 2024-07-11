# Snake Game (OOP)

## Description

This is a classic Snake game implemented in Python using the `turtle` module. The project is designed using Object-Oriented Programming (OOP) principles.

## Project Structure

The project contains the following files:

- `main.py`: Contains the main game loop.
- `snake.py`: Defines the `Snake` class which handles the behavior of the snake.
- `food.py`: Defines the `Food` class which handles the generation of food for the snake.
- `scoreboard.py`: Defines the `Scoreboard` class which handles the game score.

## How to Play

- Use the arrow keys to control the snake:
  - Up: Move up
  - Down: Move down
  - Left: Move left
  - Right: Move right

- The objective is to eat the food that appears on the screen. Each time the snake eats the food, it grows longer and the score increases by 1.

- The game ends if the snake collides with itself or the screen boundaries.

## Classes

### Snake

- **Methods**:
  - `__init__`: Initializes the snake with starting positions and segments.
  - `create`: Creates the initial snake segments.
  - `move`: Moves the snake forward.
  - `up`, `down`, `left`, `right`: Change the direction of the snake.

### Food

- **Methods**:
  - `__init__`: Initializes the food object.
  - `refresh`: Moves the food to a new random position on the screen.

### Scoreboard

- **Methods**:
  - `__init__`: Initializes the scoreboard.
  - `update_scoreboard`: Updates the score display.
  - `increase_score`: Increases the score by 1 and updates the display.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project is inspired by the classic Snake game and utilizes the `turtle` module for graphical representation.
