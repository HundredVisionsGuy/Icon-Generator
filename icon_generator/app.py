import file_clerk.clerk as clerk
import sys
from PyQt6.QtCore import QEvent, Qt
from PyQt6.QtGui import QEnterEvent, QPalette, QColor, QFontDatabase, QFont
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtWidgets import (
    QApplication,
    QGraphicsScene,
    QGraphicsView,
    QGridLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PyQt6.QtWebEngineWidgets import QWebEngineView


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Widgets App")
        self.setContentsMargins(24, 24, 24, 24)  # NEW - adds margin
        self.set_fonts()

        # Title
        title_label = QLabel("Avatar-inator",
                             alignment=Qt.AlignmentFlag.AlignHCenter)
        title_label.setFont(QFont("Knewave", 24))

        # Main Avatar
        self.avatar_main_display = QWebEngineView()
        self.avatar_main_display.setFixedSize(240, 240)
        self.avatar_main_display.setContentsMargins(5, 5, 5, 5)
        self.avatar_main_svg = "resources/images/bottts_avatar.svg"
        avatar_svg = clerk.file_to_string(self.avatar_main_svg)
        self.avatar_main_display.setHtml(avatar_svg)

        # Let user choose a text seed
        self.seed_input = QLineEdit("")
        self.seed_input.setFont(QFont("Montserrat", 12, 1))
        self.seed_input.setPlaceholderText("Add text to customize")

        self.get_avatar_button = QPushButton("Get Avatar")
        self.get_avatar_button.setFont(QFont("Montserrat"))

        # Icon button widgets
        pixel_slot_layout = IconWidget("pixel_art")
        adventurer_slot_layout = IconWidget("adventurer")
        botts_slot_layout = IconWidget("bottts")
        croodles_slot_layout = IconWidget("croodles")
        identicon_slot_layout = IconWidget("identicon")
        lorelei_slot_layout = IconWidget("lorelei")
        rings_slot_layout = IconWidget("rings")
        shapes_slot_layout = IconWidget("shapes")

        layout = QGridLayout()

        # Add widgets to the layout
        layout.addWidget(title_label, 0, 0, 1, 4)
        layout.addWidget(self.avatar_main_display, 1, 1, 2, 2)
        layout.addWidget(self.seed_input, 3, 0, 1, 3)
        layout.addWidget(self.get_avatar_button, 3, 3, 1, 1)
        layout.addWidget(pixel_slot_layout, 4, 0, 1, 1)
        layout.addWidget(adventurer_slot_layout, 4, 1, 1, 1)
        layout.addWidget(botts_slot_layout, 4, 2, 1, 1)
        layout.addWidget(croodles_slot_layout, 4, 3, 1, 1)
        layout.addWidget(identicon_slot_layout, 5, 0)
        layout.addWidget(lorelei_slot_layout, 5, 1)
        layout.addWidget(rings_slot_layout, 5, 2)
        layout.addWidget(shapes_slot_layout, 5, 3)

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
        avatar_label = QLabel(label, alignment=Qt.AlignmentFlag.AlignHCenter)
        avatar_label.setFont(QFont("Knewave", 12))
        icon_layout.addWidget(avatar_svg,
                              alignment=Qt.AlignmentFlag.AlignHCenter)
        icon_layout.addWidget(avatar_label)
        return icon_layout


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


class IconWidget(QWidget):
    def __init__(self, icon_type: str):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setMouseTracking(True)

        folder = "resources/images/"
        filepath = folder + icon_type + "_avatar.svg"

        avatar_svg = QSvgWidget(filepath)
        avatar_svg.setFixedSize(60, 60)

        # Set Button
        title = icon_type.replace("_", " ")
        label_text = self.scene.addText(title,
                                        QFont("Knewave", 12))
        label_text.setPos(10, 64)

        avatar_widget = self.scene.addWidget(avatar_svg)
        avatar_widget.setPos(14, 6)
        view = QGraphicsView(self.scene)
        vbox = QVBoxLayout()
        vbox.addWidget(view)
        self.setLayout(vbox)
        self.setStyleSheet("border: 0 solid;")
        self.setFixedSize(110, 120)

    def enterEvent(self, event: QEnterEvent) -> None:
        self.setStyleSheet(
            "background-color: #fff; border: 1px solid #336699;"
            )
        return super().enterEvent(event)

    def leaveEvent(self, a0: QEvent) -> None:
        self.setStyleSheet("border: none;")
        return super().leaveEvent(a0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    stylesheet = None
    styles_path = "resources/styles.qss"
    with open(styles_path, "r") as f:
        stylesheet = f.read()
    app.setStyleSheet(stylesheet)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()

    app.exec()
