from PyQt6.QtWidgets import QWidget, QLCDNumber, QSlider
from PyQt6.QtCore import pyqtSlot, pyqtSignal
from PyQt6 import uic


class Controller(QWidget):
    valueOffice = pyqtSlot(int)
    valueKitchen = pyqtSlot(int)
    valueLiving = pyqtSlot(int)
    valueAussen = pyqtSlot(int)

    changedTempOffice = pyqtSignal(int)
    changedTempKitchen = pyqtSignal(int)
    changedTempLiving = pyqtSignal(int)
    changedTempAussen = pyqtSignal(int)

    def __init__(self, parent=None):
        super(Controller, self).__init__(parent)

        uic.loadUi("controller.ui", self)

        self.lcdNumberOffice = self.findChild(QLCDNumber, "lcdNumbeOffice")
        self.lcdNumberLiving = self.findChild(QLCDNumber, "lcdNumberLiving")
        self.lcdNumberKitchen = self.findChild(QLCDNumber, "lcdNumberKitchen")

        self.verticalSliderOffice = self.findChild(QSlider, "verticalSliderOffice")
        self.verticalSliderLiving = self.findChild(QSlider, "verticalSliderLiving")
        self.verticalSliderKitchen = self.findChild(QSlider, "verticalSliderKitchen")
        self.horizontalSliderAussen = self.findChild(QSlider, "horizontalSliderAussen")

        self.verticalSliderOffice.valueChanged.connect(self.valueOffice)
        self.verticalSliderKitchen.valueChanged.connect(self.valueKitchen)
        self.verticalSliderLiving.valueChanged.connect(self.valueLiving)
        self.horizontalSliderAussen.valueChanged.connect(self.valueAussen)
        self.horizontalSliderAussen.setValue(20)

    def valueOffice(self, soll):
            self.changedTempOffice.emit(soll)

    def valueLiving(self, soll):
        self.changedTempLiving.emit(soll)

    def valueKitchen(self, soll):
        self.changedTempKitchen.emit(soll)

    def valueAussen(self, soll):
        self.changedTempAussen.emit(soll)

    def Frostschutz(self, wert):
        if wert == True:
            self.verticalSliderOffice.setMinimum(5)
            self.verticalSliderKitchen.setMinimum(5)
            self.verticalSliderLiving.setMinimum(5)
        elif wert == False:
            self.verticalSliderOffice.setMinimum(0)
            self.verticalSliderKitchen.setMinimum(0)
            self.verticalSliderLiving.setMinimum(0)
