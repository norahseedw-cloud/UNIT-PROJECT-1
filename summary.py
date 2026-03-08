from storage import load_scores


def show_summary(username):

    data = load_scores()

    if username not in data:
        print("No scores found for this user.")
        return

    user_games = data[username]

    print("\n========= SUMMARY =========")
    print(f"Player: {username}")

    total_scores = []

    for game, levels in user_games.items():

        print(f"\n{game}")

        for level in ["Easy", "Medium", "Hard"]:

            score = levels.get(level, "-")

            print(f"  {level:<6} : {score}")

            if isinstance(score, int):
                total_scores.append(score)

    if total_scores:
        avg = sum(total_scores) / len(total_scores)
        print(f"\nOverall Average: {avg:.2f}")