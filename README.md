# Pokemon Hunt Game

A fun pygame-based collector game where you control a character to collect coins and pokeballs while hunting for Pokémon!

## Overview

Pokemon Hunt is a simple 2D game built with Pygame where the player navigates around the screen collecting coins to earn points and special pokeballs. The game features collision detection, sound effects, and a scoring system.

## Requirements

- Python 3.x
- Pygame library
- Sound files: `coin.mp3`, `poke.mp3`
- Image files:
  - `pokeball.png` - Game icon and pokeball item
  - `_Image 2.png` - Background image
  - `south.png` - Player sprite
  - `pika.png` - Pokémon sprite
  - `dollar.png` - Coin items

## Installation

1. Install Python from [python.org](https://www.python.org/)
2. Install Pygame:
   ```
   pip install pygame
   ```
3. Ensure all image and sound files are in the same directory as `Pokemon.py`

## How to Run

```bash
python Pokemon.py
```

## Controls

- **UP Arrow** - Move player up
- **DOWN Arrow** - Move player down
- **LEFT Arrow** - Move player left
- **RIGHT Arrow** - Move player right
- **Close Window** - Exit the game

## Game Mechanics

### Collectibles

**Coins (Dollar Signs)** - 7 coins placed across the screen
- Collecting a coin: +1 score
- Plays coin collection sound effect

**Pokeballs** - Special items mixed with coins
- Collecting a pokeball: +1 pokeball count
- Plays unique pokeball sound effect

### Scoring

- **Score**: Increases by 1 for each regular coin collected
- **Pokeballs**: Special counter for pokeball items collected
- Both values are displayed in the top-left corner of the screen

## Game Window

- Resolution: 800x600 pixels
- Title: "Pokemon_Hunt"
- Black background with custom background image

## Code Structure

### Main Variables
- `player_x`, `player_y` - Player position
- `pokemon_x`, `pokemon_y` - Pokémon sprite position (static)
- `coin_x` to `coin7_x`, `coin_y` to `coin7_y` - Individual coin positions
- `score` - Current score
- `pokeball` - Pokeball count

### Key Functions

- `player(x, y)` - Draw player sprite
- `pokemon(x, y)` - Draw Pokémon sprite
- `coin(x, y)` to `coin7(x, y)` - Draw individual coins
- `isCollision(px, py, cx, cy)` - Check if player collides with a collectible
  - Returns `True` if player position overlaps with collectible (64x64 pixel check)

## Potential Improvements

- Refactor repeated coin functions into a single function with parameters
- Add collision checks for screen boundaries to prevent player from moving off-screen
- Implement respawning collectibles at random positions
- Add difficulty levels or increasing speed
- Create an enemy/obstacle system
- Add a game over or win condition
- Optimize sound loading (currently loads sound on every collision detection)
- Use a data structure (list/dict) instead of individual variables for coins

## Known Issues

- Sound is loaded every frame during collision (performance concern)
- Player can move off-screen without boundary checking
- Coins don't respawn after collection
- No game-ending condition

## Author
still making in process

Created as a fun pygame learning project!
