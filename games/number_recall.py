import random
from base_game import Game


class NumberRecall(Game):

    def generate_number(self, digits):
        """
    This function generates a random number with a specific number
    of digits and displays it spaced out for the user to memorize.
    ---------------
    digits : int
        The number of digits to generate in the random number.
    """
        number = ""
        for _ in range(digits):
            number += str(random.randint(0, 9))

        self.number_to_remember = number

        display_number = " ".join(number)  
        print(f"\nRemember this number:\n{display_number}")


    def play_level(self, digits, attempts):
        """
    Runs a round of the Number Recall game.
    The player memorizes a number and tries to recall it.

    ---------------
    digits : int
        Number of digits in the generated number.
    attempts : int
        Number of attempts allowed for the player.
    """
        while True:
            try:
                choice = input("Press Enter to start \n(Enter 0 to go back)\n ")

                if choice == "":
                    break

                if choice == "0":
                    return

                raise ValueError("Please enter a valid input")

            except ValueError as e:
                print(e)

        round_number = 1

        while True:

            print(f"\n--- Round {round_number} ---")

            self.generate_number(digits)
            self.timer(5)
            self.clear_screen()

            attempts_left = attempts

            while attempts_left > 0:

                self.display_header("Number Recall", attempts_left)

                user_answer = input("Enter the number: ")

                if user_answer == self.number_to_remember:
                    print("Correct!")
                    self.score += 1
                    break
                else:
                    print("Incorrect!")

                attempts_left -= 1

                if attempts_left > 0:
                    print("Wrong! Try again..")
                else:
                    print(f"The correct number was {self.number_to_remember}")

            print(f"Your score: {self.score}")

            choice = self.get_choice("Play another round? (y/n): ", ["y", "n"])

            if choice == "n":
                print(f"\nFinal score: {self.score}")
                print("Thanks for playing!")
                break

            round_number += 1


    def easy_level(self):
        self.level = "Easy"
        self.play_level(3, 3)  

    def medium_level(self):
        self.level = "Medium"
        self.play_level(5, 3)  


    def hard_level(self):
        self.level = "Hard"
        self.play_level(7, 3)   


    def practice(self):

        print("--- Practice Mode ---")
        print("You will see a number for a few seconds.")
        print("Try to remember it and type it after the screen clears.\n")

        while True:
            try:
                choice = input("Press Enter to start \n(Enter 0 to go back)\n ")

                if choice == "":
                    break

                if choice == "0":
                    return

                raise Exception("Please enter a valid input")

            except Exception as e:
                print(e)

        self.generate_number(3)
        self.timer(5)
        self.clear_screen()

        user_answer = input("Enter the number: ")

        if user_answer == self.number_to_remember:
            print("Correct!")
        else:
            print("Incorrect!")
            print(f"The correct number was {self.number_to_remember}")

        print("Practice finished!")


    def display_game(self):
        self.choose_level(self.easy_level, self.medium_level, self.hard_level)


    def play(self):
        self.Secound_main(self.display_game, self.practice)


number_game = NumberRecall()
number_game.play()