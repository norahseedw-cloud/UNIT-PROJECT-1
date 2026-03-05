import time
import os

class Game:


    def __init__(self):
        self.level = "Easy"
        self.score = 0


    def display_header(self, attempts=None):
        print(f"Level: {self.level}")
        print(f"Score: {self.score}")
        if attempts is not None:
            print(f"Attempts Left: {attempts}")

    def correct(self):
        self.score += 1
        print("Correct!")
        print(f"Score: {self.score}")

    def incorrect(self, attempts):
        print("Incorrect!")
        print(f"Attempts Left: {attempts}")

    def timer(self, seconds):
        for n in range(seconds, 0, -1):
            print(f"\rMemorize... {n}", end="")
            time.sleep(1)
        print()

    def clear_screen(self):
        os.system("cls" if os.name=="nt" else "clear")

    