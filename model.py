
class CalculatorModel():
    def __init__(self):
        self.sum = ""

    def operate(self, number):
            if number == '=':
                self.sum = eval(self.sum)
            elif number == 'AC':
                self.sum = 0
            else:
                if number == 0 and self.sum == 0:
                    self.sum = number
                else:
                    if self.sum == 0:
                        self.sum = f'{number}'
                    else:
                        self.sum = f'{self.sum}{number}'
    
    def getValue(self):
        return self.sum


