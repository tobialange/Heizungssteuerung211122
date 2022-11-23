from PyQt6.QtWidgets import QMainWindow
from HeatControlWidget import HeatControlWidget

class MyMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Heizungssteuerung")

        self.setCentralWidget(HeatControlWidget(self))

        self.setMinimumSize(1280, 720)