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
            print "Sorry, your temperature is either too high or too low."
        else:
            midday.append(temperature_midday)
            print "Your temperature is recorded.\n"
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
            print "Sorry, your temperature is either too high or too low."
        else:
            midnight.append(temperature_midnight)
            print "Your temperature is recorded.\n"
            break

print midday, midnight
