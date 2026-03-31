import random

words = ["apple", "mango", "banana"]

hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    
    1: (" ° ",
        "   ",
        "   "),
    
    2: (" ° ",
        " | ",
        "   "),
    
    3: (" ° ",
        "/| ",
        "   "),
    
    4: (" ° ",
        "/|\\",
        "   "),
    
    5: (" ° ",
        "/|\\",
        "/  "),
    
    6: (" ° ",
        "/|\\",
        "/ \\")
}


def display_game(wrong_guess):
    for line in hangman_art[wrong_guess]:  # FIXED name
        print(line)
    print("**********************************")


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)   # FIXED variable name
    wrong_guess = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_game(wrong_guess)
        display_hint(hint)

        guess = input("Enter a letter: ").lower()

        # validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print("Already guessed!")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guess += 1

        # win condition
        if "_" not in hint:
            display_game(wrong_guess)
            display_answer(answer)
            print("🎉 You win!")
            is_running = False

        # lose condition
        elif wrong_guess >= len(hangman_art) - 1:
            display_game(wrong_guess)
            display_answer(answer)
            print("💀 You lose!")
            is_running = False


if __name__ == "__main__":
    main()
