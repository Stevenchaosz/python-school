midday = []
midnight = []

for i in range(0, 4):

    while True:
        temperature_midday = raw_input("Enter the temperature for midday:\n")
        try:
            float(temperature_midday)
        except ValueError:
            print "This is not a number.\n"
            continue
        temperature_midday_float = float(temperature_midday)
        if temperature_midday_float < -50 or temperature_midday_float > 60:
            print "Sorry, your temperature is either too high or too low.\n"
        else:
            midday.append(temperature_midday)
            print "Your temperature is recorded.\n"
            break

    while True:
        temperature_midnight = raw_input("Enter the temperature for midnight:\n")
        try:
            float(temperature_midnight)
        except ValueError:
            print "This is not a number.\n"
            continue
        temperature_midnight_float = float(temperature_midnight)
        if temperature_midnight_float < -50 or temperature_midnight_float > 60:
            print "Sorry, your temperature is either too high or too low.\n"
        else:
            midnight.append(temperature_midnight)
            print "Your temperature is recorded.\n"
            break

max_midday_temperature = 0
min_midnight_temperature = 100
max_dayIndex = 0
min_nightIndex = 0

for day in range(0, len(midday)):
    midday_temperature = float(midday[day])
    if midday_temperature > max_midday_temperature:
        max_midday_temperature = midday_temperature
        max_dayIndex = day + 1
for night in range(0, len(midnight)):
    midnight_temperature = midnight[night]
    if midnight_temperature < min_midnight_temperature:
        min_midnight_temperature = midnight_temperature
        min_nightIndex = night + 1
print_text = ("The day with the highest midday temperature is Day", max_dayIndex,
              ". The temperature is", max_midday_temperature, "\nThe day with the lowest midnight temperature is Day",
              min_nightIndex, ". The temperature is ", min_midnight_temperature, ".")

print "The day with the highest midday temperature is Day", max_dayIndex, "."
print "The temperature is", max_midday_temperature, "."
print "\nThe day with the lowest midnight temperature is Day", min_nightIndex, "."
print "The temperature is", min_midnight_temperature, "."
