from model import CalculatorModel
from view import CalculatorView

class CalculatorController():
    def __init__(self):
        self.model = CalculatorModel()
        self.view = CalculatorView(self.model)     