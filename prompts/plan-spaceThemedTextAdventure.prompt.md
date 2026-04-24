Plan: Space-Themed Text Adventure (Oregon Trail Style)

A Python terminal-based text adventure for 1 or 2 players (turn-based), featuring open-source and simple custom ASCII art. Players journey through space toward a new Earth-like planet. The goal is to survive random events and reach the destination; players can lose if they die along the way. The number of turns (journey length) is randomized between 15 and 30.

Steps

Phase 1: Project Setup
1. Initialize a Python project structure.
2. Create main game script and supporting modules (game logic, player management, ASCII art).
3. Prepare a Dockerfile for running the game in a container.

Phase 2: Core Game Logic
4. Implement player selection (1 or 2 players, turn-based).
5. Design the main game loop:
    - Present story and choices.
    - Handle random events (e.g., asteroid fields, system failures, alien encounters).
    - Track player status (health, supplies, progress).
    - Randomize journey length (15–30 turns).
6. Implement win/lose conditions (reach planet or die).

Phase 3: ASCII Art Integration
7. Use open-source and simple custom ASCII art for:
    - Splash screen
    - Key events (e.g., spaceship, planets, hazards)
    - Victory/defeat screens

Phase 4: User Experience
8. Add clear prompts, input validation, and turn management.
9. Ensure replayability (randomized events, different outcomes).

Phase 5: Dockerization
10. Write a Dockerfile to run the game.
11. Add instructions for building and running the container.

Relevant files
- main.py — Entry point, game loop
- game.py — Game logic and event handling
- player.py — Player state and actions
- ascii_art.py — ASCII art definitions and display functions
- Dockerfile — Container setup

Verification
1. Run the game locally and in Docker to ensure it works as expected.
2. Test both 1 and 2 player modes.
3. Confirm ASCII art displays correctly in the terminal.
4. Validate win/lose conditions, event randomness, and journey length (15–30 turns).

Decisions
- 2-player mode is turn-based, sharing the same terminal.
- Space adventure theme inspired by Oregon Trail.
- Win by reaching a new planet; lose by dying from random events.
- ASCII art will be open-source or simple custom designs.
- Journey length is randomized between 15 and 30 turns.
