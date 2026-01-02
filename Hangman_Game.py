import random

# ASCII Hangman stages
HANGMAN_PICS = [
    """
       -----
       |   |
           |
           |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    --------
    """
]

def choose_word(level):
    easy_words = ["apple", "ball", "cat", "dog"]
    hard_words = ["python", "coding", "internship", "program"]

    if level == "easy":
        return random.choice(easy_words), 6
    else:
        return random.choice(hard_words), 4


def hangman_game():
    print("=" * 50)
    print("🎮 HANGMAN GAME 🎮".center(50))
    print("=" * 50)

    level = input("Choose difficulty (easy / hard): ").lower()
    if level not in ["easy", "hard"]:
        print("Invalid choice! Defaulting to EASY.")
        level = "easy"

    word, attempts = choose_word(level)

    guessed_word = ["_"] * len(word)
    guessed_letters = set()   # ✅ set() used

    while attempts > 0 and "_" in guessed_word:
        print(HANGMAN_PICS[6 - attempts])
        print("\nWord:", " ".join(guessed_word))
        print("Guessed letters:", ", ".join(sorted(guessed_letters)))
        print("Attempts left:", attempts)

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Enter only one alphabet.")
            continue

        if guess in guessed_letters:
            print("🔁 Letter already guessed!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Correct!")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            print("❌ Wrong!")
            attempts -= 1

    print(HANGMAN_PICS[6 - attempts])
    if "_" not in guessed_word:
        print("\n🎉 YOU WON! 🎉")
        print("The word was:", word)
    else:
        print("\n💀 GAME OVER 💀")
        print("The word was:", word)


# 🔁 Replay option
while True:
    hangman_game()
    again = input("\nPlay again? (yes / no): ").lower()
    if again != "yes":
        print("\n🙏 Thanks for playing Hangman!")
        break
