import random

# List of words to choose from
word_list = ['python', 'hangman', 'challenge', 'programming', 'developer']


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = ['_'] * word_length
lives = 6
guessed_letters = []


stages = [
    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    '''
]

print("Welcome to Hangman!")


while lives > 0 and '_' in display:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for index in range(word_length):
            if chosen_word[index] == guess:
                display[index] = guess
        print("Correct guess!")
    else:
        lives -= 1
        print(f"Wrong guess! You lost a life. Lives remaining: {lives}")

    print(stages[6 - lives])
    print("Word: ", ' '.join(display))
    print("Guessed letters:", ', '.join(guessed_letters))


if '_' not in display:
    print("🎉 Congratulations! You guessed the word correctly!")
else:
    print(f"💀 Game Over! The word was '{chosen_word}'. Better luck next time.")

