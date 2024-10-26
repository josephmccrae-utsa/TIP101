def convertTemp(celsius):
    kelvin = celsius + 273.15, 2
    fahrenheit = celsius * 1.80 + 32.00, 2
    ans = [kelvin, fahrenheit]
    return ans

x = convertTemp(23.00)
print(x)