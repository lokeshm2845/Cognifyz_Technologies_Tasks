def temperature_converter():
    print("---- Temperature Converter ----")
    try:
        temp = float(input("Enter the temperature value: "))
        choice = input("Convert to (C)elsius or (F)ahrenheit? Enter C or F: ").strip().upper()

        if choice == 'F':
            result = (temp * 9/5) + 32
            print(f"{temp}°C is equal to {result:.2f}°F")
        elif choice == 'C':
            result = (temp - 32) * 5/9
            print(f"{temp}°F is equal to {result:.2f}°C")
        else:
            print("Invalid choice. Please enter C or F.")
    except ValueError:
        print("Invalid temperature input. Please enter a number.")

if __name__ == "__main__":
    temperature_converter()