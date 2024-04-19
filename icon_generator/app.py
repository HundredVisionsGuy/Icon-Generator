import sys
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtGui import QFont, QFontDatabase, QMouseEvent
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import (
    QApplication,
    QGraphicsScene,
    QGraphicsView,
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
        super().__init__()

        self.setWindowTitle("Widgets App")
        self.resize(640, 580)
        self.set_fonts()

        layout = QGridLayout()

        # Title
        title_label = QLabel("Avatar-inator",
                             alignment=Qt.AlignmentFlag.AlignHCenter)
        title_label.setFont(QFont("Knewave", 24))

        # Main Avatar
        self.avatar_main_display = QWebEngineView()
        self.avatar_main_display.setFixedSize(240, 280)
        self.avatar_main_display.setContentsMargins(5, 5, 5, 5)
        self.set_default_avatar()

        # Let user choose a text seed
        # Let user choose a text seed
        self.seed_input = QLineEdit("")
        self.seed_input.setFont(QFont("Roboto", 12, 1))
        self.seed_input.setPlaceholderText("Add text to customize")

        self.get_avatar_button = QPushButton("Get Avatar")
        self.get_avatar_button.setFont(QFont("Roboto", 12, 1))

        # Icon button widgets
        self.pixel_slot_layout = IconWidget("pixel_art")
        self.pixel_slot_layout.selected.connect(self.change_main_display)
        self.lorelei_slot_layout = IconWidget("lorelei")
        self.botts_slot_layout = IconWidget("botts")
        self.shapes_slot_layout = IconWidget("shapes")
        self.identicon_slot_layout = IconWidget("identicon")
        self.croodles_slot_layout = IconWidget("croodles")
        self.adventurer_slot_layout = IconWidget("identicon")
        self.rings_slot_layout = IconWidget("rings")

        # Add widgets to the layout
        layout.addWidget(title_label, 0, 0, 1, 4)
        layout.addWidget(self.avatar_main_display, 1, 1, 2, 2)
        layout.addWidget(self.seed_input, 3, 0, 1, 3)
        layout.addWidget(self.get_avatar_button, 3, 3, 1, 1)
        layout.addWidget(self.pixel_slot_layout, 4, 0, 1, 1)
        layout.addWidget(self.lorelei_slot_layout, 4, 1, 1, 1)
        layout.addWidget(self.botts_slot_layout, 4, 2, 1, 1)
        layout.addWidget(self.shapes_slot_layout, 4, 3, 1, 1)
        layout.addWidget(self.identicon_slot_layout, 5, 0, 1, 1)
        layout.addWidget(self.croodles_slot_layout, 5, 1, 1, 1)
        layout.addWidget(self.adventurer_slot_layout, 5, 2, 1, 1)
        layout.addWidget(self.rings_slot_layout, 5, 3, 1, 1)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def change_main_display(self, path: str) -> None:
        print()

    def set_default_avatar(self):
        avatar_svg = ""
        styles_path = "resources/images/main_avatar.svg"
        with open(styles_path, "r") as f:
            avatar_svg = f.read()
        self.avatar_main_display.setHtml(avatar_svg)

    def set_fonts(self):
        # import fonts
        font_dir = "resources/fonts/"
        heading_font_name = "Knewave-Regular.ttf"
        heading_font_path = font_dir + "Knewave/" + heading_font_name

        regular_font_name = "Roboto-Bold.ttf"
        regular_font_path = font_dir + "/Roboto/" + regular_font_name

        # Try and add fonts
        success = QFontDatabase.addApplicationFont(heading_font_path)
        if success == -1:
            print(f"{heading_font_name} not loaded")
        success = QFontDatabase.addApplicationFont(regular_font_path)
        if success == -1:
            print("Regular font not loaded.")


class IconWidget(QWidget):
    selected = pyqtSignal(str)

    def __init__(self, icon_type: str):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setMouseTracking(True)

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
        self.selected.emit(self.filepath)
        return super().mousePressEvent(a0)


app = QApplication(sys.argv)
stylesheet = None
styles_path = "resources/styles.qss"
with open(styles_path, "r") as f:
    stylesheet = f.read()
app.setStyleSheet(stylesheet)
window = MainWindow()
window.show()

app.exec()
