# This Python file uses the following encoding: utf-8
from PySide6 import QtWidgets
from UI import Ui_MainWindow
from model import CalculatorModel

class CalculatorView(QtWidgets.QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.sum = 0

        self.model = model
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.buttons = [self.ui.pushButton_0,
                   self.ui.pushButton_1,
                   self.ui.pushButton_2,
                   self.ui.pushButton_3, 
                   self.ui.pushButton_4, 
                   self.ui.pushButton_5,
                   self.ui.pushButton_6,
                   self.ui.pushButton_7,
                   self.ui.pushButton_8,
                   self.ui.pushButton_9]
        
        self.opbuttons = [self.ui.pushButton_add,
                   self.ui.pushButton_sub,
                   self.ui.pushButton_mul,
                   self.ui.pushButton_div,
                   self.ui.pushButton_eq,
                   self.ui.pushButton_ac]
        
        for button in self.buttons:
            button.clicked.connect(lambda *args, btn=button: self.ClickedButton(int(btn.text())))
        
        for opbutton in self.opbuttons:
            opbutton.clicked.connect(lambda *args, btn=opbutton: self.ClickedButton(btn.text()))

    def ClickedButton(self, value):
        self.model.operate(value)
        self.ui.label.setText(str(self.model.getValue()))