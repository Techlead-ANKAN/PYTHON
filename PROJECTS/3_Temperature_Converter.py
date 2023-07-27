# Temperature Converter

type = input("Enter temp unit: ")
deg = float(input("Enter degree: ")) 
print(f"Entered Temperature: {deg}°{type.capitalize()}")



if type.lower() == "c":
    print(f"In Fahrenheit: {(deg * (9/5)) + 32}°F")
    print(f"In Kelvin: {deg + 273.15}K")

elif type.lower() == "f":
    print(f"In Celcius: {(deg - 32) * (5/9)}°C")
    print(f"In Kelvin: {((deg - 32) * (5/9)) + 273.15}K")

elif type.lower() == "k":
    print(f"In Celcius: {deg-273.15}°C")
    print(f"In Fahrenheit: {((deg-273.15) * (9/5)) + 32}°F")


