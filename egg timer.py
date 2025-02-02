# egg timer
import os
import time
import warnings
import winsound
import threading

warnings.filterwarnings("ignore")

print(" _____ _____ _____   _____ ________  ___ ___________  \n"
      "|  ___|  __ \  __ \ |_   _|_   _|  \/  ||  ___| ___ \ \n"
      "| |__ | |  \/ |  \/   | |   | | | .  . || |__ | |_/ / \n"
      "|  __|| | __| | __    | |   | | | |\/| ||  __||    /  \n"
      "| |___| |_\ \ |_\ \   | |  _| |_| |  | || |___| |\ \  \n"
      "\____/ \____/\____/   \_/  \___/\_|  |_/\____/\_| \_| \n"
      "                                                      \n"
      "                                                      \n")

mins = int(input("input min: "))
secs = int(input("input secs: "))

checksecs = secs % 60

if secs == 60:
    mins += 1

elif secs > 60 and checksecs == 0:
    mins += secs // 60

elif secs > 60 and checksecs != 0:
    mins += secs // 60
    secs += checksecs

sectime = (mins * 60) + secs

while sectime != 0:
    if secs < 0:
        mins -= 1
        secs = 59

    prettysecs = secs

    if secs < 10:
        prettysecs = "0" + str(secs)

    print(f"time left: {mins}:{prettysecs}", end='\r', flush=True)
    time.sleep(1)
    sectime -= 1
    secs -= 1

print("\nEGGS READY")

def play_sound():
    youser = os.getenv(r'USERNAME')
    winsound.PlaySound(f"C:/Users/{youser}/Downloads/USSR.wav", winsound.SND_FILENAME)

sound_thread = threading.Thread(target=play_sound)
sound_thread.start()

songmins = 3
songsecs = 44
songtime = (songmins * 60) + songsecs

while songtime != 0:
    if songsecs < 0:
        songmins -= 1
        songsecs = 59

    prettysongsecs = songsecs

    if songsecs < 10:
        prettysongsecs = "0" + str(songsecs)

    print(f"song time left: {songmins}:{prettysongsecs}", end='\r', flush=True)
    time.sleep(1)
    songtime -= 1
    songsecs -= 1

print("\nSONG ENDED")
