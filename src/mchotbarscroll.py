# builtin imports
from os import path
from json import load, decoder
from random import randint
from time import sleep, localtime, strftime

# lib imports
from pynput import keyboard, mouse

# internal imports
import utils


print("Welcome to MCHotbarScroll!")
print("You can configure this program by editing the \"config.json\" file in this file's directory. If you encounter"
      " any JSON errors and don't know how to fix them, delete the JSON file and restart the program.")

# Checks if the file exists
if not path.exists("config.json"):
    utils.generate_json()


with open("config.json", "r") as file:
    try:
        config = load(file)
    # Catches errors in JSON formatting and prints the error
    except decoder.JSONDecodeError as e:
        print(f"Error: JSON file is formatted incorrectly: \"{str(e).strip('decoder.JSONDecodeError: ')}\"")
        exit()
    if False in [default_key in list(config.keys()) for default_key in list(utils.template_dict.keys())]:
        print("Error: Missing required JSON keys in config.json! Delete the file and run this program again!")
        exit()

# Parses speed value to an integer; in case they formatted it as a string
if not isinstance(config["speed"], int):
    parsed_int = utils.try_parse(config["speed"], int)

    # Block executes if the "speed" value can't be parsed to an int
    if parsed_int is None:
        print("Warning: Invalid \"speed\" value in JSON file! The value must be an integer. Defaulting to 10...")
        parsed_int = 10

    config["speed"] = parsed_int

# Verifies the value given isn't too extreme
if not (-100 <= config["speed"] <= 100):
    config["speed"] = 10
    print("Warning: \"speed\" value must be between -100 and 100! Defaulted value to 10.")

# Parses the "reverse" and "output_to_console" values in config.json to bools

for key in ("reverse", "output_to_console"):

    if config[key].lower() not in ("true", "false"):
        config[key] = True
        print(f"Warning: Invalid \"{key}\" value in JSON file! It must only be either true or false. Defaulting to "
              f"\"true\".")

    config[key] = config[key].lower() == "true"


mouse_c = mouse.Controller()
keyboard_c = keyboard.Controller()


# Controls whether to scroll or not; set this to True if you want the program to start scrolling upon startup
toggled = False
running = True

def release(key):
    global toggled
    global running

    # Makes sure the key object refers to an alphanumeric key so that we can call the .char attribute without errors
    if not isinstance(key, keyboard._win32.KeyCode):
        return

    if key.char == config["toggle_key"]:
        toggled = not toggled
        if config["output_to_console"]:
            print(f"{strftime('%H:%M:%S', localtime())}: Scrolling toggled: {str(toggled).lower()}")
    elif key.char == config["quit_key"]:
        print(f"{strftime('%H:%M:%S', localtime())}: Program ended")
        running = False


# Creates and starts the listener so that the program can listen for keyboard inputs
listener = keyboard.Listener(on_release=release)
listener.start()

print(f"\nPress '{config['toggle_key']}' to start scrolling, and '{config['quit_key']}' to quit the program...\n")

if config["reverse"]:
    reverse_scrolls = 0

while True:
    # Quits the program
    if not running:
        exit()

    # If scrolling is not toggled, skip to next iteration
    if not toggled:
        continue

    if config["reverse"]:
        if reverse_scrolls == 0:
            config["speed"] = -config["speed"]
            reverse_scrolls = randint(5, 14)
        else:
            reverse_scrolls -= 1

    # scrolls a single hotbar slot
    mouse_c.scroll(0, -5 if config["speed"] > 0 else 5)

    # Adds delay between scrolls
    sleep(1/abs(config["speed"]))
