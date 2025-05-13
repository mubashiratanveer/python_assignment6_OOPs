
class Temperature:

    @staticmethod
    def fahrenheit_convert_to_celsius(c):
        return (c * 9/5) +32

tempC = 23
tempF = Temperature.fahrenheit_convert_to_celsius(tempC)
print(f" {tempC}\u00B0F  convert into  {tempF}\u00B0C")

