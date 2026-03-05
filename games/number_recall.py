import os
import random
from base_game import Game


class NumberRecall(Game):

    levels = ["Easy", "Medium", "Hard"]

    level_settings = {
        "Easy": {"digits": 3, "attempts": 3},
        "Medium": {"digits": 5, "attempts": 2},
        "Hard": {"digits": 7, "attempts": 1}
    }

    rounds = 3

    def level_up(self):

        if self.correct_answer >= 2:

            current_index = self.levels.index(self.level)

            if current_index < len(self.levels) - 1:
                self.level = self.levels[current_index + 1]
                print(f"\nLevel Up! Now you are in {self.level}")

            self.correct_answer = 0
            return True

        else:
            print("Sorry, you can't move to the next level. Try again.")
            self.correct_answer = 0
            return False


    def play(self):

        digits_level = self.level_settings[self.level]["digits"]
        attempts = self.level_settings[self.level]["attempts"]

        choice = input("Press Enter to start \n(Enter 0 to go back)\n> ")
        if choice == "0":
            return

        self.correct_answer = 0

        for r in range(1, self.rounds + 1):

            if r > 1:
                input("\nPress Enter to start the next round...")

            self.display_header(attempts)
            print(f"\nRound {r}/{self.rounds}")

            real_number = "".join([str(random.randint(0, 9)) for _ in range(digits_level)])
            display_numbers = " ".join(real_number)

            print("\nMemorize this number:\n")
            print(display_numbers)

            self.timer(5)
            self.clear_screen()

            current_attempts = attempts

            while current_attempts > 0:

                ask_for_answer = input("What was the number? ")

                try:
                    if not ask_for_answer:
                        raise Exception("The answer can't be empty")

                    if not ask_for_answer.isdigit():
                        raise Exception("The answer must be numbers only")

                    if len(ask_for_answer) != digits_level:
                        raise Exception(f"The answer must be exactly {digits_level} numbers")

                except Exception as e:
                    print(e)
                    continue

                if ask_for_answer == real_number:

                    self.correct()
                    self.correct_answer += 1
                    break

                else:

                    current_attempts -= 1
                    self.incorrect(current_attempts)

            if current_attempts == 0:
                print("\nNo attempts left")
                print(f"The correct number was: {real_number}")

        level_passed = self.level_up()

        if level_passed:
            print("\nStarting next level...")
            self.play()
        else:
            return


    def main_number(self):

        menu = '''
Choose mode: 
1- Play
2- Practice
3- Go back
'''

        while True:

            user_choice = input(menu)

            match user_choice:

                case "1":
                    self.play()

                case "2":
                    self.play()

                case "3":
                    print("Go back")
                    break

                case _:
                    print("Enter a valid number")


numberuu = NumberRecall()
numberuu.main_number()