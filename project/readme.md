# CL Spiel

**Developer:** Cong Loi Le

CL Spiel is a simple text-based adventure game created as a Python programming project.

The player explores different rooms, collects items, performs eco-friendly actions, and tries to complete the selected activity with the highest possible score.

## Objectives

The main objectives of the project are to practice:

- Python classes and objects
- Functions and program structure
- File handling
- JSON save and load functionality
- Multiple player profiles
- Game state management
- Basic scoring and high score system

## Gameplay

The player can choose between three activities:

- Jogging
- Work
- Shopping

Each activity has different win conditions:

- **Jogging:** Key + Shoes + 3 eco actions
- **Work:** Key + Shoes + 2 eco actions
- **Shopping:** Key + Shoes + Phone + 1 eco action

Other items are optional and may affect the final score.

When the win conditions are met in the Hall, the player can either leave and finish the game or continue exploring to improve the final score.

Available game commands include:

- move
- collect
- eco
- save
- load
- inventory
- menu

## Project Structure

- `personalinfo.py` – main program, menus, gameplay, save/load and scoring
- `player.py` – Player class
- `room.py` – Room class
- `item.py` – Item class
- `intro.txt` – game introduction
- `instructions.txt` – gameplay instructions
- `about.txt` – information about the game
- `savegames.json` – saved player profiles
- `highscores.json` – player high scores

## Progress

- Project 2: Completed
- Project 3: Completed
- Project 4: Completed
- Project 5: Completed
