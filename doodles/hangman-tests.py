
# list_variable = "apple"

# print(list_variable)

# for char in list_variable:
#     print(char)

# print("Variable as list:\n", list(list_variable))

# -------------------

import random

end_of_game = False
word_list = ["cat", "gazelle", "puma"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

lives = 6

while not end_of_game:
    guess = input("Guess a letter:\t").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1

    if lives == 0:
        print("You lose.")
        end_of_game = True

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")
