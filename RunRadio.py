#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from Radio import Radio
import QT_Gui


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = QT_Gui.Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Sélection de la radio Chérie FM
        self.ui.buttonCherieFM.clicked.connect(self.action_buttonCherieFM)

        # Sélection de la radio NRJ
        self.ui.buttonNRJ.clicked.connect(self.action_buttonNRJ)
        
        # Sélection de la radio FG
        self.ui.buttonFG.clicked.connect(self.action_buttonFG)
        
        # Sélection de la radio RFM
        self.ui.buttonRFM.clicked.connect(self.action_buttonRFM)
        
        # Sélection de la radio Voltage
        self.ui.buttonVoltage.clicked.connect(self.action_buttonVoltage)
        
        
        # Instanciation de la radio
        self.r = Radio()
        
    
    def action_buttonCherieFM(self):
        
        self.ui.statusBar.showMessage(" Radio sélectionnée : Chérie FM")
        self.r.setRadioCherieFM()
           
    def action_buttonNRJ(self):
        
        self.ui.statusBar.showMessage(" Radio sélectionnée : N.R.J.")
        self.r.setRadioNRJ()
    
    def action_buttonFG(self):
        
        self.ui.statusBar.showMessage(" Radio sélectionnée : Radio FG")
        self.r.setRadioFg()
    
    def action_buttonRFM(self):
        
        self.ui.statusBar.showMessage(" Radio sélectionnée : R.F.M")
        self.r.setRadioRFM()
        
    def action_buttonVoltage(self):
        
        self.ui.statusBar.showMessage(" Radio sélectionnée : Voltage FM")
        self.r.setRadioVoltage()


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())