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

total_midday = 0
total_midnight = 0

for i in range(0, len(midday)):
    total_midday = total_midday + float(midday[i])
average_midday = total_midday / len(midday)

for i in range(0, len(midnight)):
    total_midnight = total_midnight + float(midnight[i])
average_midnight = total_midnight / len(midnight)

print("The average midday temperature for a month is ", average_midday, "\nThe average midnight temperature is", average_midnight)