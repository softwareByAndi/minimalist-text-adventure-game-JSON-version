"""
- display opening monologue
- prompt user input
- take user input
- compare input with branch options
- choose which dialogue to display based on results of input comparison
- rinse and repeat

1. we could create a JSON file with all of our dialogue
2. or we can create a number of different python scripts
    for each section of the game
3. or just monolith code -- all dialogue and logic is in a single file.

this program is the JSON version
"""

import json
import importlib
import random
import event
from services import speak
from gameData import globals


def play_game():
    dialogue_file_name = 'game_start'
    while not globals.game_over:
        script = open("scripts/" + dialogue_file_name + '.json')
        script = json.load(script)
        for entry in script['dialogue']:
            if entry['name'] == "":
                speak.narrate(entry['dialogue'])
            else:
                print(f"{entry['name']} : ")
                speak.monologue(entry['dialogue'])

            if 'events' in entry:
                [
                    event.run(entry['events'], index)
                    for index in range(len(entry['events']))
                ]

        next_scene = None
        playerDecision = None
        if 'next_scene' in script:
            next_scene = script['next_scene']
        elif 'prompt' in script:
            while next_scene is None:
                playerDecision = speak.prompt(script['prompt']['options'])
                try:
                    playerDecision = int(playerDecision)
                    next_scene = script["prompt"]['next_scene'][playerDecision]
                except Exception:
                    next_scene = None
                    playerDecision = None
                    print("invalid input")
            if 'events' in script['prompt']:
                event.run(script['prompt']['events'], playerDecision)
        else:
            globals.game_over = True

        dialogue_file_name = next_scene


while not globals.game_over:
    speak.narrate(random.choice([
        ["Greetings traveler.", "Your adventure awaits you!"],
        ["Get ready!", "Get set!", "Adventure!"],
        [
            "By playing this game, you accept all responsibility for any "
            "harm that may occur during or as a result of this game,",
            "and you agree to not hold 'softwareByAndi' or any related "
            "parties responsible,",
            "neither will you pursue any legal action against any party "
            "related to the production of this game."
        ],
        ["Don't forget your wallet...", "Or your Adventurer spirit!"],
        [
            "Booting Reality...",
            "",
            "~Error...",
            "~~Error...",
            "~~~Err~E~rro~rr~~or...",
            "",
            "Reality does not exist!"
        ]
    ]))
    play_game()
    playerDecision = speak.prompt(['play again', 'quit'])
    if playerDecision == '0':
        globals.game_over = False

print("exiting game...")
print("")
