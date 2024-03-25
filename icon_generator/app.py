import sys
from PyQt6.QtGui import QPalette, QColor, QFontDatabase, QFont
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QGridLayout,
    QVBoxLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Widgets App")
        self.setContentsMargins(24, 24, 24, 24)  # NEW - adds margin
        self.set_fonts()

        # Title
        title_label = QLabel("Avatar-inator")
        title_label.setFont(QFont("Knewave", 24))

        # Main Avatar
        self.avatar_main_svg = QSvgWidget("resources/images/bottts_avatar.svg")

        # Let user choose a text seed
        self.seed_input = QLineEdit("")
        self.seed_input.setFont(QFont("Montserrat"))

        self.get_avatar_button = QPushButton("Get Avatar")
        self.get_avatar_button.setFont(QFont("Montserrat"))

        # Icon button widgets
        pixel_slot_layout = self.get_icon_layout("pixel_art")
        adventurer_slot_layout = self.get_icon_layout("adventurer")
        botts_slot_layout = self.get_icon_layout("bottts")
        croodles_slot_layout = self.get_icon_layout("croodles")
        identicon_slot_layout = self.get_icon_layout("identicon")
        lorelei_slot_layout = self.get_icon_layout("lorelei")
        rings_slot_layout = self.get_icon_layout("rings")
        shapes_slot_layout = self.get_icon_layout("shapes")

        layout = QGridLayout()

        # Add widgets to the layout
        layout.addWidget(title_label, 0, 0, 1, 4)
        layout.addWidget(self.avatar_main_svg, 1, 1, 2, 2)
        layout.addWidget(self.seed_input, 3, 0, 1, 3)
        layout.addWidget(self.get_avatar_button, 3, 3, 1, 1)
        layout.addLayout(pixel_slot_layout, 4, 0, 1, 1)
        layout.addLayout(adventurer_slot_layout, 4, 1, 1, 1)
        layout.addLayout(botts_slot_layout, 4, 2, 1, 1)
        layout.addLayout(croodles_slot_layout, 4, 3, 1, 1)
        layout.addLayout(identicon_slot_layout, 5, 0)
        layout.addLayout(lorelei_slot_layout, 5, 1)
        layout.addLayout(rings_slot_layout, 5, 2)
        layout.addLayout(shapes_slot_layout, 5, 3)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def set_fonts(self):
        # import fonts
        font_dir = "resources/fonts/"
        title_font_name = "Knewave-Regular.ttf"
        title_font_path = font_dir + "Knewave/" + title_font_name
        regular_font_path = font_dir + "/Montserrat/"
        regular_font_path += "Montserrat-VariableFont_wght.ttf"
        success = QFontDatabase.addApplicationFont(title_font_path)
        if success == -1:
            print(f"{title_font_name} not loaded")
        success = QFontDatabase.addApplicationFont(regular_font_path)
        if success == -1:
            print("Regular font not loaded.")

    def get_icon_layout(self, icon_type: str) -> QVBoxLayout:
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
        avatar_label.setFont(QFont("Knewave", 12))
        icon_layout.addWidget(avatar_svg)
        icon_layout.addWidget(avatar_label)
        return icon_layout


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    stylesheet = None
    styles_path = "resources/styles.qss"
    with open(styles_path, "r") as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet)
    window = MainWindow()
    window.show()

    app.exec()
