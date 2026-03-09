
from colorama import Fore,Back,Style
from games.number_recall import NumberRecall
from games.pair_match import PairMatch
from games.category_recall import CategoryRecall
from games.story_recall import StoryRecall
from summary import show_summary



username=input( "Welcome to " +Fore.BLUE+ "-- Memory Challenge🧠 --"+Fore.RESET+ "\npleas enter your name: ").strip().lower()


number_recall_game = NumberRecall(username)
pair_match_game = PairMatch(username)
category_recall_game = CategoryRecall(username)
story_recall_game = StoryRecall(username)


def game_screen():

    
    menu = f'''
{Fore.BLUE}Choose the game: {Fore.RESET}
------------
{Fore.YELLOW}1{Style.RESET_ALL} - Number Recall
{Fore.YELLOW}2{Style.RESET_ALL} - Pair Match
{Fore.YELLOW}3{Style.RESET_ALL} - Category Recall
{Fore.YELLOW}4{Style.RESET_ALL} - Story Recall
{Fore.YELLOW}5{Style.RESET_ALL} - Back
'''

    while True:
        user_input = input(menu)

        match user_input:
            case "1":
                number_recall_game.play()

            case "2":
                pair_match_game.play()

            case "3":
                category_recall_game.play()

            case "4":
                story_recall_game.play()

            case "5":
                break

            case _:
                print("Enter a valid number")


menu = f'''
{Fore.CYAN}🎮 Main Menu{Style.RESET_ALL}
------------
{Fore.YELLOW}1{Style.RESET_ALL} - Play Games
{Fore.YELLOW}2{Style.RESET_ALL} - View Summary
{Fore.YELLOW}3{Style.RESET_ALL} - Exit
'''


while True:
    user_choose = input(menu)

    match user_choose:
        case "1":
            game_screen()

        case "2":
            show_summary(username)

        case "3":
            print("Goodbye! 👋")
            break

        case _:
            print(Fore.RED+ "Enter a valid number"+Fore.RESET)