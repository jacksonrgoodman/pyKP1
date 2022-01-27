# Karma Police
# Developed by Jackson Goodman © 2022

import cmd
import mimetypes
import sys
import textwrap
# import sys
# import os
import time
import random
from scripts.engine.zone_map import zone_map
from scripts.engine.zone_map import location_card as print_location
from scripts.engine.actors import Player
from scripts.tools.text import type_text
from scripts.tools.text import console_clear
from scripts.engine.functions import game_quit

screen_width = 100

# Meta Tools


# def type_text(input):
#     for character in input:
#         sys.stdout.write(character)
#         sys.stdout.flush()
#         time.sleep(0.05)

# Ingame Tools

# ? Player


# class Player:
#     def __init__(self):
#         self.name = ""
#         self.hp = 0
#         self.ap = 0
#         self.pp = 0
#         self.job = ""
#         self.won = False
#         self.status_effects = []
#         self.location = "b2"


myplayer = Player()
myplayer.location = "b2"

# ? Title Screen


def title_scren_options():
    option = input("> ").lower()
    if option == ("play"):
        setup_game()
    elif option == ("help"):
        help_menu()
    elif option == ("quit"):
        game_quit()
    while option not in ('play', 'help', 'quit'):
        print("please enter a valid command.")
        option = input("> ")


def title_screen():
    console_clear()
    print('#####################################')
    print('#              Welcome              #')
    print('#####################################')
    print()
    print('               -Play-                ')
    print('               -Help-                ')
    print('               -Quit-                ')
    print()
    print('  Copyright © 2022 Jackson Goodman   ')
    title_scren_options()


def help_menu():
    console_clear()
    print('#####################################')
    print('#               Help                #')
    print('#####################################')
    print()
    print('   -use Arrow Keys(^v<>) to move-    ')
    print('   -type your commands to do them-   ')
    print('  -use "look" to inspect something-  ')
    print()
    print('       -Good Luck, Have Fun-         ')
    title_scren_options()

# ? Game Start


# def start_game():

    # Map
    # ''
    # '---------------------'
    # '| A1 | A2 | A3 | A4 | '
    # '--------------------- '
    # '| B1 | B2 | B3 | B4 | '
    # '--------------------- '
    # '| C1 | C2 | C3 | C4 | '
    # '--------------------- '
    # '| D1 | D2 | D3 | D4 | '
    # '--------------------- '
    # 'ZONENAME' = ''
    # 'DESCRIPTION' = 'description'
    # 'EXAMINATION' = 'examine'
    # 'SOLVED' = False
    # 'UP' = 'up', 'north'
    # 'DOWN' = 'down', 'south'
    # 'LEFT' = 'left', 'east'
    # 'RIGHT' = 'right', 'west'


solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': True, 'b3': False, 'b4': False,
                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
                 'd1': False, 'd2': False, 'd3': False, 'd4': False}


# Game Interaction


# def print_location():
#     print('\n' + ('#' * (4 * len(myplayer.location))))
#     print('\n# ' + myplayer.location + ' #')
#     print('\n' + ('#' * (4 + len(myplayer.location))))
#     print('| ' + zone_map[myplayer.location]['DESCRIPTION'] + ' |')
#     print(
#         '\n|' + ('_' * (4 + len(zone_map[myplayer.location]['DESCRIPTION'])))+'|')


def prompt():
    print('\n=================================')
    print('What would you like to do?')
    action = input('> ').lower()
    acceptable_actions = ['move', 'go', 'travel', 'walk',
                          'quit', 'examine', 'interact', 'inspect', 'look']
    while action not in acceptable_actions:
        # ! make this line more interesting
        print("Unknown action. Try again.")
        action = input('> ').lower()
    if action == 'quit':
        # ! Refactor to include safety. make function? 1. YES NO 2. game_quit $ game_exit
        game_quit()
    elif action in ['move', 'go', 'travel', 'walk']:
        player_move(action)
    elif action in ['examine', 'interact', 'inspect', 'look']:
        player_examine(action)


def player_move(myAction):
    ask = "Where do you want to move to?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zone_map[myplayer.location]['UP']
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zone_map[myplayer.location]['DOWN']
        movement_handler(destination)
    elif dest in ['left', 'east']:
        destination = zone_map[myplayer.location]['LEFT']
        movement_handler(destination)
    elif dest in ['right', 'west']:
        destination = zone_map[myplayer.location]['RIGHT']
        movement_handler(destination)


# Game Functionality
def main_game_loop():
    total_puzzles = 6
    while myplayer.won is False:
        # print_location()
        prompt()


def movement_handler(destination):
    # print("\nYou have moved to the "+destination+".")
    myplayer.location = destination
    print_location(zone_map[myplayer.location]['ID'])


def player_examine(action):
    if zone_map[myplayer.location]['SOLVED']:
        # ? Exhausted
        print("You have already exhausted this zone.")
    else:
        # ? Trigger
        print('\nYou can trigger events here.')


def start_game():
    return


# def main_game_loop():
#     prompt()
    # ? handle if game events have been resolved
    # ! BUILD


def setup_game():
    console_clear()

    question1 = 'Name?'  # ! refactor
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input('> ')
    myplayer.name = player_name

    question2 = 'Job?'  # ! refactor
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_job = input('> ').lower()
    myplayer.name = player_name
    valid_jobs = ['warrior', 'priest', 'mage']
    if player_job in valid_jobs:
        myplayer.job = player_job
    while player_job not in valid_jobs:
        player_job = input('> ').lower()
        print('you are now a '+myplayer.job+'.')

    # Player Stats
    if myplayer.job == 'warrior':
        myplayer.hp = 120
        myplayer.ap = 50
        myplayer.pp = 10

    if myplayer.job == 'priest':
        myplayer.hp = 100
        myplayer.ap = 120
        myplayer.pp = 30

    if myplayer.job == 'mage':
        myplayer.hp = 30
        myplayer.ap = 220
        myplayer.pp = 50

    question3 = 'Hello '+player_name+' the '+player_job+'.'  # ! refactor
    type_text(question3)

    speech = '\nWelcome to Karma Police, '+myplayer.job + \
        ' '+myplayer.name+'.\n\nTESTTEST\nTEST\n'
    type_text(speech)
    # playconsole_clear()
    print('##########################')
    print("#    Let's Start Now!    #")
    print('##########################')
    main_game_loop()


title_screen()
