"""Destroy after recording.

Code here is for the video only - when I need working code that I
will go over on the next video.

If I have a successful video posted, I can delete the code below.
"""

"""
from app.py
"""
class IconWidget(QWidget):
    selected = pyqtSignal(str)

    def __init__(self, icon_type: str):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setMouseTracking(True)
        self.icon_type = icon_type

        folder = "resources/images/"
        self.filepath = folder + icon_type + "_avatar.svg"

        avatar_svg = QSvgWidget(self.filepath)
        avatar_svg.setFixedSize(60, 60)

        # Set Button
        title = icon_type.replace("_", " ")
        label_text = self.scene.addText(title,
                                        QFont("Knewave", 12))
        label_text.setPos(8, 64)

        avatar_widget = self.scene.addWidget(avatar_svg)
        avatar_widget.setPos(18, 6)
        view = QGraphicsView(self.scene)
        vbox = QVBoxLayout()
        vbox.addWidget(view)
        self.setLayout(vbox)
        self.setFixedSize(130, 140)

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        self.selected.emit(self.filepath, self.icon_type)
        return super().mousePressEvent(a0)



"""
controller.py
by Hundredvisionsguy
Python code to make API connections.
"""

import requests as re
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtWidgets import (
    QLabel,
    QVBoxLayout,
)

# build out the URL based on API docs
BASE_URL = "https://api.dicebear.com/7.x/"
FILETYPE = "svg"


def call_api(style="bottts/", seed="") -> str:
    """make api call to dicebear"""
    url = BASE_URL + style + FILETYPE + seed
    response = re.get(url)
    if response.ok:
        return response.text
    else:
        return f"There was an error: {response.status_code}"


def get_file_contents(path: str) -> str:
    """get the contents from a file

    Args:
        path: path to the svg file

    Returns:
        contents: the svg code in the file."""
    contents = ""
    with open(path, "r") as f:
        contents = f.read()
    return contents


if __name__ == "__main__":
    api_response = call_api()
    print(api_response)
