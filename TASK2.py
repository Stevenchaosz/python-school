midday = []
midnight = []

for i in range(0, 30):

    while True:
        temperature_midday = raw_input("Enter the temperature for midday.\n")
        try:
            float(temperature_midday)
        except ValueError:
            print "This is not a number.\n"
            continue
        temperature_midday_float = float(temperature_midday)
        if temperature_midday_float < -50 or temperature_midday_float > 60:
            print("Sorry, your temperature is either too high or too low.")
        else:
            midday.append(temperature_midday)
            print("Your temperature is recorded.\n")
            break

    while True:
        temperature_midnight = raw_input("Enter the temperature for midnight.\n")
        try:
            float(temperature_midnight)
        except ValueError:
            print "This is not a number.\n"
            continue
        temperature_midnight_float = float(temperature_midnight)
        if temperature_midnight_float < -50 or temperature_midnight_float > 60:
            print("Sorry, your temperature is either too high or too low.")
        else:
            midnight.append(temperature_midnight)
            print("Your temperature is recorded.\n")
            break

total_midday = 0
total_midnight = 0

for day in range(0, len(midday)):
    total_midday = total_midday + float(midday[day])
average_midday = total_midday / len(midday)

for night in range(0, len(midnight)):
    total_midnight = total_midnight + float(midnight[night])
average_midnight = total_midnight / len(midnight)

print "The average midday temperature for a month is ", average_midday, "."
print "The average midnight temperature is", average_midnight, "."
