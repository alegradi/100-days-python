import pandas


# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
# print(nato_alphabet)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Please enter a word: ")
user_input_upper_list = [word.upper() for word in user_input]

# print(user_input_upper_list)

phonetic_word = []
for letter in user_input_upper_list:
    phonetic_word += [value for (key, value) in nato_alphabet.items() if key == letter]

print(phonetic_word)
