import random

def choose_word():
    words = ["python", "puzzle", "program", "algorithm", "computer", "challenge", "scramble"]
    return random.choice(words)

def scramble_word(word):
    scrambled = list(word)
    random.shuffle(scrambled)
    return "".join(scrambled)

def play_game():
    word = choose_word()
    scrambled = scramble_word(word)

    print("🔤 Welcome to Word Scramble Puzzle!")
    print("Unscramble the letters to find the correct word.")
    print("Scrambled word:", scrambled)

    attempts = 3
    while attempts > 0:
        guess = input("Your guess: ").lower().strip()
        if guess == word:
            print("🎉 Correct! You solved it!")
            break
        else:
            attempts -= 1
            print(f"❌ Nope! {attempts} attempts left.")

    if attempts == 0:
        print(f"😢 Game Over! The word was: {word}")

if __name__ == "__main__":
    play_game()
