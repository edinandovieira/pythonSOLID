from abc import ABC, abstractmethod

"""
Dependency Inversion Principle(DIP)

If possible, child class should not be dependable on parent class or concrete class, instead use abstraction/interface
"""

class LengthConverter:
    @abstractmethod
    def convert(self, from_unit, to_unit, length):
        pass


class LengthConverterusingXYZ(LengthConverter):
    def convert(self, from_unit, to_unit, length):
        print('converting length using XYZ api')


class Application:
    def __init__(self, length_converter: LengthConverter):
        self.length_converter = length_converter

    def start(self, from_unit, to_unit, length):
        self.length_converter.convert(from_unit, to_unit, length)


lcx = LengthConverterusingXYZ()
app = Application(lcx)
app.start('Meter', 'Centimeter', 2)