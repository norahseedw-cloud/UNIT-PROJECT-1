import random
from base_game import Game

class PairMatch(Game):

    def pairs(self, count):
        letters = ["A", "B", "C", "D", "E"]
        selected_letters = letters[:count]

        numbers = [random.randint(0, 100) for _ in range(count)]
        self.pairs_dict = dict(zip(selected_letters, numbers))

        for letter, number in self.pairs_dict.items():
            print(f"{letter} - {number}")


    def play_level(self, count):

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
                    print("All answers are correct! Very Good")
                    break

                attempts -= 1

                if attempts > 0:
                    print("Try again!")
                else:
                    print("Unfortunately, all your attempts have failed this round.")
                    for letter, number in self.pairs_dict.items():
                        print(f"{letter}: {number}")

            print(f"Your score: {self.score}")

            choice = input("Do you want another round? (y/n): ").lower()

            if choice != "y":
                print(f"\nYour final score is: {self.score}")
                print("Thanks for playing! Goodbye.")
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

    def display_game(self):
        
        self.choose_level(self.easy_level, self.medium_level, self.hard_level)

    def play(self):
        self.Secound_main(self.display_game, self.display_game)


pair_match1 = PairMatch()
pair_match1.play()