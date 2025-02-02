import os
import time
import warnings
import winsound
import threading

warnings.filterwarnings("ignore")

def print_ascii_art():
    art = (
        " _____ _____ _____   _____ ________  ___ ___________  \n"
        "|  ___|  __ \\  __ \\ |_   _|_   _|  \\/  ||  ___| ___ \\ \n"
        "| |__ | |  \\/ |  \\/   | |   | | | .  . || |__ | |_/ / \n"
        "|  __|| | __| | __    | |   | | | |\\/| ||  __||    /  \n"
        "| |___| |_\\ \\ |_\\ \\   | |  _| |_| |  | || |___| |\\ \\  \n"
        "\\____/ \\____/\\____/   \\_/  \\___/\\_|  |_/\\____/\\_| \\_| \n"
        "                                                      \n"
        "                                                      \n"
    )
    print(art)

def play_sound():
    user = os.getenv('USERNAME')
    sound_path = f"C:/Users/{user}/Downloads/USSR.wav"
    winsound.PlaySound(sound_path, winsound.SND_FILENAME)

def countdown_timer(minutes, seconds):
    total_seconds = (minutes * 60) + seconds
    while total_seconds != 0:
        if seconds < 0:
            minutes -= 1
            seconds = 59
        pretty_seconds = f"{seconds:02}"
        print(f"time left: {minutes}:{pretty_seconds}", end='\r', flush=True)
        time.sleep(1)
        total_seconds -= 1
        seconds -= 1
    print("\nEGGS READY")

def song_timer(minutes, seconds):
    total_seconds = (minutes * 60) + seconds
    while total_seconds != 0:
        if seconds < 0:
            minutes -= 1
            seconds = 59
        pretty_seconds = f"{seconds:02}"
        print(f"song time left: {minutes}:{pretty_seconds}", end='\r', flush=True)
        time.sleep(1)
        total_seconds -= 1
        seconds -= 1
    print("\nSONG ENDED")

def main():
    print_ascii_art()

    mins = int(input("input min: "))
    secs = int(input("input secs: "))

    check_secs = secs % 60
    if secs == 60:
        mins += 1
    elif secs > 60 and check_secs == 0:
        mins += secs // 60
    elif secs > 60 and check_secs != 0:
        mins += secs // 60
        secs = check_secs

    countdown_timer(mins, secs)

    sound_thread = threading.Thread(target=play_sound)
    sound_thread.start()

    song_timer(3, 44)

if __name__ == "__main__":
    main()
