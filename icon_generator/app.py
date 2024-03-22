import sys
import controller
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QGridLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")
        self.setContentsMargins(24, 24, 24, 24)  # NEW - adds margin

        layout = QGridLayout()

        # Title
        title_label = QLabel("Avatar-inator")

        # Main Avatar
        self.avatar_main_svg = QSvgWidget("resources/images/botts_avatar.svg")

        # Let user choose a text seed
        self.seed_input = QLineEdit("")

        self.get_avatar_button = QPushButton("Get Avatar")

        # Icon button widgets
        pixel_slot_layout = controller.get_icon_layout("lorelei")
        adventurer_slot_layout = controller.get_icon_layout("identicon")

        # Add widgets to the layout
        layout.addWidget(title_label, 0, 0, 1, 4)
        layout.addWidget(self.avatar_main_svg, 1, 1, 2, 2)
        layout.addWidget(self.seed_input, 3, 0, 1, 3)
        layout.addWidget(self.get_avatar_button, 3, 3, 1, 1)
        layout.addLayout(pixel_slot_layout, 4, 0, 1, 1)
        layout.addLayout(adventurer_slot_layout, 4, 1, 1, 1)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
