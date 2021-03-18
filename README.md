# MCHotbarScroll

## Features
- Global keybinds to pause scrolling and kill the program.
- Configurable JSON file to adjust scrolling speed, keybinds and other settings.
- Built in error handlers to diagnose issues like JSON formatting.
- Lightweight and efficient, only one external library used.

## Coming soon
- .exe build for added portability and ease of use.

## How to run
Make sure you have a Python installation of at least Python 3.7 and install the module `pynput` via pip:
```python
pip install pynput
```
Then run `mchotbarscroll.py` and it will generate a JSON file for you to configure.

Every time you make changes to the settings, you __must__ restart the program for the changes to take effect.
