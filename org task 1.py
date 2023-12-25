def convert_temperature():
    print("Temperature Converter")

    # Get user input
    temperature = float(input("Enter the temperature value: "))
    original_unit = input("Enter the original unit (Celsius, Fahrenheit, or Kelvin): ").lower()

    # Perform conversions
    if original_unit == "celsius":
        fahrenheit = (temperature * 9/5) + 32
        kelvin = temperature + 273.15
    elif original_unit == "fahrenheit":
        celsius = (temperature - 32) * 5/9
        kelvin = (temperature - 32) * 5/9 + 273.15
    elif original_unit == "kelvin":
        celsius = temperature - 273.15
        fahrenheit = (temperature - 273.15) * 9/5 + 32
    else:
        print("Invalid unit. Please enter Celsius, Fahrenheit, or Kelvin.")
        return

    # Display results
    print(f"\n{temperature} {original_unit} is equivalent to:")
    print(f"{celsius:.2f} Celsius")
    print(f"{fahrenheit:.2f} Fahrenheit")
    print(f"{kelvin:.2f} Kelvin")

if __name__ == "__main__":
    convert_temperature()
