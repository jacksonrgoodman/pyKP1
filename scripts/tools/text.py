import os
import sys
import time


def type_text(input):
    for character in input:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def console_clear():
    os.system('cls')
