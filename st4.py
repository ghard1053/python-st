
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
    

# --------
class Car:
    # ****

class Van(Car):
    def __init__(self, owner):
        super().__init__(owner)
        # ****

import car

car1 = car.Van("john")


# --------
class Game:
    def __goal(self):
        print("")
    
    def play(self):
        print("")

game = Game()
game.play()
game.__goal() # error

# --------
class Empty: pass

o = Empty()


# --------
class Hoge:
    @staticmethod
    def introduce():
        print("Hoge")

Hoge.introduce()


# --------

import json
import urllib.request

class Kawase:
    API = ""

    def __get_api(self):
        res = urllib.request.urlopen(Kawase.API)
        return res.read().decode('utf8')

    def __analize_result(self, json_str):
        return json.loads(json_str)

    def get_result(self):
        json_str = self.__get_api()
        return self.__analize_result(json_str)

    @staticmethod
    def get_usd_jpy():
        kawase = Kawase()
        data = kawase.get_result()
        usd = data.get("JPY", -1)
        return usd

print("USD:JPY = 1:", Kawase.get_usd_jpy())
