import time
from gameData.globals import defaultPause


def print_pause(line, pause=defaultPause):
    print(line)
    time.sleep((len(line)/pause) + 0.25)


def monologue(lines, pause=defaultPause):
    [print_pause("  " + line, pause) for line in lines]
    print("")


def narrate(lines, pause=defaultPause):
    print("")
    [print_pause(line, pause) for line in lines]
    print("")


def prompt(options):
    print("")
    playerInput = ''
    while playerInput not in map(lambda x: f'{x}', range(len(options))):
        print("do you:")
        for index, option in enumerate(options):
            print('  (' + str(index) + ") : " + option)
        playerInput = input("")
        print("")
    return playerInput
