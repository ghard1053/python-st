
# --------
import math

class CalcFee:
    def __init__(self):
        self.shipping_fee = 1000
        self.tax_rate = 0.08
        self.value = 0
    
    def addItem(self, price):
        self.value += price
    
    def calc(self):
        total = self.value + self.shipping_fee
        tax = math.ceil(total * self.tax_rate)
        v = math.ceil(total + tax)
        return v

class BMI:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        self.calcBMI()