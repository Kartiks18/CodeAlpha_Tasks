import random

words = ["python", "java", "sql", "reactjs", "html"]

hangman_art = {
    0: (" ", " ", " "),
    1: ("O", " ", " "),
    2: ("O", "|", " "),
    3: ("O", "/|", " "),
    4: ("O", "/|\\", " "),
    5: ("O", "/|\\", "/"),
    6: ("O", "/|\\", "/ \\")
}

def display_man(wrong_guesses):
    print("-----------")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("-----------")

def display_hint(hint):
    print(" ".join(hint))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()

    while wrong_guesses < 6 and "_" in hint:
        display_man(wrong_guesses)
        display_hint(hint)

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
            print("Wrong guess!")

    display_man(wrong_guesses)

    if "_" not in hint:
        print("🎉 Congratulations! You won!")
        print("Word:", answer)
    else:
        print("💀 You lost!")
        print("Correct word:", answer)

if __name__ == "__main__":
    main()
