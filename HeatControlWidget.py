from PyQt6.QtWidgets import QWidget, QHBoxLayout
from PyQt6.QtCore import QTimer, pyqtSlot, pyqtSignal
from Controller import Controller
from Heater import Heater
from Gastherme import Gastherme
from Notaus import Notaus
from Diagramm import Diagramm

class HeatControlWidget(QWidget):
    slotReferenceValueKitchen = pyqtSlot(int)
    slotRealValueKitchen = pyqtSlot()
    signalRealValueKitchenChanged = pyqtSignal(int)

    slotReferenceValueLiving = pyqtSlot(int)
    slotRealValueLiving = pyqtSlot()
    signalRealValueLivingChanged = pyqtSignal(int)

    slotReferenceValueOffice = pyqtSlot(int)
    slotRealValueOffice = pyqtSlot()
    signalRealValueOfficeChanged = pyqtSignal(int)

    slotRealValueAussen = pyqtSlot(int)
    signalRealValueAussenChanged = pyqtSignal(int)

    signalFrostSchutzIsActive = pyqtSignal(bool)

    signalRuecklauf = pyqtSignal(int)

    slotNotaus = pyqtSlot()

    def __init__(self, parent=None):
        super(HeatControlWidget, self).__init__(parent)
        ###Klassen importieren###
        self.heater = Heater(self)
        self.controller = Controller(self)
        self.gastherme = Gastherme(self)
        self.notaus = Notaus(self)
        self.diagramm=Diagramm(self)

        ###Notaus###
        self.notaus.signalNotaus.connect(self.slotNotaus)

        ###Timer Kitchen###
        self.timerKitchen = QTimer(self)
        self.timerKitchen.timeout.connect(self.slotRealValueKitchen)
        self.referenceValueKitchen = 0
        self.realValueKitchen = 0
        ###Timer Living###
        self.timerLiving = QTimer(self)
        self.timerLiving.timeout.connect(self.slotRealValueLiving)
        self.referenceValueLiving = 0
        self.realValueLiving = 0
        ###Timer Office###
        self.timerOffice = QTimer(self)
        self.timerOffice.timeout.connect(self.slotRealValueOffice)
        self.referenceValueOffice = 0
        self.realValueOffice = 0
        ###Signals&Slots Kitchen###
        self.controller.changedTempKitchen.connect(self.slotReferenceValueKitchen)
        self.signalRealValueKitchenChanged.connect(self.heater.textKitchen)
        self.signalRealValueKitchenChanged.connect(self.vergleichen)
        ###Signals&Slots Office###
        self.controller.changedTempOffice.connect(self.slotReferenceValueOffice)
        self.signalRealValueOfficeChanged.connect(self.heater.textOffice)
        self.signalRealValueOfficeChanged.connect(self.vergleichen)
        ###Signals&Slots Living###
        self.controller.changedTempLiving.connect(self.slotReferenceValueLiving)
        self.signalRealValueLivingChanged.connect(self.heater.textLiving)
        self.signalRealValueLivingChanged.connect(self.vergleichen)
        ###Signals&Slots Außentemperatur###
        self.controller.changedTempAussen.connect(self.slotRealValueAussen)
        self.signalRealValueAussenChanged.connect(self.heater.textAussen)
        ###Signals&Slots Frostschutz###
        self.signalFrostSchutzIsActive.connect(self.controller.Frostschutz)
        ###Signals&Slots Rücklauf###
        self.signalRuecklauf.connect(self.gastherme.changeRuecklauf)

        ###Layout###
        myLayout = QHBoxLayout(self)
        myLayout.addWidget(self.controller)
        myLayout.addWidget(self.heater)
        myLayout.addWidget(self.gastherme)
        myLayout.addWidget(self.notaus)
        myLayout.addWidget(self.diagramm)
        self.setLayout(myLayout)



    #Notaus Funktion
    def slotNotaus(self,wert):
        self.controller.verticalSliderLiving.setEnabled(wert)
        self.controller.verticalSliderOffice.setEnabled(wert)
        self.controller.verticalSliderKitchen.setEnabled(wert)
        self.controller.horizontalSliderAussen.setEnabled(wert)
        self.gastherme.QDialVorlauf.setEnabled(wert)
        self.gastherme.QDialRuecklauf.setEnabled(wert)
        self.gastherme.QDialWarmwasser.setEnabled(wert)
        self.gastherme.QDialFrostschutz.setEnabled(wert)


    #Außentemperatur wird übergeben und Frostschutz auf True oder False gesetzt
    def slotRealValueAussen(self, temp):
        self.realValueAussen = temp
        # Außentemperatur wird an realValueAussen übergeben
        self.signalRealValueAussenChanged.emit(self.realValueAussen)
        if self.realValueAussen < 5:
            self.signalFrostSchutzIsActive.emit(True)
        else:
            self.signalFrostSchutzIsActive.emit(False)

    #Starten des Timers falls nicht aktiv
    def slotReferenceValueKitchen(self, referenceValue: int):
        self.referenceValueKitchen = referenceValue

        if self.timerKitchen.isActive() == False:
            self.timerKitchen.start(1 * 1000)
    #Abgleich ob Soll >/</= isttemperatur
    def slotRealValueKitchen(self):
        if self.referenceValueKitchen > self.realValueKitchen:
            self.realValueKitchen += 1
        elif self.referenceValueKitchen < self.realValueKitchen:
            self.realValueKitchen -= 1
        else:
            self.timerKitchen.stop()

        self.signalRealValueKitchenChanged.emit(self.realValueKitchen)

    def slotReferenceValueLiving(self, referenceValue: int):
        self.referenceValueLiving = referenceValue

        if self.timerLiving.isActive() == False:
            self.timerLiving.start(1 * 1000)

    def slotRealValueLiving(self):
        if self.referenceValueLiving > self.realValueLiving:
            self.realValueLiving += 1
        elif self.referenceValueLiving < self.realValueLiving:
            self.realValueLiving -= 1
        else:
            self.timerLiving.stop()

        self.signalRealValueLivingChanged.emit(self.realValueLiving)

    def slotReferenceValueOffice(self, referenceValue: int):
        self.referenceValueOffice = referenceValue

        if self.timerOffice.isActive() == False:
            self.timerOffice.start(1 * 1000)

    def slotRealValueOffice(self):
        if self.referenceValueOffice > self.realValueOffice:
            self.realValueOffice += 1
        elif self.referenceValueOffice < self.realValueOffice:
            self.realValueOffice -= 1
        else:
            self.timerOffice.stop()

        self.signalRealValueOfficeChanged.emit(self.realValueOffice)

    #Vergleich welche Solltemp am größten ist
    def vergleichen(self):
        if self.referenceValueOffice > self.referenceValueLiving and self.referenceValueOffice > self.referenceValueKitchen:
            self.max = self.referenceValueOffice
            self.signalRuecklauf.emit(self.max+1)

        elif self.referenceValueLiving > self.referenceValueKitchen and self.referenceValueLiving > self.referenceValueOffice:
            self.max = self.referenceValueLiving
            self.signalRuecklauf.emit(self.max+1)

        else:
            self.max = self.referenceValueKitchen
            self.signalRuecklauf.emit(self.max+1)



