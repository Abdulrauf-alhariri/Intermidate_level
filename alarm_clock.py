from tkinter import *
import pygame
import webbrowser
from datetime import datetime
import time
import random

root = Tk()
pygame.init()


class Timer:

    def __init__(self, hours, minutes, seconds, links):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

        self.links = links

        self.hour_entery = Entry(root, textvariable=self.hours,
                                 font=("Arial", 18, ""), width=7, bd=7)
        self.minutes_entry = Entry(root, textvariable=self.minutes,
                                   font=("Arial", 18, ""), width=7, bd=7)
        self.seconds_entry = Entry(root, textvariable=self.seconds,
                                   font=("Arial", 18, ""), width=7, bd=7)

        # We are placing the entry in rows and columns
        self.hour_entery.grid(row=0, column=0, pady=10)
        self.minutes_entry.grid(row=0, column=1, pady=10)
        self.seconds_entry.grid(row=0, column=2, pady=10)

    @classmethod
    def default(cls):

        # We are creating the default value for the Entry
        hours = StringVar()
        minutes = StringVar()
        seconds = StringVar()

        # We are seting the default value to time now (hours, minutes)
        hours.set(datetime.now().hour)
        minutes.set(datetime.now().minute)
        seconds.set(datetime.now().second)

        # The youtube links that we gonna choice from
        links = ["https://www.youtube.com/watch?v=3NndCfFQNHA", "https://www.youtube.com/watch?v=WKuNWrxuJ9g",
                 "https://www.youtube.com/watch?v=DFOOq3mwL4o", "https://www.youtube.com/watch?v=Nj-hdQMa3uA",
                 "https://www.youtube.com/watch?v=j1fc0FlCjyI", "https://www.youtube.com/watch?v=LeYsRMZFUq0",
                 "https://www.youtube.com/watch?v=FzcfZyEhOoI", "https://www.youtube.com/watch?v=Z-pT0XDYvDM"]

        # We are opening a new file and we are writing a link in each line
        with open("links.txt", "w") as link_file:
            for link in links:
                link_file.write(link)
                link_file.write("\n")

        # We are reding the file and adding each link to a list
        # Then we are picking up a random link to open in our browser
        with open("links.txt", "r") as link_file:
            youtube_links = []
            reader = link_file.readlines()
            for line in reader:
                youtube_links.append(line)

        return cls(hours, minutes, seconds, random.choice(youtube_links))

    def timer(self):
        hours = self.hours
        minutes = self.minutes
        sekunder_nu = self.seconds

        # We are getting the secunds now and the seconds of the given time
        # We are getting the diffrence of the given time and time right now
        try:
            sekunder_defult = int(datetime.now().hour) * \
                3600 + int(datetime.now().minute) * 60 + \
                int(datetime.now().second)

            sekunder = int(hours.get()) * 3600 + \
                int(minutes.get()) * 60 - sekunder_defult

        except:
            print("Enter a vaild value")

        while sekunder > -1:

            # we are getting the quotient and rest
            hour, sec = divmod(sekunder, 3600)
            minuter, sec = divmod(sec, 60)

            hours.set("{0:2d}".format(hour))
            minutes.set("{0:2d}".format(minuter))
            sekunder_nu.set("{0:2d}".format(sec))

            root.update()
            time.sleep(1)
            if sekunder == 0:
                pygame.mixer.music.load(
                    "C:\\Users\\abdullrauf.alhariri\\Desktop\\HelloWorld\\Intermidiate_level\\alarm_appliction\\alarm_clock_2010.mp3")
                pygame.mixer.music.play()

                # Opening the youtube vedio
                link = self.links
                webbrowser.open(link)

            sekunder -= 1


if __name__ == "__main__":
    play = Timer.default()

    # We are creating the button to set the alarm
    set_button = Button(root, text="Set Alarm", font=(
        "Arial", 15, ""), command=play.timer)

    set_button.grid(row=1, column=1)

    root.mainloop()
