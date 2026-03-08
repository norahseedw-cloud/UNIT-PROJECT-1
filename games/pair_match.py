import random
from games.base_game import Game
from storage import save_score

class PairMatch(Game):

    def __init__(self, username):
        super().__init__(username)

    def pairs(self, count):
        """
    This function generates letter-number pairs for the player to memorize.
    ---------------
count : int
        The number of pairs to generate.
    """
        letters = ["A", "B", "C", "D", "E"]
        selected_letters = letters[:count]

        numbers = [random.randint(0, 100) for _ in range(count)] # Random number
        self.pairs_dict = dict(zip(selected_letters, numbers)) # To add two together 

        for letter, number in self.pairs_dict.items():
            print(f"{letter} - {number}")


    def play_level(self, count):
        """
    Runs a round of the Pair Matching game.
    The player memorizes letter-number pairs and tries to recall them.
    ---------------
    count : int
        Number of letter-number pairs shown to the player.
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

            self.pairs(count)
            self.timer(5)
            self.clear_screen()

            attempts = 3
            correct_letters = {letter: False for letter in self.pairs_dict}

            while attempts > 0:

                self.display_header("Pair Matching", attempts)
                score_this_round = 0
                try:
                    for letter in self.pairs_dict:

                        if not correct_letters[letter]:

                            ask = int(input(f"What number was with {letter}: "))

                            if ask == self.pairs_dict[letter]:
                                print(f"{letter} is correct!")
                                correct_letters[letter] = True
                                score_this_round += 1
                            else:
                                print(f"{letter} is incorrect!")

                except ValueError:
                    print("Please enter numbers only!")
                    continue

                self.score += score_this_round

                if all(correct_letters.values()):
                    print("All answers are correct!")
                    break

                attempts -= 1

                if attempts > 0:
                    print("Try again!")
                else:
                    print("Unfortunately, all your attempts have failed this round.")
                    for letter, number in self.pairs_dict.items():
                        print(f"{letter}: {number}")

            print(f"Your score: {self.score}")

            choice = self.get_choice("Play another round? (y/n): ", ["y", "n"])

            if choice == "n":
                print(f"\nFinal score: {self.score}")
                save_score(self.username, "Pair Match", self.score, self.level)
                print("Thanks for playing!")
                break

            round_number += 1

    def easy_level(self):
        self.level="Easy"
        self.play_level(2)

    def medium_level(self):
        self.level="Medium"
        self.play_level(3)

    def hard_level(self):
      self.level="Hard"
      self.play_level(4)   


    def practice(self):

        print("--- Practice Mode ---")
        print("You will see letters with numbers for a few seconds.")
        print("Try to remember the number with each letter.")
        print("After the screen clears, type the correct number.\n")
        while True:
            try:
                choice = input("Press Enter to start \n(Enter 0 to go back)\ ")

                if choice == "":
                    break   

                if choice == "0":
                    return  

                raise Exception("Please enter a valid input")

            except Exception as e:
                print(e)


        self.pairs(2)  
        self.timer(5)
        self.clear_screen()

        try:
            for letter in self.pairs_dict:

                ask = int(input(f"What number was with {letter}: "))

                if ask == self.pairs_dict[letter]:
                    print(f"{letter} is correct!")
                else:
                    print(f"{letter} is incorrect!")
                    print(f"The correct number was {self.pairs_dict[letter]}")

        except ValueError:
            print("Please enter numbers only!")

        print("Practice finished!") 

    def display_game(self):
        
        self.choose_level(self.easy_level, self.medium_level, self.hard_level)

    def play(self):
        self.Secound_main(self.display_game, self.practice)


