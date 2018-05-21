midday = []
midnight = []

for i in range(0, 4):

    while True:
        temperature_midday = input("Enter the temperature for midday.\n")
        temperature_midday_float = float(temperature_midday)
        if temperature_midday_float < -50 or temperature_midday_float > 60:
            print "Sorry, your temperature is either too high or too low."
        else:
            midday.append(temperature_midday)
            print "Your temperature is recorded."
            break

    while True:
        temperature_midnight = input("Enter the temperature for midnight.\n")
        temperature_midnight_float = float(temperature_midnight)
        if temperature_midnight_float < -50 or temperature_midnight_float > 60:
            print "Sorry, your temperature is either too high or too low."
        else:
            midnight.append(temperature_midnight)
            print "Your temperature is recorded."
            break

max_midday_temperature = 0
min_midnight_temperature = 100
max_dayIndex = 0
min_nightIndex = 0
for i in range(0, len(midday)):
    midday_temperature = float(midday[i])
    if midday_temperature > max_midday_temperature:
        max_midday_temperature = midday_temperature
        max_dayIndex = i
for i in range(0, len(midnight)):
    midnight_temperature = midnight[i]
    if midnight_temperature < min_midnight_temperature:
        min_midnight_temperature = midnight_temperature
        min_nightIndex = i
print "The day with the highest midday temperature is Day", max_dayIndex, ". The temperature is", max_midday_temperature, "\nThe day with the lowest midnight temperature is Day", max_dayIndex, ". The temperature is ", min_midnight_temperature, "."
