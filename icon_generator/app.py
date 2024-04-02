import sys
import controller
from PyQt6.QtCore import Qt
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Avatar-inator")
        self.resize(320, 240)

        # Initialize Widgets
        title_label = QLabel("Avatar-inator",
                             alignment=Qt.AlignmentFlag.AlignHCenter)

        self.avatar_main_path = "resources/images/bottts_avatar.svg"
        self.avatar_main = QSvgWidget(self.avatar_main_path)

        # Seed input
        self.seed_input = QLineEdit("")
        self.seed_input.setPlaceholderText("Add text to customize")

        # Get avatar button
        self.get_avatar_button = QPushButton("Get Avatar")

        # Avatar icons
        # TODO: Turn these into custom widgets and set size
        self.pixel_icon = QSvgWidget("resources/images/pixel_art_avatar.svg")
        self.adventurer_icon = QSvgWidget("resources/images/adventurer_avatar.svg")
        self.bottts_icon = QSvgWidget("resources/images/bottts_avatar.svg")
        self.croodles_icon = QSvgWidget("resources/images/croodles_avatar.svg")
        self.identicon_icon = QSvgWidget("resources/images/identicon_avatar.svg")
        self.lorelei_icon = QSvgWidget("resources/images/lorelei_avatar.svg")
        self.rings_icon = QSvgWidget("resources/images/rings_avatar.svg")
        self.shapes_icon = QSvgWidget("resources/images/shapes_avatar.svg")

        layout = QGridLayout()

        # Insert widgets into the layout
        layout.addWidget(title_label, 0, 0, 1, 4)
        layout.addWidget(self.avatar_main, 1, 1, 1, 2,
                         alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.seed_input, 2, 0, 1, 3)
        layout.addWidget(self.get_avatar_button, 2, 3, 1, 1)
        layout.addWidget(self.pixel_icon, 3, 0)
        layout.addWidget(self.adventurer_icon, 3, 1)
        layout.addWidget(self.bottts_icon, 3, 2)
        layout.addWidget(self.croodles_icon, 3, 3)
        layout.addWidget(self.identicon_icon, 4, 0)
        layout.addWidget(self.lorelei_icon, 4, 1)
        layout.addWidget(self.rings_icon, 4, 2)
        layout.addWidget(self.shapes_icon, 4, 3)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
