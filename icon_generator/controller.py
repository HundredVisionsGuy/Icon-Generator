"""
controller.py
by Hundredvisionsguy
Python code to make API connections.
"""

import requests as re


# build out the URL based on API docs
base_url = "https://api.dicebear.com/7.x/"
filetype = "svg"


def get_avatar(style: str, seed: str) -> str:
    """returns an svg from dicebear

    Args:
        style: style of avatar.
        seed: any text (name, word, phrase) will be used to customize
            the avatar

    Returns:
        svg: the SVG code from dicebear API
    """
    style = style + "/"
    seed = "?seed=" + seed
    url = base_url + style + filetype + seed
    response = re.get(url)
    if response.ok:
        svg = response.text
    else:
        svg = f"Error: {response.status_code}"
    return svg


if __name__ == '__main__':
    result = get_avatar("bottts", "stuffy stuff")
    print(result)
