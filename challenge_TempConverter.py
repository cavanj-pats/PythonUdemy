#  Challenge Temperature Converter




"""
Celsius
F = (c * 9/5)+32
K = C + 273.15
"""
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5)+32
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32)*5/9
    
    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15
    
    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15
    
    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        c = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
        return TemperatureConverter.celsius_to_kelvin(c)
    


if __name__ == "__main__":
    tc = TemperatureConverter

    print(tc.fahrenheit_to_celsius(-6))
    print(tc.celsius_to_fahrenheit(-45))
    print(tc.fahrenheit_to_kelvin(350))
