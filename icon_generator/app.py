import sys
from PyQt6.QtGui import QPalette, QColor
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
        super(MainWindow, self).__init__()

        self.setWindowTitle("Avatar-inator")

        layout = QGridLayout()

        # Build our widgets
        self.title_label = QLabel("Avatar-inator")
        
        self.avatar_main_svg = QSvgWidget("media/avatar_main.svg")

        self.seed_input = QLineEdit("")

        self.get_avatar_button = QPushButton("Get Avatar")

        layout.addWidget(self.title_label, 0, 0, 1, 4)
        layout.addWidget(self.avatar_main_svg, 1, 1, 1, 2)
        layout.addWidget(self.seed_input, 2, 0, 1, 3)
        layout.addWidget(self.get_avatar_button, 2, 2, 1, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
