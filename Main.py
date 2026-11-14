from sense_hat import SenseHat
import time
import configparser

config = configparser.ConfigParser()
config.read("TerraPi/settings.ini")
MessageSpeed = float(config["settings"]["MessageSpeed"])
Mode = config["settings"]["Mode"]
TemperatureUnit = config["settings"]["TemperatureUnit"]


sense = SenseHat()
temperature = sense.get_temperature()
if Mode == "None":
    print("Mode is not set.")
    sense.show_message("Mode is not set.", scroll_speed=MessageSpeed)
elif Mode == "Pacman": 
    print("Pacman mode activated.")
    import Pacman


if TemperatureUnit == "Celsius":
    ## Temperature unit set to Celsius
    TemperatureUnit = "C"
    temperature = temperature # No conversion needed for Celsius
    
elif TemperatureUnit == "Fahrenheit":
    ## Temperature unit set to Fahrenheit
    TemperatureUnit = "F"
    temperature = temperature * 9 / 5 + 32
else:
    ## Temperature unit set to Celsius
    TemperatureUnit = "C"
    temperature = temperature # No conversion needed for Celsius
