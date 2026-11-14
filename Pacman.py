from pdb import run

from sense_hat import SenseHat
import configparser 
import time
import Main
config = configparser.ConfigParser()
config.read("TerraPi/settings.ini")
Pacman_Temptiming = int(config["settings"]["Pacman_Temptiming"])
MessageSpeed = float(config["settings"]["MessageSpeed"])
Mode = config["settings"]["Mode"]
TemperatureUnit = config["settings"]["TemperatureUnit"]

Gr = (0, 255, 0)    # Green for frog body
Bl = (0, 0, 0)      # Black for empty space
Ye = (255, 255, 0)  # Yellow for mouth

sense = SenseHat()

# 8x8 Pacman Frog pixel art
PacmanArt = [
        [Bl,Gr,Gr,Gr,Gr,Gr,Gr,Bl],
        [Gr,Gr,Gr,Gr,Gr,Gr,Gr,Gr],
        [Gr,Gr,Bl,Bl,Bl,Bl,Gr,Gr],
        [Gr,Gr,Bl,Ye,Bl,Bl,Gr,Gr],
        [Gr,Gr,Bl,Ye,Ye,Ye,Gr,Gr],
        [Gr,Gr,Bl,Ye,Ye,Ye,Gr,Gr],
        [Gr,Gr,Gr,Gr,Gr,Gr,Gr,Gr],
        [Bl,Gr,Gr,Gr,Gr,Gr,Gr,Bl]
        ]
sense.set_pixels([pixel for row in PacmanArt for pixel in row])
time.sleep(5)
sense.clear()
time.sleep(1)  # Add a short delay before ending the function

def run():
    print(str(Main.temperature) + Main.TemperatureUnit)
    sense.show_message(str(Main.temperature) + Main.TemperatureUnit, scroll_speed=MessageSpeed)
    time.sleep(Pacman_Temptiming)  # Add a short delay after showing the message
    sense.clear()


run()