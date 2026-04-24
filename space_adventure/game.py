from .rooms import Room, setup_rooms
from .items import Item
from .player import Player

import random

def main():
        print(r"""
           .      /^\      .         .         /^\
    .             |V|   .         .            |V|      .
          --[O]---' '---      _______      ---' '---[O]--
       * /  EXPLORER    \    | ALIEN |    /    THREAT    \   *
        |________________|   |_______|   |________________|
     .      ||   ||           /V\           ||   ||      .
    ________||___||__________// \\__________||___||________
   (                                                       )
    )   .     O      .     [ ASTEROIDS ]     .      O     (
   (      .      .           #### ####           .      .  )
    )_____________________________________________________(')
             _..._             _..._             _..._
           .'     '.         .'     '.         .'     '.
         * | (o)(o) |   .    | (o)(o) |        | (o)(o) |     .
            \  __  /          \  __  /          \  __  /
             '____'            '____'            '____'
        """)
        print("Welcome to Space Adventure!")
        print("Your mission: Survive the journey to an Earth-like planet.")
    turns_to_win = 5
    turns_survived = 0
    alive = True

    while alive:
        print(f"\nTurn {turns_survived + 1} of {turns_to_win}")
        event = random.choice(["asteroid", "alien", "safe"])
        if event == "asteroid":
            print("Warning! An asteroid field is ahead.")
            action = input("Do you 'dodge' or 'brace'? ").strip().lower()
            if action == "dodge":
                if random.random() < 0.7:
                    print("You skillfully dodge the asteroids!")
                else:
                    print("You fail to dodge and your ship is destroyed!")
                    alive = False
            elif action == "brace":
                if random.random() < 0.3:
                    print("You survive the impact, but your ship is damaged.")
                else:
                    print("The asteroid impact destroys your ship!")
                    alive = False
            else:
                print("You hesitate and are hit by an asteroid!")
                alive = False
        elif event == "alien":
            print("Alert! An alien ship is attacking!")
            action = input("Do you 'fight' or 'run'? ").strip().lower()
            if action == "fight":
                if random.random() < 0.5:
                    print("You defeat the alien ship!")
                else:
                    print("The aliens overpower you. You are lost in space.")
                    alive = False
            elif action == "run":
                if random.random() < 0.6:
                    print("You escape the aliens!")
                else:
                    print("You fail to escape and are destroyed.")
                    alive = False
            else:
                print("You freeze and the aliens destroy your ship!")
                alive = False
        else:
            print("This part of space is calm. You travel safely.")

        if alive:
            turns_survived += 1
            if turns_survived >= turns_to_win:
                print("\nCongratulations! You have reached an Earth-like planet and won the game!")
                break
        else:
            print("Game Over. Thanks for playing!")
