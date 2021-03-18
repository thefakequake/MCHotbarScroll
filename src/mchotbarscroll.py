from os import path
from json import dumps, load
from pynput import keyboard, mouse
import time
from random import randint

print("Welcome to MCHotbarScroll!\n")

# Checks if the file exists
if not path.exists("config.json"):
    with open("config.json", "w+") as file:

        # JSON template
        template_dict = {
            "reverse": "false",
            "speed": 5,
        }

        # Formats the dict into JSON and writes it to the new file
        file.write(dumps(template_dict, indent=4))


with open("config.json", "r") as file:
    config = load(file)


# Parses the "reverse" value in config.json to a bool
if config["reverse"].lower() not in ("true", "false"):
    config["reverse"] = False
    print("Invalid \"reverse\" value in JSON file! It must only be either true or false. Defaulting to \"false\".")


if not isinstance(config["speed"], int):
    


config["reverse"] = config["reverse"].lower() == "true"


mouse = mouse.Controller()
keyboard = keyboard.Controller()


while True:
    if config["reverse"]:
        scroll_amount = randint(-config["speed"], config["speed"])
    else:
        scroll_amount = config["speed"]

    mouse.scroll(0, scroll_amount)

    time.sleep(1/scroll_amount)
