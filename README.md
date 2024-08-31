# Snake Game

This is a simple implementation of the classic Snake game using Python and the `turtle` library. The goal of the game is to control the snake to eat the food that appears on the screen and grow. The game ends when the snake collides with the screen borders or itself.

## Features

- Control the snake using the `W`, `A`, `S`, `D` keys.
- Displays current score and high score.
- Difficulty increases as the snake grows.
- Win and lose messages.
- High score saved and loaded from a file.

## Configuration

- `HIGH_SCORES_FILE_PATH`: Path to the file where the high score is stored. The default path is `./high_scores`.

## How to Play

1. Run the Python script to start the game.
2. Use the `W`, `A`, `S`, `D` keys to control the snake’s direction.
3. The snake grows each time it eats the food (a red dot on the screen).
4. The game ends when the snake collides with the screen borders or itself.

## Main Functions

- `init_state()`: Initializes the game state.
- `setup(state)`: Sets up the screen and the snake.
- `move_head(state)`: Moves the snake’s head according to the current direction.
- `move_body(state)`: Moves the body of the snake.
- `create_food(state)`: Creates food at a random position.
- `add_body(state)`: Adds a segment to the snake's body.
- `check_if_food_to_eat(state)`: Checks if the snake has eaten the food.
- `boundaries_collision(state)`: Checks if the snake has collided with the screen borders.
- `check_collisions(state)`: Checks if the snake has collided with itself or the screen borders.
- `main()`: The main function that runs the game.
