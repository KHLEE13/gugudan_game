import random


def ask_question():
    dan = random.randint(2, 9)
    num = random.randint(1, 9)
    return dan, num, dan * num


def ask_rounds(default=5):
    prompt = f"How many questions? Default is {default}. (Enter = default) "
    raw = input(prompt).strip()
    if not raw:
        return default
    try:
        rounds = int(raw)
        if rounds <= 0:
            raise ValueError
        return rounds
    except ValueError:
        print("Invalid input; using the default.\n")
        return default


def play_gugudan(rounds):
    print("Multiplication quiz! Type the number or 'q' to quit.\n")
    score = 0
    for idx in range(1, rounds + 1):
        dan, num, answer = ask_question()
        while True:
            guess = input(f"[{idx}/{rounds}] {dan} x {num} = ").strip()
            if guess.lower() in {"q", "quit"}:
                print("Quitting the game.\n")
                return score, idx - 1
            try:
                user_answer = int(guess)
            except ValueError:
                print("Type a number or 'q' to quit.")
                continue

            if user_answer == answer:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong; the answer is {answer}.\n")
            break
    return score, rounds


if __name__ == "__main__":
    total_rounds = ask_rounds()
    correct, played = play_gugudan(total_rounds)
    print(f"Score: {correct}/{played} correct.")
