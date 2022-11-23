from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget, QGridLayout
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os

class Diagramm(PlotWidget):

    def __init__(self, *args, **kwargs):
        super(Diagramm, self).__init__(*args, **kwargs)


        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        # plot data: x, y values
        self.plot(hour, temperature)




