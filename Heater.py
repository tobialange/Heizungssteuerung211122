from PyQt6.QtWidgets import QWidget, QTextBrowser
from PyQt6.QtCore import pyqtSlot
from PyQt6 import uic


class Heater(QWidget):
    textOffice = pyqtSlot(int)
    textLiving = pyqtSlot(int)
    textKitchen = pyqtSlot(int)
    textAussen = pyqtSlot(int)

    def __init__(self, parent=None):
        super(Heater, self).__init__(parent)

        uic.loadUi("heater.ui", self)

        self.textBrowserOffice = self.findChild(QTextBrowser, "textBrowserOffice")
        self.textBrowserLiving = self.findChild(QTextBrowser, "textBrowserLiving")
        self.textBrowserKitchen = self.findChild(QTextBrowser, "textBrowserKitchen")
        self.textBrowserAussen = self.findChild(QTextBrowser, "textBrowserAussen")

    def textOffice(self, ist):
        text = str(ist) + " °C"
        self.textBrowserOffice.setText(text)

    def textLiving(self, ist):
        text = str(ist) + " °C"
        self.textBrowserLiving.setText(text)

    def textKitchen(self, ist):
        text = str(ist) + " °C"
        self.textBrowserKitchen.setText(text)

    def textAussen(self, ist):
        text = str(ist) + " °C"
        self.textBrowserAussen.setText(text)
