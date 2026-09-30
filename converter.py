def show_menu():
    print("\n=== Unit Converter ===")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Quit")


LENGTH_CONVERSIONS = {
    "1": ("Kilometers → Miles",      lambda x: x * 0.621371),
    "2": ("Miles → Kilometers",      lambda x: x / 0.621371),
    "3": ("Meters → Feet",           lambda x: x * 3.28084),
    "4": ("Feet → Meters",           lambda x: x / 3.28084),
}


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a number. Try again.")


def run_conversions(table, title):
    print(f"\n--- {title} ---")

    while True:
        for key, (label, _) in table.items():
            print(f"{key}. {label}")
        print(f"{len(table) + 1}. Back to main menu")

        choice = input("\nChoose a conversion: ")

        if choice == str(len(table) + 1):
            return

        if choice not in table:
            print("Invalid choice.")
            continue

        label, func = table[choice]
        number = get_number(f"Enter value in {label.split(' → ')[0]}: ")
        result = func(number)
        print(f"\n{number} {label.split(' → ')[0]} = {result:.4f} {label.split(' → ')[1]}")


def mode_length():
    run_conversions(LENGTH_CONVERSIONS, "Length")


WEIGHT_CONVERSIONS = {
    "1": ("Kilograms → Pounds", lambda x: x * 2.20462),
    "2": ("Pounds → Kilograms", lambda x: x / 2.20462),
    "3": ("Grams → Ounces",     lambda x: x * 0.035274),
    "4": ("Ounces → Grams",     lambda x: x / 0.035274),
}

def mode_weight():
    run_conversions(WEIGHT_CONVERSIONS, "Weight")


TEMPERATURE_CONVERSIONS = {
    "1": ("Celsius → Fahrenheit",    lambda x: (x * 9/5) + 32),
    "2": ("Fahrenheit → Celsius",    lambda x: (x - 32) * 5/9),
    "3": ("Celsius → Kelvin",        lambda x: x + 273.15),
    "4": ("Kelvin → Celsius",        lambda x: x - 273.15),
}


def mode_temperature():
    run_conversions(TEMPERATURE_CONVERSIONS, "Temperature")


def main():
    while True:
        show_menu()
        choice = input("Choose a category: ")

        if choice == "1":
            mode_length()
        elif choice == "2":
            mode_weight()
        elif choice == "3":
            mode_temperature()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()