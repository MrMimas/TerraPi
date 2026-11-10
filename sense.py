## sense_hat pacman frog terrrium monitor
##!! designed for pacman frogs
## The script is still in development. Updated 2026-05-25

## if you have a different type of frog, !!
## you may need to adjust the temperature and humidity thresholds !!
## in the code to better suit your specific frog's needs. Always research the ideal conditions !!
## for your particular species of frog to ensure their health and well-being. !!

## Raspberry Pi and Sense_Hat needed.
## run it a couple minutes to get a good reading of the temperature and humidity.

from turtle import clear

from sense_hat import SenseHat
import time

sense = SenseHat()


mode = 0

while True:

    if event.direction == "up":
            clear()  # Clear the LED matrix
    elif event.direction == "down":
            clear(100, 100, 100)  # Clear the LED matrix
    
    
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()

    temp = temp - 25  # Adjust temperature reading for better accuracy
    if temp > 27:
        humidity = humidity - 10  # Adjust humidity reading for better accuracy
    elif temp < 25:
        humidity = humidity + 25  # Adjust humidity reading for better accuracy
    else :
        humidity = humidity + 15  # Adjust humidity reading for better accuracy
    
    if pressure > 1010:
        humidity = humidity - 5  # Adjust humidity reading for better accuracy
    else:
        humidity = humidity + 5  # Adjust humidity reading for better accuracy

    if temp > 29:
        temp = 29  # Cap temperature at 29°C for better accuracy
    elif temp < 18:
        temp = 18  # Cap temperature at 18°C for better accuracy
    
    if humidity > 75:
        temp = temp - 5  # Adjust temperature reading for better accuracy
    elif humidity < 73:
        temp = temp + 5  # Adjust temperature reading for better accuracy

    temp = round(temp, 1)
    humidity = round(humidity, 1)
    pressure = round(pressure, 1)

    print("Temperature: {}°C".format(temp))
    print("Humidity: {}%".format(humidity))
    print("Pressure: {} hPa".format(pressure))

    # Check for joystick events
    # 0 = standby mode, 1 = frog mode, 2 = night mode 3 = normal mode
    for event in sense.stick.get_events():
        if event.action == "pressed":
            button_event = event.direction
            if button_event == "middle":
                mode += 1  # Increment mode by 1
                if mode > 3:   # Reset mode to 0 if it exceeds 3
                    mode = 0
        

    if mode == 0:
        sense.clear()  # Clear the LED matrix
        time.sleep(1)  # Time to wait before the next reading
        sense.show_message("Standby Mode", text_colour=[255, 0, 255])  # purple text for standby
    
    elif mode == 1: # daytime mode = frogs want slightly warmer with the same humidity as night mode.
        sense.clear()  # Clear the LED matrix
        time.sleep(1)  # Time to wait before the next reading
        if temp > 29 or humidity > 79:
            sense.show_message("Warning: High Temperature or Humidity" + str(temp) + "°C" + str(humidity) + "%", text_colour=[255, 0, 0])  # Red text for alert
        elif temp < 24 or humidity < 60:
            sense.show_message("Warning: Low Temperature or Humidity" + str(temp) + "°C" + str(humidity) + "%", text_colour=[255, 0, 0])  # Red text for alert
        else:
            sense.show_message("normal conditions good job" + str(temp) + "°C" + str(humidity) + "%", text_colour=[0, 255, 0])  # Green
    
    elif mode == 2: # night mode = frog wants colder with the same humidity as frog mode.
        sense.clear()  # Clear the LED matrix
        time.sleep(1)  # Time to wait before the next reading
        if temp < 25 or humidity < 79:
            sense.show_message("warning: temperature or humidity too high " + str(temp) + "°C" + str(humidity) + "%", text_colour=[220, 0, 220])  # Purple text for night mode
        elif temp > 18 or humidity > 60:
            sense.show_message("warning: temperature or humidity too low " + str(temp) + "°C" + str(humidity) + "%", text_colour=[220, 0, 220])  # Purple text for night mode
        else:
            sense.show_message("normal conditions good job" + str(temp) + "°C" + str(humidity) + "%", text_colour=[0, 220, 0])  # When conditions are normal
    elif mode == 3: # normal monitoring mode
        sense.clear()  # Clear the LED matrix
        time.sleep(1)  # Time to wait before the next reading
        sense.show_message("Normal Mode: Room Monitoring active" + str(temp) + "°C" + str(humidity) + "%", text_colour=[0, 220, 220])  # White text for normal mode 

time.sleep(20)  # Wait for 20 seconds before the next reading
