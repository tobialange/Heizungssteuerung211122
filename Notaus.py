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
        self.notaustimer2.timeout.connect(self.notausan)

    def slotNotaus(self,wert):

        if self.first == False:
            self.notaustimer.start(5 * 1000)
            self.first = True
        else:
            self.first = True
        self.signalNotaus.emit(wert)

        if self.notausbutton.isDown():
            print(self.notaustimer.remainingTime())
            self.notaustimer.timeout.connect(self.SlotNotan)

        if self.notausbutton.isDown() == False:
            self.notaustimer.stop()
            self.first = False

    def SlotNotan(self):
        print("Notan")
        self.notaustimer.stop()
        self.signalNotaus.emit(True)
        self.notausbutton.setDisabled(True)
        if self.second == False:
            self.notaustimer2.start(1000)
            self.second = True

    def notausan(self):
        print("Notausfunk")
        self.notausbutton.setEnabled(True)
        self.notaustimer2.stop()
        self.second = False





