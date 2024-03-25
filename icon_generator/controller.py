"""
controller.py
by Hundredvisionsguy
Python code to make API connections.
"""

import requests as re
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtWidgets import (
    QLabel,
    QSizePolicy,
    QVBoxLayout,
)

# build out the URL based on API docs
base_url = "https://api.dicebear.com/7.x/"
style = "bottts/"
filetype = "svg"
seed = "?seed=HundredVisionsGuy"

url = base_url + style + filetype + seed
response = re.get(url)


def get_icon_layout(icon_type: str) -> QVBoxLayout:
    """return a vbox layout with an avatar and label.

    Arguments:
        icon_type: the type of icon we will display.

    Returns:
        icon_layout: a vbox layout with an avatar and label.
    """
    icon_layout = QVBoxLayout()
    folder = "resources/images/"
    filepath = folder + icon_type + "_avatar.svg"
    avatar_svg = QSvgWidget(filepath)
    avatar_svg.setFixedSize(64, 64)
    label = icon_type.replace("_", " ")
    avatar_label = QLabel(label)
    icon_layout.addWidget(avatar_svg)
    icon_layout.addWidget(avatar_label)
    return icon_layout


if response.ok:
    print(response.text)
else:
    print(f"There was an error: {response.status_code}")
