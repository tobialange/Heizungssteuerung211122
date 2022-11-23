from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QAbstractButton
from PyQt6.QtCore import QTimer, pyqtSlot, pyqtSignal
from PyQt6 import uic



class Notaus(QWidget):

    slotNotaus = pyqtSlot(bool)
    signalNotaus = pyqtSignal(bool)
    SlotNotan = pyqtSlot()

    def __init__(self, parent=None):
        super(Notaus, self).__init__(parent)

        uic.loadUi("Notaus.ui", self)

        self.notausbutton = self.findChild(QPushButton, "Notaus")
        self.notausbutton.setAutoRepeat(True)
        self.notausbutton.clicked.connect(self.slotNotaus)
        self.notaustimer = QTimer(self)
        self.notaustimer2 = QTimer(self)
        self.first = False
        self.second = False
        self.notaustimer.timeout.connect(self.counterzähler)
        self.counter = 0

    def slotNotaus(self,wert):


        if self.notausbutton.isDown():
            if self.notaustimer.isActive() == False:
                self.notaustimer.start(1000)

        else:
            self.notaustimer.stop()
            self.counter = 0

    def counterzähler(self):
        self.counter += 1
        if self.counter == 5:
            print("Ziel")

