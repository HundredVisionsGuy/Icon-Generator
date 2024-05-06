"""
controller.py
by Hundredvisionsguy
Python code to make API connections.
"""

import requests as re

# build out the URL based on API docs
base_url = "https://api.dicebear.com/8.x/"
default_style = "bottts"
filetype = "svg"
default_seed = "HundredVisionsGuy"


def call_api(style=default_style, seed=default_seed):
    """make API call to Dicebear.

    The seed and style parameters are optional, so if the user doesn't provide
    a style or seed, it will use the default values.

    If the call is unsuccessful, it will return an error code
    and an error message.

    Args:
        style: the style of avatar to get.
        seed: a text seed to randomize the avatar.

    Returns:
        response: the text of the response or an error.
    """
    url = f"{base_url}{style}/svg?seed={seed}"
    response = re.get(url)
    if response.ok:
        return response.text
    else:
        return f"Error: {response.status_code} - {response.reason}"


def get_avatar(style: str, seed: str) -> str:
    """returns an svg from a dicebear API call"""
    response = call_api(style, seed)
    return response


def get_avatar_type(avatar_path: str) -> str:
    """returns the avatar type from the avatar_path
    Args:
        avatar_path: the relative path to the avatar.

    Returns:
        avatar_type: the type of avatar"""
    avatar_type = ""
    filename = avatar_path.split("/")[-1]
    avatar_type = filename.split("_")[0]
    return avatar_type


def get_file_contents(path: str) -> str:
    """returns the contents of a file.

    Args:
        path: path to file

    Returns:
        contents: file contents
    """
    contents = ""
    with open(path, "r", encoding='utf-8') as f:
        contents = f.read()
    return contents


if __name__ == "__main__":
    # test
    avatar_code = call_api("pixel-art", "phred")
    print(avatar_code)
