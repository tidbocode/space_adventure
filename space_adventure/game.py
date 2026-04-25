from .rooms import Room, setup_rooms
from .items import Item
from .player import Player

import random

def main():
    print(r"""
       .        /^\      .         .        /^\
    .           |V|   .         .           |V|      .
        --[O]---' '---      _______      ---' '---[O]--
       /  EXPLORER    \    | ALIEN |    /    THREAT    \   *
      |________________|   |_______|   |________________|
     .      ||   ||           /V\           ||   ||      .
    ________||___||__________// \\__________||___||________
   (                                                       )
    )   .     O      .     [ ASTEROIDS ]     .      O     (
   (      .      .           #### ####           .      .  )
    )_____________________________________________________(
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
    last_event = None

    while alive:
        print(f"\nTurn {turns_survived + 1} of {turns_to_win}")
        if turns_survived < 3:
            possible_events = ["asteroid", "alien", "safe", "safe", "wormhole"]
        else:
            possible_events = ["asteroid", "alien", "safe", "safe", "blackhole", "wormhole"]
        if last_event == "safe" or last_event == "wormhole":
            possible_events = [e for e in possible_events if e not in ["safe", "wormhole"]]
        event = random.choice(possible_events)
        last_event = event
        skip_increment = False
        if event == "asteroid":
            print("Warning! An asteroid field is ahead.")
            action = input("Do you 'dodge' or 'brace'? ").strip().lower()
            if action == "dodge":
                if random.random() < 0.8:
                    print("You skillfully dodge the asteroids!")
                else:
                    print("You fail to dodge and your ship is destroyed!")
                    alive = False
            elif action == "brace":
                if random.random() < 0.4:
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
                if random.random() < 0.6:
                    print("You defeat the alien ship!")
                else:
                    print("The aliens overpower you. You are lost in space.")
                    alive = False
            elif action == "run":
                if random.random() < 0.7:
                    print("You escape the aliens!")
                else:
                    print("You fail to escape and are destroyed.")
                    alive = False
            else:
                print("You freeze and the aliens destroy your ship!")
                alive = False
        elif event == "blackhole":
            print("Warning! A massive black hole appears and pulls your ship in!")
            print("You are crushed by the immense gravity. Game over.")
            alive = False
        elif event == "wormhole":
            print("A mysterious wormhole opens before you!")
            if random.random() < 0.7:
                turns_survived += 1
                print("You emerge from the wormhole closer to your destination!")
            else:
                turns_survived += 2
                print("You emerge much closer to your destination!")
            skip_increment = True
        else:
            print("This part of space is calm. You travel safely.")

        if not alive:
            print(r"""
_ ._  _ , _ ._
        (_ ' ( `  )_  .__)
      ( (  (    )   `)  ) _)
     (__ (_   (_ . _) _) ,__)
         `~~`\ ' . /`~~`
              |   |
   -- ---  _(_   _)_  --- --
      _  __/_  (( _ )\_  _
     --      (  `  )     --
            __)  (__
            """)
            print("Game Over. Thanks for playing!")
            break
        else:
            if not skip_increment:
                turns_survived += 1
            if turns_survived >= turns_to_win:
                print(r"""
      / \
     /   \
    /     \
   /_______\
  |   ( )   |
  |  -----  |
  | |  O  | |
  | |  |  | |
  | |__/\_| |
 /  \_____/  \
|___ __|__ ___|
   |   |   |
   |   |   |
  / \ / \ / \
   v   v   v
       
      .....
   .:::::::::.
  :::::::::::::
  :::::::::::::    Bowen is a nerd :)
   ':::::::::'
      '''''
                """)
                print("\nCongratulations! You have reached an Earth-like planet and won the game!")
                break
                print(r"""
      / \
     /   \
    /     \
   /_______\
  |   ( )   |
  |  -----  |
  | |     | |
  | |     | |
  | |_____| |
 /  \_____/  \
|______|______|
   |   |   |
   |   |   |
  / \ / \ / \
   v   v   v
       
      .....
   .:::::::::.
  :::::::::::::
  :::::::::::::    Daddy is the coolest :)
   ':::::::::'
      '''''
                """)
                print("\nCongratulations! You have reached an Earth-like planet and won the game!")
                break

