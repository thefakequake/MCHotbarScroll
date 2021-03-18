from json import dumps


template_dict = {
    "speed": 10,
    "toggle_key": "y",
    "quit_key": "u",
    "reverse": "true",
    "output_to_console": "true"
}


def generate_json():
    with open("config.json", "w+") as file:
        # JSON template
        # Formats the dict into JSON and writes it to the new file
        file.write(dumps(template_dict, indent=4))


def try_parse(content, type_converter):
    try:
        output = type_converter(content)
        return output
    except ValueError:
        return None
