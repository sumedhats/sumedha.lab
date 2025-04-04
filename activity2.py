# Temperature Converter Program

def temperature_converter():
    print("Welcome to the Temperature Converter!")
    print("Available conversions:")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")

    # Get user input for the conversion type
    try:
        choice = int(input("Please choose a conversion (1-6): "))

        if choice not in [1, 2, 3, 4, 5, 6]:
            print("Invalid input! Please choose a number between 1 and 6.")
            return

        # Get temperature value from the user based on the chosen conversion
        temperature = float(input("Enter the temperature value: "))

        if choice == 1:  # Celsius to Fahrenheit
            result = (temperature * 9/5) + 32
            print(f"{temperature} Celsius is {result} Fahrenheit.")
        
        elif choice == 2:  # Celsius to Kelvin
            result = temperature + 273.15
            print(f"{temperature} Celsius is {result} Kelvin.")
        
        elif choice == 3:  # Fahrenheit to Celsius
            result = (temperature - 32) * 5/9
            print(f"{temperature} Fahrenheit is {result} Celsius.")
        
        elif choice == 4:  # Fahrenheit to Kelvin
            result = (temperature - 32) * 5/9 + 273.15
            print(f"{temperature} Fahrenheit is {result} Kelvin.")
        
        elif choice == 5:  # Kelvin to Celsius
            result = temperature - 273.15
            print(f"{temperature} Kelvin is {result} Celsius.")
        
        elif choice == 6:  # Kelvin to Fahrenheit
            result = (temperature - 273.15) * 9/5 + 32
            print(f"{temperature} Kelvin is {result} Fahrenheit.")
    
    except ValueError:
        print("Error: Please enter a valid number for the temperature value.")

# Call the temperature converter function
temperature_converter()

