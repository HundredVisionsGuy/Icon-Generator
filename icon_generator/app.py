import controller
import file_clerk.clerk as clerk
import sys
from PyQt6.QtCore import QEvent, Qt, pyqtSignal
from PyQt6.QtGui import (QEnterEvent, QMouseEvent, QPalette, QColor,
                         QFontDatabase, QFont)
from PyQt6.QtSvgWidgets import QSvgWidget
from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
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
        self.setContentsMargins(12, 12, 12, 12)  # NEW - adds margin
        self.set_fonts()

        # Title
        title_label = QLabel("Avatar-inator",
                             alignment=Qt.AlignmentFlag.AlignHCenter)
        title_label.setFont(QFont("Knewave", 24))

        # Main Avatar
        self.avatar_type = "bottts"
        self.avatar_main_display = QWebEngineView()
        self.avatar_main_display.setFixedSize(240, 240)
        self.avatar_main_display.setContentsMargins(5, 5, 5, 5)
        self.set_default_avatar()

        # Let user choose a text seed
        self.seed_input = QLineEdit("")
        self.seed_input.setFont(QFont("Montserrat", 12, 1))
        self.seed_input.setPlaceholderText("Add text to customize")

        self.get_avatar_button = QPushButton("Get Avatar")
        self.get_avatar_button.setFont(QFont("Montserrat"))
        self.get_avatar_button.clicked.connect(self.get_avatar)

        self.clear_button = QPushButton("Clear text")
        self.clear_button.setFont(QFont("Montserrat"))
        self.clear_button.clicked.connect(self.clear_input)

        self.save_button = QPushButton("Save avatar")
        self.save_button.setFont(QFont("Montserrat"))
        self.save_button.clicked.connect(self.save_avatar)

        # Icon button widgets
        pixel_slot_layout = IconWidget("pixel-art")
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
        layout.addWidget(self.clear_button, 3, 3, 1, 1)
        layout.addWidget(self.get_avatar_button, 4, 0, 1, 2)
        layout.addWidget(self.save_button, 4, 2, 1, 2)
        layout.addWidget(pixel_slot_layout, 5, 0)
        layout.addWidget(adventurer_slot_layout, 5, 1)
        layout.addWidget(botts_slot_layout, 5, 2)
        layout.addWidget(croodles_slot_layout, 5, 3)
        layout.addWidget(identicon_slot_layout,6, 0)
        layout.addWidget(lorelei_slot_layout, 6, 1)
        layout.addWidget(rings_slot_layout, 6, 2)
        layout.addWidget(shapes_slot_layout, 6, 3)

        items = (layout.itemAt(i) for i in range(layout.count()))
        for w in items:
            data = w.widget()
            if isinstance(data, IconWidget):
                data.selected.connect(self.change_main_svg)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def set_default_avatar(self):
        self.avatar_main_svg = "resources/images/bottts_avatar.svg"
        avatar_svg = clerk.file_to_string(self.avatar_main_svg)
        self.avatar_main_display.setHtml(avatar_svg)

    def change_main_svg(self, path):
        self.avatar_type = controller.get_avatar_type(path)
        self.get_avatar()

    def clear_input(self):
        self.seed_input.setText("")
        self.set_default_avatar()

    def get_avatar(self):
        # get text from input
        seed = self.seed_input.text()
        if not seed:
            seed = "HundredVisionsGuy"

        # get avatar_type
        avatar_type = self.avatar_type

        # make dicebear call
        self.avatar_main_svg = controller.get_avatar(avatar_type, seed)

        # Change main avatar (if no error)
        if "Error" not in self.avatar_main_svg:
            self.avatar_main_display.setHtml(self.avatar_main_svg)

    def save_avatar(self):
        name = QFileDialog.getSaveFileName(self, 'Save File', 'myAvatar',
                                           'SVG File (*.svg)')
        file = open(name[0], 'w', encoding='utf-8')
        code = self.avatar_main_svg
        file.write(code)
        file.close()

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


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


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
        label_text.setPos(10, 64)

        avatar_widget = self.scene.addWidget(avatar_svg)
        avatar_widget.setPos(14, 6)
        view = QGraphicsView(self.scene)
        vbox = QVBoxLayout()
        vbox.addWidget(view)
        self.setLayout(vbox)
        self.setStyleSheet("border: 0 solid;")
        self.setFixedSize(110, 120)

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        self.selected.emit(self.filepath)
        return super().mousePressEvent(a0)

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
