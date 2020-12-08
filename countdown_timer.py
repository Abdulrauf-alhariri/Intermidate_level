import time
import sys


class Timer:
    def __init__(self, seconds):
        self.seconds = seconds

    def timer(self):
        sekonder = self.seconds
        hours, seconds = divmod(sekonder, 3600)
        minutes, seconds = divmod(seconds, 60)
        return (f"{hours:02}:{minutes:02}:{seconds:02}")


if __name__ == "__main__":
    seconds = int(input("Enter the lenght of the timer:"))
    while seconds:
        clock = Timer(seconds)
        print(clock.timer(), end="\r")
        seconds -= 1
        time.sleep(1)

    print("\n", "Wake up")
