midday = []
midnight = []

for i in range(0, 30):

    while True:
        temperature_midday = input("Enter the temperature for midday.\n")
        temperature_midday_float = float(temperature_midday)
        if temperature_midday_float < -50 or temperature_midday_float > 60:
            print("Sorry, your temperature is either too high or too low.")
        else:
            midday.append(temperature_midday)
            print("Your temperature is recorded.")
            break

    while True:
        temperature_midnight = input("Enter the temperature for midnight.\n")
        temperature_midnight_float = float(temperature_midnight)
        if temperature_midnight_float < -50 or temperature_midnight_float > 60:
            print("Sorry, your temperature is either too high or too low.")
        else:
            midnight.append(temperature_midnight)
            print("Your temperature is recorded.")
            break

print(midday, midnight)
