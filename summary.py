from storage import load_scores
from colorama import Fore, Back


def sum_scores_recursive(scores):
    if not scores:
        return 0
    return scores[0] + sum_scores_recursive(scores[1:])


calculate_average = lambda total, count: total / count


def show_summary(username):

    data = load_scores()

    if username not in data:
        print(Fore.RED + "No scores found for this user." + Fore.RESET)
        return

    user_games = data[username]

    print(Fore.BLUE + "\n------- SUMMARY -------" + Fore.RESET)
    print(f"Player: {Fore.MAGENTA}{username}{Fore.RESET}")

    total_scores = []

    for game, levels in user_games.items():

        print(f"\n{Back.LIGHTCYAN_EX}{game}{Back.RESET}")

        for level in ["Easy", "Medium", "Hard"]:

            score = levels.get(level, "-")

            print(f"  {level:<6} : {Fore.YELLOW}{score}{Fore.RESET}")

            if isinstance(score, int):
                total_scores.append(score)

    if total_scores:
        total = sum_scores_recursive(total_scores)
        avgrage = calculate_average(total, len(total_scores))

        print(f"\n{Back.GREEN}Overall Average:{Back.RESET} {Fore.YELLOW}{avgrage:.2f}{Fore.RESET}")