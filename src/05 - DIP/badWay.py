class LengthConverter:
    def convert(self, from_unit, to_unit, length):
        converted_length = length * 100
        print(converted_length)


class Application:
    def start(self, from_unit, to_unit, length):
        lc = LengthConverter()
        lc.convert(from_unit, to_unit, length)


app = Application()
app.start('Meter', 'Centimeter', 2)