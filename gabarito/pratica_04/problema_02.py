def celsius_para_fahrenheit(celsius: float) -> float:
    tf = (celsius * 9 / 5) + 32
    return tf


def fahrenheit_para_kelvin(fahrenheit: float) -> float:
    tk = (fahrenheit - 32) * 5 / 9 + 273.15
    return tk


# Main

temperatura_celsius = float(input("Digite a temperatura em Celsius: "))

temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)

temperatura_kelvin = fahrenheit_para_kelvin(temperatura_fahrenheit)

print(f"Temperatura em Fahrenheit: {temperatura_fahrenheit:.1f}°F")
print(f"Temperatura em Kelvin: {temperatura_kelvin:.1f}K")